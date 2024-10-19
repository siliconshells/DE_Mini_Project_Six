from my_lib.extract import extract
from my_lib.transform import transform_n_load
import os
from my_lib.crud import (
    read_data,
    save_data,
    delete_data,
    update_data,
    get_table_columns,
)
from sql_scripts import query

column_map = {
    "air_quality_id": 0,
    "indicator_id": 1,
    "indicator_name": 2,
    "measure": 3,
    "measure_info": 4,
    "geo_type_name": 5,
    "geo_id": 6,
    "geo_place_name": 7,
    "time_period": 8,
    "start_date": 9,
    "data_value": 10,
    "fn_geo_id": 6,
    "fn_indicator_id": 1,
}


# Test extract
def test_extract():
    if os.path.exists("data/air_quality.csv"):
        os.remove("data/air_quality.csv")

    assert not os.path.exists("population_bar.png")

    extract(
        "https://data.cityofnewyork.us/resource/c3uy-2p5r.csv?$$app_token={0}&$limit=10000".format(
            os.getenv("APP_TOKEN")
        ),
        "air_quality.csv",
        ("time_period", "2021"),
        "unique_id",
    )

    assert os.path.exists("data/air_quality.csv")
    print("Extraction Test Successful")


# Test transform and load
def test_transform_and_load():
    result = transform_n_load(
        local_dataset="air_quality.csv",
        new_data_tables={
            "le88_tbl_air_quality": [
                "air_quality_id",
                "fn_indicator_id",
                "fn_geo_id",
                "time_period",
                "start_date",
                "data_value",
            ],
        },
        new_lookup_tables={
            "le88_tbl_indicator": [
                "indicator_id",
                "indicator_name",
                "measure",
                "measure_info",
            ],
            "le88_tbl_geo_data": ["geo_id", "geo_place_name", "geo_type_name"],
        },
        column_attributes={
            "air_quality_id": "INTEGER PRIMARY KEY",
            "indicator_id": "INTEGER PRIMARY KEY",
            "indicator_name": "STRING",
            "measure": "STRING",
            "measure_info": "STRING",
            "geo_type_name": "STRING",
            "geo_id": "INTEGER PRIMARY KEY",
            "geo_place_name": "STRING",
            "time_period": "STRING",
            "start_date": "STRING",
            "data_value": "REAL",
            "fn_indicator_id": "INTEGER",
            "fn_geo_id": "INTEGER",
        },
        column_map={
            "air_quality_id": 0,
            "indicator_id": 1,
            "indicator_name": 2,
            "measure": 3,
            "measure_info": 4,
            "geo_type_name": 5,
            "geo_id": 6,
            "geo_place_name": 7,
            "time_period": 8,
            "start_date": 9,
            "data_value": 10,
            "fn_geo_id": 6,
            "fn_indicator_id": 1,
        },
    )
    assert result == "Transform and load Successful"
    print("Transform and Load Test Successful")


# Test read data
def test_read_data():
    rows = read_data(
        query.query_one_record, ["le88_tbl_air_quality", "air_quality_id", 823470]
    )
    assert rows[0]["data_value"] == 6
    print("Record Reading Test Successful")


# Test save data
def test_save_data():
    result = read_data(query.query_one_record, ["le88_tbl_geo_data", "geo_id", 100000])
    assert result is None

    save_data("le88_tbl_geo_data", ["100000", "Lancaster", "UFO"])

    result = read_data(query.query_one_record, ["le88_tbl_geo_data", "geo_id", 100000])
    assert len(result) == 1

    print("Record Saving Test Successful")


# Test update data
def test_update_data():

    result = read_data(query.query_one_record, ["le88_tbl_geo_data", "geo_id", 100000])
    assert result[0][1] == "Lancaster"

    update_data("le88_tbl_geo_data", {"geo_place_name": "Duke"}, 100000)

    result = read_data(query.query_one_record, ["le88_tbl_geo_data", "geo_id", 100000])
    assert result[0][1] == "Duke"

    print("Record Update Test Successful")


# Test delete data
def test_delete_data():

    result = read_data(query.query_one_record, ["le88_tbl_geo_data", "geo_id", 100000])
    assert len(result) == 1

    print(delete_data("le88_tbl_geo_data", 100000))

    result = read_data(query.query_one_record, ["le88_tbl_geo_data", "geo_id", 100000])
    assert result is None

    print("Record Deletion Test Successful")


# Test read all column names
def test_get_table_columns():
    columns = get_table_columns("le88_tbl_air_quality")
    assert len(columns.split(",")) == 6
    print("Reading All Column Test Successful")


if __name__ == "__main__":
    test_extract()
    test_transform_and_load()
    test_read_data()
    test_save_data()
    test_update_data()
    test_delete_data()
    test_get_table_columns()
