"""
Transform the extracted data 
"""

import csv
from my_lib.db_connector import connect_to_databricks
from my_lib.util import test_numeric


def create_table(cursor, table, columns, column_attributes):
    col_attrib_list = [(f"{col} {column_attributes[col]}") for col in columns]
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(col_attrib_list)})")


def check_table_exists(table_name: str):
    conn = connect_to_databricks()
    c = conn.cursor()
    to_execute = f"""SELECT EXISTS (
        SELECT * FROM ids706_data_engineering.information_schema.tables 
        WHERE table_schema = 'default'
        AND table_name = '{table_name}' );
        """
    result = c.execute(to_execute).fetchall()[0].asDict()
    c.close()
    conn.close()
    return result["exists()"]


# load the csv file and insert into the database
def transform_n_load(
    local_dataset: str,
    new_data_tables: dict,
    new_lookup_tables: dict,
    column_attributes: dict,
    column_map: dict,
):
    """ "Transforms and Loads data into the database"""

    # DON'T TRANSFORM AND LOAD IF ANY OF THE TABLES EXIST
    for table in new_data_tables.keys():
        if check_table_exists(table):
            return f"{table} already exists."
    for table in new_lookup_tables.keys():
        if check_table_exists(table):
            return f"{table} already exists."

    # load the data from the csv
    reader = csv.reader(open("data/" + local_dataset, newline=""), delimiter=",")

    conn = connect_to_databricks()
    c = conn.cursor()

    try:
        # Create tables
        for k, v in new_data_tables.items():
            create_table(c, k, v, column_attributes)

        for k, v in new_lookup_tables.items():
            create_table(c, k, v, column_attributes)

        # skip the first row
        next(reader)

        loaded_lookups = dict()

        # To insert multiple rows for the main table only
        things_to_insert = dict()

        for row in reader:
            first_for_loop_broken = False
            # Insert lookup parts of the row
            for lookup_table, columns in new_lookup_tables.items():
                # If the ID is not a number don't import it
                # assuming Id is always integer
                if not test_numeric(row[column_map[columns[0]]]):
                    first_for_loop_broken = True
                    break  # Go to outer loop

                # Check if lookup part not in lookup table already
                id = int(float(row[column_map[columns[0]]]))
                row[column_map[columns[0]]] = str(id)  # to make sure it's int
                if not lookup_table in loaded_lookups.keys():
                    loaded_lookups[lookup_table] = []
                # If not already in lookup table, insert
                # Using a local variable to avoid checking in database for each iteration
                if not id in loaded_lookups[lookup_table]:
                    # pick columns of interest to this table out of the row
                    data_values = "', '".join(
                        [(row[column_map[col]]) for col in columns]
                    )
                    to_execute = f"INSERT INTO {lookup_table} ({', '.join(columns)}) VALUES ('{data_values}')"
                    c.execute(to_execute)
                    conn.commit()
                    loaded_lookups[lookup_table].append(id)

            # Only load the main data if all lookup information are there
            if not first_for_loop_broken:
                for k, v in new_data_tables.items():
                    # add table to temp dictionary
                    if not k in things_to_insert.keys():
                        things_to_insert[k] = []
                    # pick columns of interest to this table out of the row
                    data_values = "', '".join([(row[column_map[col]]) for col in v])
                    things_to_insert[k].append(f"('{data_values}')")

        # NOW INSERT ALL ITEMS IN EACH MAIN TABLE AT A GO TO REDUCE TRIPS TO DATABASE
        for atable, tuples_list in things_to_insert.items():
            to_execute = "INSERT INTO {0} ({1}) VALUES {2}".format(
                atable, ", ".join(new_data_tables[atable]), ",".join(tuples_list)
            )
            c.execute(to_execute)
            conn.commit()
    except Exception as error:
        print("Error in transform:", error)
        return "Transform and load Failed"
    finally:
        c.close()
        conn.close()

    return "Transform and load Successful"
