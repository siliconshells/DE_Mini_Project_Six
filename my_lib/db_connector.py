from databricks import sql
import os
from dotenv import load_dotenv


def connect_to_databricks():
    load_dotenv()
    connection = sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOST"),
        http_path=os.getenv("DATABRICKS_SQL_HTTP"),
        access_token=os.getenv("DATABRICKS_API_KEY"),
    )
    return connection


def close_databricks_connection(cursor):
    connection = cursor.connection
    cursor.close()
    connection.close()
