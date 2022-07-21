from src.config import PostgresConfig
import urllib.request
import os
import pandas as pd
from sqlalchemy import create_engine
from src.constants import Constants
import yaml

class Postgres:
    def __init__(self):
        self._conn = create_engine(f'postgresql://{PostgresConfig.username}:{PostgresConfig.password}@{PostgresConfig.host}:{PostgresConfig.port}/{PostgresConfig.database}').connect()

    @staticmethod
    def create_table_query(table_path):
        tables = yaml.safe_load(open(table_path, "r"))["tables"]
        for table in tables:
            column_ddl = ",".join([" ".join(list(column.values())) for column in table["columns"]])
            yield f"""create table if not exists {table["schema"]}.{table["name"]} ({column_ddl})"""


    def create_table(self, table_path):
        try:
            for query in Postgres.create_table_query(table_path):
                self._conn.execute(query)
                print("Tables are created!")

            # Insert dump data to credentials table
            self._conn.execute(f"INSERT INTO credentials (username, password) VALUES ('icgencel', 'icgencel123')")
        except:
            raise Exception("Cannot create tables!")


    def load_data(self, table_name, data):
        data.to_sql(f'{table_name}', self._conn, if_exists='replace', index=False)
        # Next(f) skips the first line - because it is header

    def get_data(self, query):
        df = pd.read_sql(f'{query}', self._conn)
        return df

    def run_query(self, query):
        self._conn.execute(query)

    def insert_prediction(self, prediction_table, predictions):
        predictions.to_sql(f'{prediction_table}', self._conn, if_exists='replace', index=False)
        print(f"Prediction inserted to {prediction_table}!")


    def insert_api_prediction(self, prediction_table, prediction):
        prediction.to_sql(f'{prediction_table}', self._conn, if_exists='append', index=False)