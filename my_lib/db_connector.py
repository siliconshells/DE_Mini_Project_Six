from databricks import sql
import os
from dotenv import load_dotenv


def connect_to_databricks():
    load_dotenv()
    connection = sql.connect(
        server_hostname=os.getenv("databricks_server_host"),
        http_path=os.getenv("databricks_sql_http"),
        access_token=os.getenv("databricks_api_key"),
    )
    return connection


def close_databricks_connection(cursor):
    connection = cursor.connection
    cursor.close()
    connection.close()
