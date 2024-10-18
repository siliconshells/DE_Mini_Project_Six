# Data Engineering Mini Project Six

[![CI](https://github.com/nogibjj/Leonard_Eshun_Mini_Project_Six/actions/workflows/workflow.yml/badge.svg)](https://github.com/nogibjj/Leonard_Eshun_Mini_Project_Six/actions/workflows/workflow.yml)


This repository is created as an assignment from the Data Engineering course, IDS 706. The aim is to create a python script that interacts with an SQL Database.

The requirements are:
1. Do the standard CI/CD setup
1. Connect to a SQL database
1. Perform CRUD operations
1. Design a complex SQL query involving joins, aggregation, and sorting
1. Provide an explanation for what the query is doing and the expected results


## The functions and what they do

1. **extract** to extract the read an external csv file via its url and save to file in the /data folder using the name you give it. This uses Pandas for more features.
	```python
	extract(url: str, file_name: str, column_contains: tuple, index_column: str) -> str
	```
	The parameters are:
	- url : The url for the external CSV file
	- file_name : The file name to use to save the CSV file locally
	- column_contains : This is for filtering by a column. Give it a tuple of column and value. Insert ```None``` if you don't want to use it.
	- index_column : Sets the index column to prevent pandas from providing an index column.   

	>**Note:**
	>Give the CSV file a header (first row).   

1. **extract** to extract the read an external csv file via its url and save to file in the /data folder using the name you give it. This overload uses request for simplicity.
	```python
	extract(url: str, file_name: str,) -> str
	```
	The parameters are:
	- url : The url for the external CSV file
	- file_name : The file name to use to save the CSV file locally

	>**Note:**
	>Give the CSV file a header (first row).   

1. **transform_n_load** to create a number of tables in the SQLite database based on the table structures you give it for transformation, then saves the content of the csv file to the tables you created. 
	```python
	transform_n_load(    
		local_dataset: str,
    	new_data_tables: dict,
    	new_lookup_tables: dict,
    	column_attributes: dict,
    	column_map: dict,)
	```
	The parameters are:
	- local_dataset : The local CSV file to load
	- new_data_tables : A dictionary of the tables non-lookup tables to be created. The key is the table name and the value is an array of columns.
	- new_lookup_tables : A dictionary of the tables lookup tables to be created. The key is the table name and the value is an array of columns.
	- column_attributes : A dictionary of the column attributes, eg. Integer, Primary Key. The key is the column name and the values are the attributes.
	- column_map : A dictionary maping the columns in the new tables defined above to the column indices in the CSV file. The key is the column.

	>**Note:**
	>The ID Primary Key of the table should always be the first column. 
	>Column names also shouldn't have spaces.


1. **read_data** to read data from the database based on the script parameters you give it.
	```python
	read_data(query: str, parameters: list, add_script=False)
	```
	The parameters are:
	- query : The script to execute.	
	- parameters : The parameters, if any, you set in the script to be used with ```string.format``` to fill.	
	- add_script : If it should return the script used in addition to the result in a tuple.

1. **save_data** to save records to a table you give it, following the table column structure.
	```python
	save_data(table_name: str, row: list)
	```
	The parameters are:
	- table_name : The name of the table in the database.
	- row : A list of the items to be saved. The order should follow the exact output of the ```get_table_columns``` function for that table.

1. **delete_data** to delete a record from the database given a record ID.
	```python
	delete_data(table_name: str, data_id: int)
	```
	The parameters are:
	- table_name : The name of the table in the database.	
	- data_id : The ID of the record to be deleted.	

1. **update_data** to update a record in the database using the table columns and a record ID.
	```python
	update_data(table_name: str, things_to_update: dict, data_id: int)
	```
	The parameters are:
	- table_name : The name of the table in the database.
	- things_to_update : A dictionary of the items to be updated. The key is the column name and the value is the new data. The column names use must be in the output of the  ```get_table_columns``` function for that table.
	- data_id : The ID of the record to be updated.	

1. **get_table_columns** to get the column names of a table. This is useful for saving and updating.
	```python
	get_table_columns(table_name: str)
	```
	The parameters are:
	- table_name : The name of the table.


### A query with join, aggregation and sorting ### 
Different Air Quality indicator readings in New York for 2021:<br />
```sql
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
```

And it generated this (column names renamed with the pandas 'rename' function):<br />
|    | Air Quality Indicator   |   No of Occurance |   Average |   Minimum |   Maximum |
|---:|:------------------------|------------------:|----------:|----------:|----------:|
|  1 | Fine particles (PM 2.5) |               423 |   7.48511 |       5.7 |      10.9 |
|  2 | Nitrogen dioxide (NO2)  |               423 |  16.9887  |       4.9 |      29.2 |
|  3 | Ozone (O3)              |               141 |  29.7369  |      26.9 |      34.9 |


[Please find more information generated by CI here](Query_results.md)   


## Explanation of what the queries in the Query_results.md file do ## 

**1\. Different Air Quality indicator readings in New York for 2021**
```sql
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
```

This SQL query retrieves statistical insights about air quality data from two tables, le88_tbl_air_quality and le88_tbl_indicator, by aggregating the data for each air quality indicator. Here’s the explanation for each part of the query:

- SELECT Clause:   
The _select_ clause specifies what information is being retrieved from the group of tables.   
  * indicator_name: The name of the air quality indicator from the *le88_tbl_indicator* table.   
  * COUNT(indicator_name) AS indicator_occurances: Counts the number of occurrences (or entries) of each indicator in the air quality dataset, using the alias *indicator_occurances* in the output (which was later renamed for better presentation).   
  * AVG(data_value) AS avg_air_quality: Calculates the average value of the air quality data (e.g., average pollutant concentration) for each indicator, using the alias *avg_air_quality* in the output (which was later renamed for better presentation).   
  * MIN(data_value) AS min_air_quality: Finds the minimum recorded value of the air quality data for each indicator, using the alias *min_air_quality* in the output (which was later renamed for better presentation).   
  * MAX(data_value) AS max_air_quality: Finds the maximum recorded value of the air quality data for each indicator, using the alias *max_air_quality* in the output (which was later renamed for better presentation).   

- FROM Clause:   
The _from_ clause specifies the reference table to which a join will be made. It's the _left_ table of a join.   
  * le88_tbl_air_quality: The main table that contains the air quality data, where *data_value* holds the actual measurements.   

- JOIN Clause:   
The _join_ clause joins the two tables based on the the condition provided in its _on_ statement. The table here becomes the _right_ table in the join.   
  * le88_tbl_indicator: The table that contains information about each air quality indicator, such as its name and ID.   
  * ON le88_tbl_indicator.indicator_id = le88_tbl_air_quality.fn_indicator_id: Joins the *le88_tbl_air_quality* and *le88_tbl_indicator* tables based on the condition that *indicator_id* column from *le88_tbl_indicator* and *fn_indicator_id* from *le88_tbl_air_quality* have equal values. This ensures that the air quality data is matched with its corresponding indicator name. *fn_indicator_id* is the foreign key of the indicator id in the *le88_tbl_indicator*, in the *le88_tbl_air_quality* table.  

- GROUP BY Clause:   
The _group by_ clause groups the records by the column(s) specified. Thus, repeating values in these columns will be aggregated based on the aggregate function used.   
  * GROUP BY indicator_name: Groups the results by the *indicator_name* column. This means that the calculations (such as COUNT, AVG, MIN, MAX) will be performed for each unique air quality indicator.   

- ORDER BY Clause:   
The _order by_ clause simply sorts the result (ascending or descending) using data in the column(s) specified.    
  * ORDER BY indicator_name: Sorts the final result set by indicator_name in ascending order.   

**Summary**   
The query is designed to:   
  * Group air quality data by each air quality indicator.   
  * For each indicator, it calculates the count of occurrences, average, minimum, and maximum air quality values.   
  * The results are then ordered by the indicator name.     
<br/>

**2\. Fine particles (PM 2.5) Air Quality in New York neighbourhoods for 2021**
```sql
SELECT  geo_place_name,
            COUNT(fn_indicator_id) AS fine_particles_pm_2_5_,
            CAST(AVG(data_value) as DECIMAL(10,2)) AS avg_air_quality,
            CAST(MIN(data_value) as DECIMAL(10,2)) AS min_air_quality,
            CAST(MAX(data_value) as DECIMAL(10,2)) AS max_air_quality
            FROM le88_tbl_air_quality
            JOIN le88_tbl_geo_data on 
            le88_tbl_geo_data.geo_id = le88_tbl_air_quality.fn_geo_id
            GROUP BY fn_indicator_id, geo_place_name
            HAVING fn_indicator_id = 365
            ORDER BY geo_place_name
```

This SQL query retrieves air quality statistics specifically related to fine particles (PM 2.5) for different geographical locations in New York for the year 2021. This is used in a loop to generate the same information for the different indicators. Here’s the explanation for each part of the query:   

- SELECT Clause:   
The _select_ clause specifies what information is being retrieved from the group of tables.   
  * geo_place_name: The name of the geographical location in New York.   
  * COUNT(fn_indicator_id) AS fine_particles_pm_2_5_: Counts the number of times where the air quality indicator is recorded for the particular geographical area. In this query, *fn_indicator_id* corresponds to the indicator id for the Fine particles (PM 2.5), as a foreign key in the *le88_tbl_air_quality* table. It uses the alias *fine_particles_pm_2_5_* in the output (which was later renamed for better presentation).   
  * CAST(AVG(data_value) AS DECIMAL(10,2)) AS avg_air_quality: Calculates the average air quality measurement for the Fine particles (PM 2.5) indicator for each geographical location, casting the result to a decimal with 2 decimal places. It uses the alias *avg_air_quality* in the output (which was later renamed for better presentation).    
  * CAST(MIN(data_value) AS DECIMAL(10,2)) AS min_air_quality: Finds the minimum recorded value of Fine particles PM 2.5 for each geographical location, casting it to 2 decimal places. It uses the alias *min_air_quality* in the output (which was later renamed for better presentation).  
  * CAST(MAX(data_value) AS DECIMAL(10,2)) AS max_air_quality: Finds the maximum recorded value of Fine particles PM 2.5 for each geographical location, also casts to 2 decimal places. It uses the alias *max_air_quality* in the output (which was later renamed for better presentation).  

- FROM Clause:   
The _from_ clause specifies the reference table to which a join will be made. It's the _left_ table of a join.   
  * le88_tbl_air_quality: The table containing air quality data where data_value holds the measurements (in this case, fine particles PM 2.5).   
  * le88_tbl_geo_data: A table containing geographical data such as *geo_place_name* and *geo_id*.   

- JOIN Clause:   
The _join_ clause joins the two tables based on the the condition provided in its _on_ statement. The table here becomes the _right_ table in the join.   
  * le88_tbl_geo_data ON le88_tbl_geo_data.geo_id = le88_tbl_air_quality.fn_geo_id: This joins the air quality data with geographical data. The *geo_id* from the *le88_tbl_geo_data* table is matched with the *fn_geo_id* in the *le88_tbl_air_quality* table, linking air quality measurements to specific locations.   

- GROUP BY Clause:   
The _group by_ clause groups the records by the columns specified. Thus, repeating values in these columns will be aggregated based on the aggregate function used.   
  * GROUP BY fn_indicator_id, geo_place_name: The results are grouped by the air quality indicator (fn_indicator_id) and the geographical location *geo_place_name*. This means that the COUNT, AVG, MIN, and MAX functions will be computed for each unique combination of indicator and location. In aggregation, all the selected columns should either be aggregated or be in the Group By clause. However, you can have columns in the Group By clause that are not selected. That's what I did for the *fn_indicator_id* column because I didn't want it or the actual indicator name to repeat. The whole result is for that indicator only.   

- HAVING Clause:   
The _having_ clause filters the result of the aggregate query based on the condition given to it. An easy way of looking at it is that it is the _Where_ clause in an aggregation query.   
  * HAVING fn_indicator_id = 365: This filters the results to include only the rows where fn_indicator_id equals 365, which corresponds to the specific air quality indicator for fine particulate matter PM 2.5.

- ORDER BY Clause:   
The _order by_ clause simply sorts the result (ascending or descending) using data in the column(s) specified.    
  * ORDER BY geo_place_name: The final result is sorted by the geographical location name in ascending order.   

**Summary:**   
  *	This query focuses on fine particulate matter (PM 2.5), indicated by fn_indicator_id = 365, across different geographical locations.   
  *	The same query is used to get information from the remaining indicators, all shown in the Query_result.md file.   
  *	For each location, it provides:   
    * The count of occurrences (number of PM 2.5 measurements) for that neighbourhood.   
    * The average, minimum, and maximum PM 2.5 levels.   
    * All numeric results for air quality measurements are cast to two decimal places for precision.   
   


## CLI Integration
The main.py script provides a CLI allowing the ETL and CRUD operations to be done from the command line.

At the cli prompt, type:
```
python main.py
```

and follow with the argument information below, leaving space between arguments.
```python
	extract:
   		url
        file_name

    transform_n_load:
        local_dataset
        new_data_tables, type=dictionary in a string format
        new_lookup_tables, type=dictionary in a string format
        column_attributes, type=dictionary in a string format
        column_map, type=dictionary in a string format

    read_data:
        table_name
        data_id, type=int

    save_data:
        table_name
        row, type=list in a string format

    update_data:
        table_name
        data_id, type=int
        things_to_update, type=dictionary in a string format

    delete_data:
        table_name
        data_id, type=int

    get_table_columns:
        table_name
```

> [!IMPORTANT]
> It's important to provide the arguments in the order and formats as desribed above for the CLI to work. You can find some samples in the Make file.

