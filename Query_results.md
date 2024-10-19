### Different Air Quality indicator readings in New York for 2021 ### 
The query executed was:<br />
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

And the result was (column names renamed with the pandas 'rename' function):<br />
|    | Air Quality Indicator   |   No of Occurances |   Average |   Minimum |   Maximum |
|---:|:------------------------|-------------------:|----------:|----------:|----------:|
|  1 | Fine particles (PM 2.5) |                423 |   7.48511 |       5.7 |      10.9 |
|  2 | Nitrogen dioxide (NO2)  |                423 |  16.9887  |       4.9 |      29.2 |
|  3 | Ozone (O3)              |                141 |  29.7369  |      26.9 |      34.9 |

<br /><br />

### Fine particles (PM 2.5) Air Quality in New York neighbourhoods for 2021 ### 
The query executed was:<br />
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

And the result was (column names renamed with the pandas 'rename' function):<br />
|    | Location Name                                  |   Fine particles (PM 2.5) Occurrances |   Average |   Minimum |   Maximum |
|---:|:-----------------------------------------------|--------------------------------------:|----------:|----------:|----------:|
|  1 | Bay Ridge and Dyker Heights (CD10)             |                                     6 |      7.87 |       6.5 |       9.6 |
|  2 | Bayside Little Neck-Fresh Meadows              |                                     3 |      6.93 |       6.3 |       7.9 |
|  3 | Bayside and Little Neck (CD11)                 |                                     3 |      6.97 |       6.3 |       7.9 |
|  4 | Bedford Stuyvesant - Crown Heights             |                                     9 |      7.42 |       6.6 |       8.7 |
|  5 | Bensonhurst (CD11)                             |                                     3 |      7.1  |       6.4 |       8.2 |
|  6 | Borough Park                                   |                                     9 |      7.34 |       6.4 |       8.8 |
|  7 | Borough Park (CD12)                            |                                     3 |      7.27 |       6.5 |       8.4 |
|  8 | Bronx                                          |                                     6 |      7.35 |       6.5 |       8.6 |
|  9 | Brooklyn                                       |                                     3 |      7.33 |       6.6 |       8.5 |
| 10 | Brownsville (CD16)                             |                                     3 |      7.2  |       6.5 |       8.3 |
| 11 | Bushwick (CD4)                                 |                                     9 |      7.51 |       6.8 |       8.8 |
| 12 | Central Harlem (CD10)                          |                                     3 |      7.6  |       6.8 |       8.8 |
| 13 | Central Harlem - Morningside Heights           |                                     9 |      7.67 |       6.8 |       9.1 |
| 14 | Chelsea - Clinton                              |                                     6 |      8.62 |       7.1 |      10.4 |
| 15 | Chelsea-Village                                |                                     3 |      9.33 |       8.4 |      10.4 |
| 16 | Coney Island (CD13)                            |                                     3 |      6.97 |       6.3 |       8   |
| 17 | Coney Island - Sheepshead Bay                  |                                     9 |      7.1  |       6.3 |       8.4 |
| 18 | Crown Heights and Prospect Heights (CD8)       |                                     6 |      8.3  |       6.7 |      10.2 |
| 19 | Downtown - Heights - Slope                     |                                     9 |      7.93 |       7.1 |       9.3 |
| 20 | East Flatbush (CD17)                           |                                     3 |      7.17 |       6.5 |       8.3 |
| 21 | East Flatbush - Flatbush                       |                                     9 |      7.28 |       6.4 |       8.7 |
| 22 | East Harlem                                    |                                     9 |      7.52 |       6.8 |       8.8 |
| 23 | East Harlem (CD11)                             |                                     3 |      7.5  |       6.8 |       8.7 |
| 24 | East New York                                  |                                     9 |      7.26 |       6.5 |       8.6 |
| 25 | Elmhurst and Corona (CD4)                      |                                     6 |      7.2  |       6.3 |       8.5 |
| 26 | Flatbush and Midwood (CD14)                    |                                     3 |      7.13 |       6.4 |       8.3 |
| 27 | Flatlands and Canarsie (CD18)                  |                                     3 |      6.87 |       6.2 |       8   |
| 28 | Flushing - Clearview                           |                                     9 |      7.26 |       6.5 |       8.5 |
| 29 | Fordham - Bronx Pk                             |                                     9 |      7.86 |       6.6 |       9.6 |
| 30 | Fresh Meadows                                  |                                     6 |      6.97 |       6.3 |       8.1 |
| 31 | Greenpoint                                     |                                     9 |      8.01 |       6.8 |       9.6 |
| 32 | Greenwich Village and Soho (CD2)               |                                     9 |      8.11 |       6.5 |      10.5 |
| 33 | High Bridge - Morrisania                       |                                     6 |      8.05 |       6.6 |       9.8 |
| 34 | Hunts Point - Mott Haven                       |                                     6 |      7.6  |       6.8 |       9   |
| 35 | Jamaica                                        |                                     9 |      6.97 |       6.3 |       8   |
| 36 | Jamaica and Hollis (CD12)                      |                                     3 |      6.93 |       6.3 |       7.9 |
| 37 | Kingsbridge - Riverdale                        |                                     9 |      7.84 |       6.6 |       9.7 |
| 38 | Long Island City - Astoria                     |                                     9 |      7.76 |       6.8 |       9.1 |
| 39 | Manhattan                                      |                                     3 |      8.23 |       7.4 |       9.4 |
| 40 | Midtown (CD5)                                  |                                     6 |      8.78 |       6.8 |      10.9 |
| 41 | Morningside Heights and Hamilton Heights (CD9) |                                     3 |      7.57 |       6.8 |       8.8 |
| 42 | Morris Park and Bronxdale (CD11)               |                                     9 |      7.79 |       6.6 |       9.2 |
| 43 | Northern SI                                    |                                     3 |      6.97 |       6.3 |       8.2 |
| 44 | Parkchester and Soundview (CD9)                |                                     9 |      7.27 |       6.4 |       8.6 |
| 45 | Pelham - Throgs Neck                           |                                     9 |      7.93 |       6.6 |      10   |
| 46 | Port Richmond                                  |                                     6 |      7.03 |       6.3 |       8.3 |
| 47 | Queens                                         |                                     3 |      7.1  |       6.5 |       8.1 |
| 48 | Queens Village (CD13)                          |                                     3 |      6.83 |       6.3 |       7.8 |
| 49 | Ridgewood and Maspeth (CD5)                    |                                     9 |      7.3  |       6.5 |       8.8 |
| 50 | Riverdale and Fieldston (CD8)                  |                                     9 |      7.09 |       6.3 |       8.7 |
| 51 | Rockaway and Broad Channel (CD14)              |                                     3 |      6.37 |       5.9 |       7.2 |
| 52 | Rockaways                                      |                                     9 |      6.5  |       5.9 |       7.8 |
| 53 | Sheepshead Bay (CD15)                          |                                     3 |      6.93 |       6.3 |       8   |
| 54 | South Beach - Tottenville                      |                                     3 |      6.47 |       5.8 |       7.6 |
| 55 | South Bronx                                    |                                     3 |      7.6  |       6.8 |       8.8 |
| 56 | South Crown Heights and Lefferts Gardens (CD9) |                                     6 |      7.95 |       6.5 |       9.8 |
| 57 | Southeast Queens                               |                                     9 |      6.89 |       6.2 |       8.1 |
| 58 | Southern SI                                    |                                     3 |      6.57 |       5.9 |       7.7 |
| 59 | Southwest Queens                               |                                     9 |      7.02 |       6.3 |       8.3 |
| 60 | Stapleton - St. George                         |                                     6 |      6.82 |       6.1 |       8.1 |
| 61 | Staten Island                                  |                                     3 |      6.73 |       6.1 |       7.9 |
| 62 | Sunset Park                                    |                                     9 |      7.7  |       6.8 |       9   |
| 63 | Sunset Park (CD7)                              |                                     6 |      8.4  |       7   |      10.1 |
| 64 | Union Square-Lower Manhattan                   |                                     3 |      8.57 |       7.7 |       9.7 |
| 65 | Upper East Side                                |                                     6 |      7.42 |       6.5 |       8.9 |
| 66 | Upper East Side (CD8)                          |                                     3 |      7.67 |       7   |       8.9 |
| 67 | Upper East Side-Gramercy                       |                                     3 |      8.3  |       7.6 |       9.4 |
| 68 | Washington Heights                             |                                     9 |      7.87 |       6.9 |       9.7 |
| 69 | Washington Heights and Inwood (CD12)           |                                     3 |      7.67 |       6.9 |       8.8 |
| 70 | West Queens                                    |                                     9 |      7.87 |       7.1 |       9.5 |
| 71 | Williamsbridge and Baychester (CD12)           |                                     3 |      7.47 |       6.5 |       8.6 |
| 72 | Willowbrook                                    |                                     6 |      6.6  |       5.7 |       8   |

<br /><br />

### Nitrogen dioxide (NO2) Air Quality in New York neighbourhoods for 2021 ### 
The query executed was:<br />
```sql
SELECT  geo_place_name,
            COUNT(fn_indicator_id) AS nitrogen_dioxide_no2_,
            CAST(AVG(data_value) as DECIMAL(10,2)) AS avg_air_quality,
            CAST(MIN(data_value) as DECIMAL(10,2)) AS min_air_quality,
            CAST(MAX(data_value) as DECIMAL(10,2)) AS max_air_quality
            FROM le88_tbl_air_quality
            JOIN le88_tbl_geo_data on 
            le88_tbl_geo_data.geo_id = le88_tbl_air_quality.fn_geo_id
            GROUP BY fn_indicator_id, geo_place_name
            HAVING fn_indicator_id = 375
            ORDER BY geo_place_name
```

And the result was (column names renamed with the pandas 'rename' function):<br />
|    | Location Name                                  |   Nitrogen dioxide (NO2) Occurrances |   Average |   Minimum |   Maximum |
|---:|:-----------------------------------------------|-------------------------------------:|----------:|----------:|----------:|
|  1 | Bay Ridge and Dyker Heights (CD10)             |                                    6 |     18.93 |      11.5 |      25.6 |
|  2 | Bayside Little Neck-Fresh Meadows              |                                    3 |     14.8  |      10.2 |      19.9 |
|  3 | Bayside and Little Neck (CD11)                 |                                    3 |     14.77 |      10.2 |      19.9 |
|  4 | Bedford Stuyvesant - Crown Heights             |                                    9 |     17.24 |      11.9 |      22.7 |
|  5 | Bensonhurst (CD11)                             |                                    3 |     15.83 |      10.9 |      20.2 |
|  6 | Borough Park                                   |                                    9 |     16.8  |      11.4 |      22.1 |
|  7 | Borough Park (CD12)                            |                                    3 |     16.57 |      11.6 |      21.2 |
|  8 | Bronx                                          |                                    6 |     16.33 |      11.1 |      21.8 |
|  9 | Brooklyn                                       |                                    3 |     16.47 |      11.5 |      21.2 |
| 10 | Brownsville (CD16)                             |                                    3 |     16.57 |      11.3 |      21.7 |
| 11 | Bushwick (CD4)                                 |                                    9 |     18.53 |      12.7 |      22.6 |
| 12 | Central Harlem (CD10)                          |                                    3 |     18.13 |      14.5 |      21.6 |
| 13 | Central Harlem - Morningside Heights           |                                    9 |     18.36 |      14.4 |      23.5 |
| 14 | Chelsea - Clinton                              |                                    6 |     21.07 |      14.4 |      26.8 |
| 15 | Chelsea-Village                                |                                    3 |     22.7  |      19.4 |      26.1 |
| 16 | Coney Island (CD13)                            |                                    3 |     13.63 |       8   |      18.8 |
| 17 | Coney Island - Sheepshead Bay                  |                                    9 |     14.78 |       8.5 |      21.4 |
| 18 | Crown Heights and Prospect Heights (CD8)       |                                    6 |     19.33 |      12.3 |      24.7 |
| 19 | Downtown - Heights - Slope                     |                                    9 |     19.27 |      14.6 |      24.5 |
| 20 | East Flatbush (CD17)                           |                                    3 |     16.2  |      10.9 |      21.2 |
| 21 | East Flatbush - Flatbush                       |                                    9 |     16.37 |      10.7 |      21.4 |
| 22 | East Harlem                                    |                                    9 |     18.01 |      13.1 |      22.3 |
| 23 | East Harlem (CD11)                             |                                    3 |     18.13 |      14.5 |      21.6 |
| 24 | East New York                                  |                                    9 |     16.79 |      10.8 |      22.3 |
| 25 | Elmhurst and Corona (CD4)                      |                                    6 |     16.05 |      10   |      22   |
| 26 | Flatbush and Midwood (CD14)                    |                                    3 |     15.77 |      10.5 |      20.6 |
| 27 | Flatlands and Canarsie (CD18)                  |                                    3 |     13.83 |       8.1 |      19.1 |
| 28 | Flushing - Clearview                           |                                    9 |     16.38 |      11.7 |      21.2 |
| 29 | Fordham - Bronx Pk                             |                                    9 |     17.3  |      12.1 |      22.6 |
| 30 | Fresh Meadows                                  |                                    6 |     15.52 |      10.5 |      20.8 |
| 31 | Greenpoint                                     |                                    9 |     20.06 |      15.3 |      23.7 |
| 32 | Greenwich Village and Soho (CD2)               |                                    9 |     18.09 |      12.4 |      24.4 |
| 33 | High Bridge - Morrisania                       |                                    6 |     20.13 |      14.2 |      25.4 |
| 34 | Hunts Point - Mott Haven                       |                                    6 |     19    |      15.1 |      23.4 |
| 35 | Jamaica                                        |                                    9 |     15.14 |      10.2 |      19.8 |
| 36 | Jamaica and Hollis (CD12)                      |                                    3 |     15.03 |      10.5 |      19.5 |
| 37 | Kingsbridge - Riverdale                        |                                    9 |     17.33 |      10.8 |      25.6 |
| 38 | Long Island City - Astoria                     |                                    9 |     18.57 |      13.4 |      22.9 |
| 39 | Manhattan                                      |                                    3 |     19.93 |      16.4 |      23.4 |
| 40 | Midtown (CD5)                                  |                                    6 |     21.72 |      13.8 |      29.2 |
| 41 | Morningside Heights and Hamilton Heights (CD9) |                                    3 |     17.83 |      14.2 |      21.3 |
| 42 | Morris Park and Bronxdale (CD11)               |                                    9 |     18.29 |      12.6 |      23.4 |
| 43 | Northern SI                                    |                                    3 |     14.57 |      10.4 |      18.5 |
| 44 | Parkchester and Soundview (CD9)                |                                    9 |     16.17 |      10.8 |      22.2 |
| 45 | Pelham - Throgs Neck                           |                                    9 |     18.58 |      12.3 |      25.5 |
| 46 | Port Richmond                                  |                                    6 |     15.18 |      11.2 |      18.7 |
| 47 | Queens                                         |                                    3 |     15.53 |      11   |      20.1 |
| 48 | Queens Village (CD13)                          |                                    3 |     14.6  |      10.4 |      18.8 |
| 49 | Ridgewood and Maspeth (CD5)                    |                                    9 |     16.54 |      11.3 |      21.8 |
| 50 | Riverdale and Fieldston (CD8)                  |                                    9 |     14.29 |       8.2 |      19.8 |
| 51 | Rockaway and Broad Channel (CD14)              |                                    3 |     10.63 |       4.9 |      15.7 |
| 52 | Rockaways                                      |                                    9 |     11.83 |       4.9 |      18.7 |
| 53 | Sheepshead Bay (CD15)                          |                                    3 |     14.23 |       8.7 |      19.1 |
| 54 | South Beach - Tottenville                      |                                    3 |     10.47 |       5.4 |      14.7 |
| 55 | South Bronx                                    |                                    3 |     18.5  |      14.5 |      22.9 |
| 56 | South Crown Heights and Lefferts Gardens (CD9) |                                    6 |     18    |      11.6 |      22.8 |
| 57 | Southeast Queens                               |                                    9 |     14.73 |       9.9 |      20.4 |
| 58 | Southern SI                                    |                                    3 |     11.37 |       6.6 |      15.5 |
| 59 | Southwest Queens                               |                                    9 |     15.21 |       9.8 |      20.9 |
| 60 | Stapleton - St. George                         |                                    6 |     13.42 |       8.1 |      18.6 |
| 61 | Staten Island                                  |                                    3 |     12.3  |       7.7 |      16.4 |
| 62 | Sunset Park                                    |                                    9 |     18.24 |      13.7 |      23.1 |
| 63 | Sunset Park (CD7)                              |                                    6 |     20.97 |      13.7 |      27.1 |
| 64 | Union Square-Lower Manhattan                   |                                    3 |     20.07 |      16.4 |      23.6 |
| 65 | Upper East Side                                |                                    6 |     17.93 |      10.4 |      23.3 |
| 66 | Upper East Side (CD8)                          |                                    3 |     20.2  |      16.8 |      23.4 |
| 67 | Upper East Side-Gramercy                       |                                    3 |     21.73 |      18.3 |      25.1 |
| 68 | Washington Heights                             |                                    9 |     18.34 |      13.2 |      24   |
| 69 | Washington Heights and Inwood (CD12)           |                                    3 |     17.07 |      13   |      21.3 |
| 70 | West Queens                                    |                                    9 |     19.23 |      14.7 |      24.1 |
| 71 | Williamsbridge and Baychester (CD12)           |                                    3 |     16.2  |      12   |      21   |
| 72 | Willowbrook                                    |                                    6 |     11.57 |       5.1 |      16.8 |

<br /><br />

### Ozone (O3) Air Quality in New York neighbourhoods for 2021 ### 
The query executed was:<br />
```sql
SELECT  geo_place_name,
            COUNT(fn_indicator_id) AS ozone_o3_,
            CAST(AVG(data_value) as DECIMAL(10,2)) AS avg_air_quality,
            CAST(MIN(data_value) as DECIMAL(10,2)) AS min_air_quality,
            CAST(MAX(data_value) as DECIMAL(10,2)) AS max_air_quality
            FROM le88_tbl_air_quality
            JOIN le88_tbl_geo_data on 
            le88_tbl_geo_data.geo_id = le88_tbl_air_quality.fn_geo_id
            GROUP BY fn_indicator_id, geo_place_name
            HAVING fn_indicator_id = 386
            ORDER BY geo_place_name
```

And the result was (column names renamed with the pandas 'rename' function):<br />
|    | Location Name                                  |   Ozone (O3) Occurrances |   Average |   Minimum |   Maximum |
|---:|:-----------------------------------------------|-------------------------:|----------:|----------:|----------:|
|  1 | Bay Ridge and Dyker Heights (CD10)             |                        2 |     28.85 |      28   |      29.7 |
|  2 | Bayside Little Neck-Fresh Meadows              |                        1 |     30.3  |      30.3 |      30.3 |
|  3 | Bayside and Little Neck (CD11)                 |                        1 |     30.3  |      30.3 |      30.3 |
|  4 | Bedford Stuyvesant - Crown Heights             |                        3 |     30    |      29.4 |      30.3 |
|  5 | Bensonhurst (CD11)                             |                        1 |     31.2  |      31.2 |      31.2 |
|  6 | Borough Park                                   |                        3 |     30.17 |      29.5 |      30.5 |
|  7 | Borough Park (CD12)                            |                        1 |     30.4  |      30.4 |      30.4 |
|  8 | Bronx                                          |                        2 |     30    |      29.8 |      30.2 |
|  9 | Brooklyn                                       |                        1 |     30.5  |      30.5 |      30.5 |
| 10 | Brownsville (CD16)                             |                        1 |     30.8  |      30.8 |      30.8 |
| 11 | Bushwick (CD4)                                 |                        3 |     28.67 |      27.8 |      30.4 |
| 12 | Central Harlem (CD10)                          |                        1 |     28.6  |      28.6 |      28.6 |
| 13 | Central Harlem - Morningside Heights           |                        3 |     28.53 |      28.5 |      28.6 |
| 14 | Chelsea - Clinton                              |                        2 |     28    |      27.1 |      28.9 |
| 15 | Chelsea-Village                                |                        1 |     27.4  |      27.4 |      27.4 |
| 16 | Coney Island (CD13)                            |                        1 |     32.4  |      32.4 |      32.4 |
| 17 | Coney Island - Sheepshead Bay                  |                        3 |     31.57 |      30.7 |      32   |
| 18 | Crown Heights and Prospect Heights (CD8)       |                        2 |     28.95 |      28   |      29.9 |
| 19 | Downtown - Heights - Slope                     |                        3 |     28.83 |      28.7 |      29.1 |
| 20 | East Flatbush (CD17)                           |                        1 |     31    |      31   |      31   |
| 21 | East Flatbush - Flatbush                       |                        3 |     30.53 |      29.8 |      30.9 |
| 22 | East Harlem                                    |                        3 |     28.8  |      28.4 |      29.6 |
| 23 | East Harlem (CD11)                             |                        1 |     28.3  |      28.3 |      28.3 |
| 24 | East New York                                  |                        3 |     30.37 |      28.9 |      31.1 |
| 25 | Elmhurst and Corona (CD4)                      |                        2 |     30.2  |      30.1 |      30.3 |
| 26 | Flatbush and Midwood (CD14)                    |                        1 |     30.4  |      30.4 |      30.4 |
| 27 | Flatlands and Canarsie (CD18)                  |                        1 |     32.2  |      32.2 |      32.2 |
| 28 | Flushing - Clearview                           |                        3 |     30.67 |      30.4 |      30.8 |
| 29 | Fordham - Bronx Pk                             |                        3 |     29.47 |      28.4 |      30   |
| 30 | Fresh Meadows                                  |                        2 |     30.35 |      30.2 |      30.5 |
| 31 | Greenpoint                                     |                        3 |     28.13 |      27.8 |      28.8 |
| 32 | Greenwich Village and Soho (CD2)               |                        3 |     29.57 |      27.9 |      30.4 |
| 33 | High Bridge - Morrisania                       |                        2 |     28.2  |      27.2 |      29.2 |
| 34 | Hunts Point - Mott Haven                       |                        2 |     28.65 |      27.8 |      29.5 |
| 35 | Jamaica                                        |                        3 |     30.77 |      30.3 |      31   |
| 36 | Jamaica and Hollis (CD12)                      |                        1 |     31.4  |      31.4 |      31.4 |
| 37 | Kingsbridge - Riverdale                        |                        3 |     28.67 |      28   |      29   |
| 38 | Long Island City - Astoria                     |                        3 |     29.6  |      29.2 |      30.4 |
| 39 | Manhattan                                      |                        1 |     27.9  |      27.9 |      27.9 |
| 40 | Midtown (CD5)                                  |                        2 |     27.95 |      26.9 |      29   |
| 41 | Morningside Heights and Hamilton Heights (CD9) |                        1 |     28.6  |      28.6 |      28.6 |
| 42 | Morris Park and Bronxdale (CD11)               |                        3 |     29.63 |      29.3 |      30.3 |
| 43 | Northern SI                                    |                        1 |     28.9  |      28.9 |      28.9 |
| 44 | Parkchester and Soundview (CD9)                |                        3 |     30.17 |      29.7 |      30.4 |
| 45 | Pelham - Throgs Neck                           |                        3 |     29.3  |      27.3 |      30.3 |
| 46 | Port Richmond                                  |                        2 |     28.6  |      28.6 |      28.6 |
| 47 | Queens                                         |                        1 |     30.9  |      30.9 |      30.9 |
| 48 | Queens Village (CD13)                          |                        1 |     31.3  |      31.3 |      31.3 |
| 49 | Ridgewood and Maspeth (CD5)                    |                        3 |     30.23 |      29.7 |      30.5 |
| 50 | Riverdale and Fieldston (CD8)                  |                        3 |     31.23 |      29.1 |      32.3 |
| 51 | Rockaway and Broad Channel (CD14)              |                        1 |     34.9  |      34.9 |      34.9 |
| 52 | Rockaways                                      |                        3 |     34    |      32.4 |      34.8 |
| 53 | Sheepshead Bay (CD15)                          |                        1 |     31.8  |      31.8 |      31.8 |
| 54 | South Beach - Tottenville                      |                        1 |     30.2  |      30.2 |      30.2 |
| 55 | South Bronx                                    |                        1 |     29.2  |      29.2 |      29.2 |
| 56 | South Crown Heights and Lefferts Gardens (CD9) |                        2 |     29.45 |      28.3 |      30.6 |
| 57 | Southeast Queens                               |                        3 |     31.37 |      31.1 |      31.5 |
| 58 | Southern SI                                    |                        1 |     29.8  |      29.8 |      29.8 |
| 59 | Southwest Queens                               |                        3 |     31.53 |      30.8 |      31.9 |
| 60 | Stapleton - St. George                         |                        2 |     29.25 |      29.1 |      29.4 |
| 61 | Staten Island                                  |                        1 |     29.5  |      29.5 |      29.5 |
| 62 | Sunset Park                                    |                        3 |     28.97 |      28.9 |      29   |
| 63 | Sunset Park (CD7)                              |                        2 |     27.9  |      26.9 |      28.9 |
| 64 | Union Square-Lower Manhattan                   |                        1 |     28.2  |      28.2 |      28.2 |
| 65 | Upper East Side                                |                        2 |     29.55 |      27.8 |      31.3 |
| 66 | Upper East Side (CD8)                          |                        1 |     27.8  |      27.8 |      27.8 |
| 67 | Upper East Side-Gramercy                       |                        1 |     27.4  |      27.4 |      27.4 |
| 68 | Washington Heights                             |                        3 |     27.87 |      27.8 |      27.9 |
| 69 | Washington Heights and Inwood (CD12)           |                        1 |     27.6  |      27.6 |      27.6 |
| 70 | West Queens                                    |                        3 |     28.8  |      28   |      29.2 |
| 71 | Williamsbridge and Baychester (CD12)           |                        1 |     30.3  |      30.3 |      30.3 |
| 72 | Willowbrook                                    |                        2 |     29.65 |      29.1 |      30.2 |

<br /><br />

