install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

test:
	python -m pytest -cov=main test_main.py

extract:
	python main.py extract "https://data.cityofnewyork.us/resource/c3uy-2p5r.csv?%24limit=10000" "air_quality.csv" '("time_period", "2021")' "unique_id"

transform_and_load:
	python main.py transform_n_load "air_quality.csv" '{"air_quality":["air_quality_id","fn_indicator_id","fn_geo_id","time_period","start_date","data_value"]}' '{"indicator":["indicator_id","indicator_name","measure","measure_info"],"geo_data":["geo_id","geo_place_name","geo_type_name"]}' '{"air_quality_id":"INTEGER PRIMARY KEY","indicator_id":"INTEGER PRIMARY KEY","indicator_name":"STRING","measure":"STRING","measure_info":"STRING","geo_type_name":"STRING","geo_id":"INTEGER PRIMARY KEY","geo_place_name":"STRING","time_period":"STRING","start_date":"STRING","data_value":"REAL","fn_indicator_id":"INTEGER","fn_geo_id":"INTEGER"}' '{"air_quality_id":0,"indicator_id":1,"indicator_name":2,"measure":3,"measure_info":4,"geo_type_name":5,"geo_id":6,"geo_place_name":7,"time_period":8,"start_date":9,"data_value":10,"fn_geo_id":6,"fn_indicator_id":1}'

query:
	python main.py read_data "select * from {0} where {1} = {2}" '["le88_tbl_air_quality", "air_quality_id", 823470]'

generate_and_push:
	# Create the markdown file
	python query.py

	# Add, commit, and push the generated files to GitHub
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add .; \
	git commit -m "Add generated plots and markdown"; \
	git push; \

all: install format lint test extract transform_and_load query generate_and_push