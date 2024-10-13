### The different Air Quality indicator readings in New York for 2022 ### 
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

And the result was:<br />
|    | Air Quality Indicator   |   No of Occurance |   Average |   Minimum |   Maximum |
|---:|:------------------------|------------------:|----------:|----------:|----------:|
|  1 | Fine particles (PM 2.5) |               121 |   6.74711 |       5.5 |       8.7 |
|  2 | Nitrogen dioxide (NO2)  |               127 |  11.7551  |       6.8 |      22.5 |
|  3 | Ozone (O3)              |               119 |  33.1664  |      27.7 |      37.7 |

<br /><br />

### The Fine particles (PM 2.5) Air Quality in New York neighbourhoods for 2021 ### 
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

And the result was:<br />
|    | Location Name                            |   Fine particles (PM 2.5) Occurrance |   Average |   Minimum |   Maximum |
|---:|:-----------------------------------------|-------------------------------------:|----------:|----------:|----------:|
|  1 | Bayside Little Neck-Fresh Meadows        |                                    1 |      6.3  |       6.3 |       6.3 |
|  2 | Bedford Stuyvesant (CD3)                 |                                    3 |      6.9  |       6.7 |       7   |
|  3 | Bedford Stuyvesant - Crown Heights       |                                    3 |      6.73 |       6.5 |       7.2 |
|  4 | Belmont and East Tremont (CD6)           |                                    3 |      6.53 |       6.2 |       7.2 |
|  5 | Bensonhurst (CD11)                       |                                    1 |      6    |       6   |       6   |
|  6 | Bensonhurst - Bay Ridge                  |                                    3 |      6.37 |       6   |       7.1 |
|  7 | Borough Park (CD12)                      |                                    1 |      6.2  |       6.2 |       6.2 |
|  8 | Brownsville (CD16)                       |                                    1 |      6.4  |       6.4 |       6.4 |
|  9 | Central Harlem (CD10)                    |                                    1 |      7.1  |       7.1 |       7.1 |
| 10 | Central Harlem - Morningside Heights     |                                    3 |      7.07 |       7   |       7.1 |
| 11 | Chelsea-Village                          |                                    1 |      8.2  |       8.2 |       8.2 |
| 12 | Coney Island (CD13)                      |                                    1 |      5.8  |       5.8 |       5.8 |
| 13 | Crown Heights and Prospect Heights (CD8) |                                    2 |      7.3  |       6.6 |       8   |
| 14 | Downtown - Heights - Slope               |                                    3 |      7.1  |       6.9 |       7.5 |
| 15 | East Flatbush (CD17)                     |                                    1 |      6.2  |       6.2 |       6.2 |
| 16 | East Flatbush - Flatbush                 |                                    2 |      6.7  |       6.2 |       7.2 |
| 17 | East Harlem (CD11)                       |                                    1 |      7.1  |       7.1 |       7.1 |
| 18 | East New York                            |                                    2 |      6.4  |       6.4 |       6.4 |
| 19 | Elmhurst and Corona (CD4)                |                                    1 |      6.8  |       6.8 |       6.8 |
| 20 | Flatbush and Midwood (CD14)              |                                    1 |      6.1  |       6.1 |       6.1 |
| 21 | Flatlands and Canarsie (CD18)            |                                    1 |      5.9  |       5.9 |       5.9 |
| 22 | Fordham - Bronx Pk                       |                                    3 |      7.2  |       7.1 |       7.4 |
| 23 | Fordham and University Heights (CD5)     |                                    3 |      6.83 |       6.7 |       7.1 |
| 24 | Fresh Meadows                            |                                    2 |      6.35 |       6.3 |       6.4 |
| 25 | Greenpoint                               |                                    3 |      7.2  |       7.2 |       7.2 |
| 26 | High Bridge - Morrisania                 |                                    1 |      7.1  |       7.1 |       7.1 |
| 27 | Jackson Heights (CD3)                    |                                    2 |      6.7  |       6.6 |       6.8 |
| 28 | Jamaica                                  |                                    3 |      6.3  |       6.3 |       6.3 |
| 29 | Jamaica and Hollis (CD12)                |                                    1 |      6.3  |       6.3 |       6.3 |
| 30 | Kew Gardens and Woodhaven (CD9)          |                                    3 |      6.2  |       6.1 |       6.4 |
| 31 | Kingsbridge - Riverdale                  |                                    3 |      7.2  |       7.1 |       7.4 |
| 32 | Long Island City - Astoria               |                                    3 |      7.13 |       7   |       7.2 |
| 33 | Lower Manhattan                          |                                    2 |      6.8  |       6.2 |       7.4 |
| 34 | Manhattan                                |                                    1 |      7.5  |       7.5 |       7.5 |
| 35 | Midtown (CD5)                            |                                    1 |      8.7  |       8.7 |       8.7 |
| 36 | New York City                            |                                    1 |      6.4  |       6.4 |       6.4 |
| 37 | Northeast Bronx                          |                                    3 |      7.5  |       7.1 |       8.3 |
| 38 | Northern SI                              |                                    1 |      6    |       6   |       6   |
| 39 | Park Slope and Carroll Gardens (CD6)     |                                    1 |      8.3  |       8.3 |       8.3 |
| 40 | Pelham - Throgs Neck                     |                                    2 |      7.5  |       7   |       8   |
| 41 | Port Richmond                            |                                    2 |      6.15 |       6.1 |       6.2 |
| 42 | Queens                                   |                                    1 |      6.4  |       6.4 |       6.4 |
| 43 | Queens Village (CD13)                    |                                    1 |      6.1  |       6.1 |       6.1 |
| 44 | Ridgewood - Forest Hills                 |                                    3 |      6.57 |       6.5 |       6.7 |
| 45 | Riverdale and Fieldston (CD8)            |                                    3 |      6.3  |       5.9 |       7.1 |
| 46 | Rockaway and Broad Channel (CD14)        |                                    1 |      5.5  |       5.5 |       5.5 |
| 47 | Rockaways                                |                                    3 |      5.67 |       5.5 |       6   |
| 48 | South Beach - Tottenville                |                                    1 |      5.6  |       5.6 |       5.6 |
| 49 | South Bronx                              |                                    1 |      7.2  |       7.2 |       7.2 |
| 50 | Southern SI                              |                                    1 |      5.7  |       5.7 |       5.7 |
| 51 | Southwest Queens                         |                                    3 |      6.37 |       6.2 |       6.7 |
| 52 | Stapleton - St. George                   |                                    1 |      5.9  |       5.9 |       5.9 |
| 53 | Sunset Park (CD7)                        |                                    1 |      8    |       8   |       8   |
| 54 | Throgs Neck and Co-op City (CD10)        |                                    2 |      6.35 |       5.8 |       6.9 |
| 55 | Tottenville and Great Kills (CD3)        |                                    2 |      5.75 |       5.6 |       5.9 |
| 56 | Union Square - Lower East Side           |                                    1 |      7.6  |       7.6 |       7.6 |
| 57 | Union Square-Lower Manhattan             |                                    1 |      7.5  |       7.5 |       7.5 |
| 58 | Upper East Side                          |                                    2 |      6.7  |       6.3 |       7.1 |
| 59 | Upper East Side (CD8)                    |                                    1 |      7.1  |       7.1 |       7.1 |
| 60 | Upper East Side-Gramercy                 |                                    1 |      7.5  |       7.5 |       7.5 |
| 61 | Upper West Side                          |                                    2 |      6.9  |       6.8 |       7   |
| 62 | Upper West Side (CD7)                    |                                    2 |      7.1  |       7   |       7.2 |
| 63 | Washington Heights                       |                                    3 |      7.2  |       7.2 |       7.2 |
| 64 | Washington Heights and Inwood (CD12)     |                                    1 |      7.2  |       7.2 |       7.2 |
| 65 | West Queens                              |                                    3 |      7    |       6.9 |       7.2 |
| 66 | Williamsbridge and Baychester (CD12)     |                                    1 |      7.1  |       7.1 |       7.1 |
| 67 | Williamsburg - Bushwick                  |                                    2 |      7.05 |       7   |       7.1 |

<br /><br />

### The Ozone (O3) Air Quality in New York neighbourhoods for 2021 ### 
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

And the result was:<br />
|    | Location Name                                  |   Ozone (O3) Occurrance |   Average |   Minimum |   Maximum |
|---:|:-----------------------------------------------|------------------------:|----------:|----------:|----------:|
|  1 | Bayside Little Neck-Fresh Meadows              |                       1 |     33.7  |      33.7 |      33.7 |
|  2 | Bayside and Little Neck (CD11)                 |                       1 |     33.7  |      33.7 |      33.7 |
|  3 | Bedford Stuyvesant (CD3)                       |                       2 |     32.4  |      31.6 |      33.2 |
|  4 | Bedford Stuyvesant - Crown Heights             |                       1 |     33.7  |      33.7 |      33.7 |
|  5 | Belmont and East Tremont (CD6)                 |                       2 |     33.55 |      31.9 |      35.2 |
|  6 | Bensonhurst (CD11)                             |                       1 |     36.5  |      36.5 |      36.5 |
|  7 | Bensonhurst - Bay Ridge                        |                       3 |     34.83 |      32.9 |      35.8 |
|  8 | Borough Park (CD12)                            |                       1 |     35.1  |      35.1 |      35.1 |
|  9 | Brownsville (CD16)                             |                       1 |     34.2  |      34.2 |      34.2 |
| 10 | Central Harlem (CD10)                          |                       1 |     31.2  |      31.2 |      31.2 |
| 11 | Central Harlem - Morningside Heights           |                       3 |     31.13 |      30.9 |      31.6 |
| 12 | Coney Island (CD13)                            |                       1 |     37.7  |      37.7 |      37.7 |
| 13 | Crown Heights and Prospect Heights (CD8)       |                       2 |     31.85 |      30.3 |      33.4 |
| 14 | Downtown - Heights - Slope                     |                       3 |     32.47 |      32.3 |      32.8 |
| 15 | East Flatbush - Flatbush                       |                       3 |     33.77 |      31.5 |      34.9 |
| 16 | East Harlem (CD11)                             |                       1 |     31.5  |      31.5 |      31.5 |
| 17 | East New York                                  |                       2 |     32.85 |      31.3 |      34.4 |
| 18 | Elmhurst and Corona (CD4)                      |                       2 |     33.75 |      33.4 |      34.1 |
| 19 | Fordham - Bronx Pk                             |                       2 |     31.55 |      31.4 |      31.7 |
| 20 | Fordham and University Heights (CD5)           |                       3 |     32.87 |      31.2 |      33.7 |
| 21 | Fresh Meadows                                  |                       2 |     34.05 |      33.9 |      34.2 |
| 22 | Greenpoint                                     |                       3 |     32.23 |      31.9 |      32.4 |
| 23 | High Bridge - Morrisania                       |                       2 |     30.6  |      29.7 |      31.5 |
| 24 | Jackson Heights (CD3)                          |                       2 |     34.35 |      34.2 |      34.5 |
| 25 | Jamaica                                        |                       3 |     34.23 |      33.9 |      34.4 |
| 26 | Jamaica and Hollis (CD12)                      |                       1 |     34.6  |      34.6 |      34.6 |
| 27 | Kew Gardens and Woodhaven (CD9)                |                       3 |     34.63 |      34.5 |      34.7 |
| 28 | Kingsbridge - Riverdale                        |                       3 |     30.1  |      30   |      30.3 |
| 29 | Long Island City - Astoria                     |                       3 |     33.13 |      32.9 |      33.6 |
| 30 | Lower Manhattan                                |                       2 |     32.55 |      30.3 |      34.8 |
| 31 | Manhattan                                      |                       1 |     30.2  |      30.2 |      30.2 |
| 32 | Midtown (CD5)                                  |                       1 |     27.7  |      27.7 |      27.7 |
| 33 | Morningside Heights and Hamilton Heights (CD9) |                       1 |     30.6  |      30.6 |      30.6 |
| 34 | New York City                                  |                       2 |     33.15 |      32.2 |      34.1 |
| 35 | Northeast Bronx                                |                       3 |     31.53 |      30.2 |      32.2 |
| 36 | Northern SI                                    |                       1 |     34.6  |      34.6 |      34.6 |
| 37 | Park Slope and Carroll Gardens (CD6)           |                       2 |     30.85 |      28.8 |      32.9 |
| 38 | Pelham - Throgs Neck                           |                       3 |     32.03 |      29.5 |      33.3 |
| 39 | Port Richmond                                  |                       2 |     34.2  |      34.2 |      34.2 |
| 40 | Queens Village (CD13)                          |                       1 |     34.7  |      34.7 |      34.7 |
| 41 | Ridgewood - Forest Hills                       |                       3 |     34.13 |      34   |      34.2 |
| 42 | Riverdale and Fieldston (CD8)                  |                       2 |     33.15 |      30.2 |      36.1 |
| 43 | Rockaway and Broad Channel (CD14)              |                       1 |     37.6  |      37.6 |      37.6 |
| 44 | Rockaways                                      |                       3 |     36.83 |      35.5 |      37.5 |
| 45 | Sheepshead Bay (CD15)                          |                       1 |     36.8  |      36.8 |      36.8 |
| 46 | South Beach - Tottenville                      |                       1 |     36    |      36   |      36   |
| 47 | Southern SI                                    |                       1 |     35.6  |      35.6 |      35.6 |
| 48 | Southwest Queens                               |                       3 |     34.93 |      34.4 |      35.2 |
| 49 | Stapleton - St. George                         |                       2 |     35    |      34.8 |      35.2 |
| 50 | Staten Island                                  |                       1 |     35.3  |      35.3 |      35.3 |
| 51 | Sunset Park (CD7)                              |                       2 |     31.2  |      28.9 |      33.5 |
| 52 | Throgs Neck and Co-op City (CD10)              |                       3 |     35.93 |      33.6 |      37.1 |
| 53 | Tottenville and Great Kills (CD3)              |                       1 |     34.8  |      34.8 |      34.8 |
| 54 | Union Square - Lower East Side                 |                       2 |     32.8  |      31.2 |      34.4 |
| 55 | Upper East Side                                |                       1 |     34.6  |      34.6 |      34.6 |
| 56 | Upper East Side (CD8)                          |                       1 |     30.7  |      30.7 |      30.7 |
| 57 | Upper West Side                                |                       1 |     29.9  |      29.9 |      29.9 |
| 58 | Upper West Side (CD7)                          |                       2 |     31.4  |      29.9 |      32.9 |
| 59 | Washington Heights                             |                       3 |     30.77 |      29.9 |      32.5 |
| 60 | Washington Heights and Inwood (CD12)           |                       1 |     29.6  |      29.6 |      29.6 |
| 61 | West Queens                                    |                       3 |     33.33 |      32.8 |      33.6 |
| 62 | Williamsbridge and Baychester (CD12)           |                       1 |     31.8  |      31.8 |      31.8 |
| 63 | Williamsburg - Bushwick                        |                       3 |     33.07 |      32.8 |      33.2 |

<br /><br />

### The Nitrogen dioxide (NO2) Air Quality in New York neighbourhoods for 2021 ### 
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

And the result was:<br />
|    | Location Name                                  |   Nitrogen dioxide (NO2) Occurrance |   Average |   Minimum |   Maximum |
|---:|:-----------------------------------------------|------------------------------------:|----------:|----------:|----------:|
|  1 | Bayside Little Neck-Fresh Meadows              |                                   1 |     10.7  |      10.7 |      10.7 |
|  2 | Bayside and Little Neck (CD11)                 |                                   1 |     10.7  |      10.7 |      10.7 |
|  3 | Bedford Stuyvesant (CD3)                       |                                   3 |     12.63 |      11.9 |      13   |
|  4 | Bedford Stuyvesant - Crown Heights             |                                   2 |     12.25 |      11.4 |      13.1 |
|  5 | Belmont and East Tremont (CD6)                 |                                   3 |     11.07 |      10.1 |      13   |
|  6 | Bensonhurst (CD11)                             |                                   1 |      9.4  |       9.4 |       9.4 |
|  7 | Bensonhurst - Bay Ridge                        |                                   3 |     10.67 |       9.8 |      12.4 |
|  8 | Borough Park (CD12)                            |                                   1 |     10.3  |      10.3 |      10.3 |
|  9 | Brooklyn                                       |                                   1 |     10.7  |      10.7 |      10.7 |
| 10 | Brownsville (CD16)                             |                                   1 |     11.2  |      11.2 |      11.2 |
| 11 | Central Harlem (CD10)                          |                                   1 |     13.1  |      13.1 |      13.1 |
| 12 | Central Harlem - Morningside Heights           |                                   3 |     13.53 |      13.2 |      14.2 |
| 13 | Chelsea-Village                                |                                   1 |     18.5  |      18.5 |      18.5 |
| 14 | Coney Island (CD13)                            |                                   1 |      8.2  |       8.2 |       8.2 |
| 15 | Crown Heights and Prospect Heights (CD8)       |                                   2 |     14.2  |      11.8 |      16.6 |
| 16 | Downtown - Heights - Slope                     |                                   3 |     13.67 |      13.4 |      14.2 |
| 17 | East Flatbush (CD17)                           |                                   1 |     10.5  |      10.5 |      10.5 |
| 18 | East Flatbush - Flatbush                       |                                   3 |     10.83 |      10.2 |      12.1 |
| 19 | East Harlem (CD11)                             |                                   1 |     13    |      13   |      13   |
| 20 | East New York                                  |                                   3 |     11.83 |      10.9 |      13.7 |
| 21 | Elmhurst and Corona (CD4)                      |                                   2 |     11.45 |      10.7 |      12.2 |
| 22 | Flatbush and Midwood (CD14)                    |                                   1 |      9.8  |       9.8 |       9.8 |
| 23 | Flatlands and Canarsie (CD18)                  |                                   1 |      8.5  |       8.5 |       8.5 |
| 24 | Fordham - Bronx Pk                             |                                   3 |     12.2  |      11.5 |      13.6 |
| 25 | Fordham and University Heights (CD5)           |                                   3 |     12.9  |      12.5 |      13.7 |
| 26 | Fresh Meadows                                  |                                   1 |     10.6  |      10.6 |      10.6 |
| 27 | Greenpoint                                     |                                   3 |     14.07 |      14   |      14.1 |
| 28 | High Bridge - Morrisania                       |                                   1 |     13.6  |      13.6 |      13.6 |
| 29 | Jackson Heights (CD3)                          |                                   3 |     11.17 |      11   |      11.5 |
| 30 | Jamaica                                        |                                   3 |     10.5  |      10.5 |      10.5 |
| 31 | Jamaica and Hollis (CD12)                      |                                   1 |     10.3  |      10.3 |      10.3 |
| 32 | Kew Gardens and Woodhaven (CD9)                |                                   3 |     10.07 |       9.8 |      10.6 |
| 33 | Kingsbridge - Riverdale                        |                                   3 |     12.7  |      10.6 |      16.9 |
| 34 | Long Island City - Astoria                     |                                   3 |     12.8  |      12   |      13.2 |
| 35 | Lower Manhattan                                |                                   2 |     13.65 |      10.6 |      16.7 |
| 36 | Midtown (CD5)                                  |                                   2 |     18.05 |      13.6 |      22.5 |
| 37 | Morningside Heights and Hamilton Heights (CD9) |                                   1 |     13.3  |      13.3 |      13.3 |
| 38 | New York City                                  |                                   2 |     11.4  |      10.6 |      12.2 |
| 39 | Northeast Bronx                                |                                   2 |     14    |      11.6 |      16.4 |
| 40 | Northern SI                                    |                                   1 |      8.9  |       8.9 |       8.9 |
| 41 | Park Slope and Carroll Gardens (CD6)           |                                   1 |     19.5  |      19.5 |      19.5 |
| 42 | Pelham - Throgs Neck                           |                                   3 |     13.93 |      12   |      17.8 |
| 43 | Port Richmond                                  |                                   2 |      9.35 |       9.3 |       9.4 |
| 44 | Queens                                         |                                   1 |     10.6  |      10.6 |      10.6 |
| 45 | Queens Village (CD13)                          |                                   1 |     10    |      10   |      10   |
| 46 | Ridgewood - Forest Hills                       |                                   2 |     10.9  |      10.6 |      11.2 |
| 47 | Riverdale and Fieldston (CD8)                  |                                   3 |      9.27 |       8.6 |      10.6 |
| 48 | Rockaway and Broad Channel (CD14)              |                                   1 |      6.9  |       6.9 |       6.9 |
| 49 | Rockaways                                      |                                   3 |      7.73 |       7   |       9.2 |
| 50 | Sheepshead Bay (CD15)                          |                                   1 |      8.5  |       8.5 |       8.5 |
| 51 | South Beach - Tottenville                      |                                   1 |      6.9  |       6.9 |       6.9 |
| 52 | South Bronx                                    |                                   1 |     13.5  |      13.5 |      13.5 |
| 53 | Southern SI                                    |                                   1 |      7.4  |       7.4 |       7.4 |
| 54 | Southwest Queens                               |                                   2 |      9.7  |       9.7 |       9.7 |
| 55 | Stapleton - St. George                         |                                   2 |      8.35 |       8   |       8.7 |
| 56 | Staten Island                                  |                                   1 |      7.8  |       7.8 |       7.8 |
| 57 | Sunset Park (CD7)                              |                                   2 |     16.1  |      12.6 |      19.6 |
| 58 | Throgs Neck and Co-op City (CD10)              |                                   3 |      9.57 |       8.5 |      11.7 |
| 59 | Tottenville and Great Kills (CD3)              |                                   2 |      7.55 |       6.8 |       8.3 |
| 60 | Union Square - Lower East Side                 |                                   1 |     10.6  |      10.6 |      10.6 |
| 61 | Upper East Side                                |                                   1 |     10.7  |      10.7 |      10.7 |
| 62 | Upper East Side (CD8)                          |                                   1 |     15.3  |      15.3 |      15.3 |
| 63 | Upper West Side                                |                                   3 |     13.73 |      11.8 |      14.7 |
| 64 | Upper West Side (CD7)                          |                                   2 |     14.05 |      13.4 |      14.7 |
| 65 | Washington Heights                             |                                   3 |     13.7  |      13.5 |      14.1 |
| 66 | Washington Heights and Inwood (CD12)           |                                   1 |     13.6  |      13.6 |      13.6 |
| 67 | West Queens                                    |                                   2 |     13.5  |      12.8 |      14.2 |
| 68 | Williamsbridge and Baychester (CD12)           |                                   1 |     11.4  |      11.4 |      11.4 |
| 69 | Williamsburg - Bushwick                        |                                   2 |     12.1  |      11.5 |      12.7 |

<br /><br />

