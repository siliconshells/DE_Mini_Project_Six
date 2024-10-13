from my_lib.db_connector import connect_to_databricks


def get_table_columns(table_name: str):
    conn = connect_to_databricks()
    c = conn.cursor()
    to_execute = f"""SELECT column_name
        FROM ids706_data_engineering.information_schema.columns
        WHERE table_schema = 'default'
        AND table_name = '{table_name}' ;
        """
    rows = c.execute(to_execute).fetchall()
    c.close()
    conn.close()
    return ", ".join([row[0] for row in rows])


def get_primary_key(cursor, table_name):
    return cursor.execute(
        f"SELECT column_name FROM ids706_data_engineering.information_schema.columns WHERE table_name = '{table_name}' AND ordinal_position = 0"
    ).fetchone()[0]


def read_data(query: str, parameters: list, add_script=False):
    conn = connect_to_databricks()
    c = conn.cursor()

    parameters = [] if parameters is None else parameters
    to_execute = query.format(*parameters)
    result = c.execute(to_execute).fetchall()

    c.close()
    conn.close()

    if result:
        if add_script:
            return result, to_execute
        else:
            return result
    else:
        return None


def save_data(table_name: str, row: list):
    conn = connect_to_databricks()
    c = conn.cursor()
    col_names = ", ".join(get_table_columns(table_name))
    data_values = "', '".join(row)
    to_execute = f"INSERT INTO ids706_data_engineering.{table_name} ({col_names}) VALUES ('{data_values}')"
    c.execute(to_execute)
    conn.commit()
    c.close()
    conn.close()
    return "Save Successful"


def delete_data(table_name: str, data_id: int):
    conn = connect_to_databricks()
    c = conn.cursor()
    to_execute = f"delete from ids706_data_engineering.{table_name} where {get_primary_key(c, table_name)} = {data_id}"
    c.execute(to_execute)
    conn.commit()
    c.close()
    conn.close()
    return "Delete Successful"


def update_data(table_name: str, things_to_update: dict, data_id: int):
    conn = connect_to_databricks()
    c = conn.cursor()
    set_values = ", ".join(
        [(k + "='" + v + "'") for (k, v) in things_to_update.items()]
    )
    to_execute = f"UPDATE ids706_data_engineering.{table_name} SET {set_values} WHERE {get_primary_key(c, table_name)} = {data_id}"
    c.execute(to_execute)
    conn.commit()
    c.close()
    conn.close()
    return "Update Successful"
