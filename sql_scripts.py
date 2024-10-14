class query:
    query_one_record = "select * from {0} where {1} = {2}"

    indicators = "select * from le88_tbl_indicator"

    air_quality_indicators_average = """
        SELECT indicator_name, 
            COUNT(indicator_name) AS indicator_occurances,
            AVG(data_value) AS avg_air_quality,
            MIN(data_value) AS min_air_quality,
            MAX(data_value) AS max_air_quality
            FROM le88_tbl_air_quality
            JOIN le88_tbl_indicator on
            le88_tbl_indicator.indicator_id = le88_tbl_air_quality.fn_indicator_id
            GROUP BY indicator_name
            ORDER BY indicator_name
    """

    air_quality_location_indicator_average = """
        SELECT  geo_place_name,
            COUNT(fn_indicator_id) AS {0},
            CAST(AVG(data_value) as DECIMAL(10,2)) AS avg_air_quality,
            CAST(MIN(data_value) as DECIMAL(10,2)) AS min_air_quality,
            CAST(MAX(data_value) as DECIMAL(10,2)) AS max_air_quality
            FROM le88_tbl_air_quality
            JOIN le88_tbl_geo_data on 
            le88_tbl_geo_data.geo_id = le88_tbl_air_quality.fn_geo_id
            GROUP BY fn_indicator_id, geo_place_name
            HAVING fn_indicator_id = {1}
            ORDER BY geo_place_name
    """
