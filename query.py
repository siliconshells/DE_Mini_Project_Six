from my_lib.crud import read_data
from sql_scripts import query
import pandas as pd
import re
from my_lib.util import write_markdown


# Get the average air quality for the different indicators
def get_average_air_quality():
    rows, executed = read_data(query.air_quality_indicators_average, [], True)
    panda_table = pd.DataFrame([[col for col in row] for row in rows])
    panda_table = panda_table.rename(
        mapper={
            0: "Air Quality Indicator",
            1: "No of Occurances",
            2: "Average",
            3: "Minimum",
            4: "Maximum",
        },
        axis="columns",
    )
    panda_table.index = panda_table.index + 1

    write_markdown(
        "Different Air Quality indicator readings in New York for 2021",
        header=True,
        new_log_file=True,
    )
    write_markdown("The query executed was:")
    write_markdown(executed, True)
    write_markdown(
        "And the result was (column names renamed with the pandas 'rename' function):"
    )
    write_markdown(panda_table.to_markdown(), last_in_group=True)
    return "Query executed successfully"


# Get air quality for the each indicator for NY neighbourhoods
def get_location_average_air_quality():
    # Get the indicators
    rows = read_data(query.indicators, [])
    for indicator in rows:
        # Get average for locations
        # "".join([ c if c.isalnum() else "_" for c in s ])
        rows, executed = read_data(
            query.air_quality_location_indicator_average,
            [
                re.sub("[^0-9a-zA-Z]+", "_", indicator["indicator_name"]).lower(),
                indicator["indicator_id"],
            ],
            True,
        )
        panda_table = pd.DataFrame([[col for col in row] for row in rows])
        panda_table = panda_table.rename(
            mapper={
                0: "Location Name",
                1: indicator["indicator_name"] + " Occurrances",
                2: "Average",
                3: "Minimum",
                4: "Maximum",
            },
            axis="columns",
        )
        panda_table.index = panda_table.index + 1

        title = "{0} Air Quality in New York neighbourhoods for 2021".format(
            indicator["indicator_name"]
        )
        write_markdown(title, header=True)
        write_markdown("The query executed was:")
        write_markdown(executed, True)
        write_markdown(
            "And the result was (column names renamed with the pandas 'rename' function):"
        )
        write_markdown(panda_table.to_markdown(), last_in_group=True)

    return "Query executed successfully"


if __name__ == "__main__":
    print(get_average_air_quality())
    print(get_location_average_air_quality())
