from app import client
import json
from starlette.testclient import TestClient
from src.constants import Constants
import base64
from requests.auth import HTTPBasicAuth
from pydantic_model import InputData
import pytest
from src.postresql import Postgres
import pandas as pd

auth = HTTPBasicAuth(username="icgencel", password="icgencel123")
client = TestClient(client)

db = Postgres()

def test_create_table_n_get_data():
    db.create_table(Constants.test_table_yaml_path)
    db.run_query("insert into dummy values ('1','2')")
    df = db.get_data("select * from dummy")
    assert ((df['dummydata'].values[0])=='1') and ((df['dummydata2'].values[0])=='2')
    db.run_query("drop table dummy")

def test_load_data():
    data = pd.DataFrame([['1','2'],['3','4']], columns=['dummydata','dummydata2'])
    db.load_data("dummy", data)
    df = db.get_data("select * from dummy")
    assert ((df['dummydata'].values[0])=='1') and ((df['dummydata2'].values[0])=='2') \
              and ((df['dummydata'].values[1])=='3') and ((df['dummydata2'].values[1])=='4')   
    db.run_query("drop table dummy")

def test_insert_prediction():
    dummy_prediction = pd.DataFrame([[1,1,0],[2,1,1]], columns=['customer_id','label', 'prediction'])
    db.insert_prediction('dummy_prediction_table', dummy_prediction)
    df = db.get_data("select * from dummy_prediction_table")
    assert ((df['customer_id'].values[0])==1) and ((df['label'].values[0])==1) \
                and ((df['prediction'].values[0])==0) and ((df['customer_id'].values[1])==2) \
                and ((df['label'].values[1])==1) and ((df['prediction'].values[1])==1)
    db.run_query("drop table dummy_prediction_table")


def test_api():
    response = client.post('/prediction', json=Constants.payload, auth=auth)
    db.run_query('DELETE FROM car_load_prediction_api WHERE id=(select max(id) from car_load_prediction_api)')
    assert response.status_code == 200

def test_user_auth():
    response = client.post('/prediction', json=Constants.payload)
    response2 = client.post('/prediction', json=Constants.payload, auth=auth)
    db.run_query('DELETE FROM car_load_prediction_api WHERE id=(select max(id) from car_load_prediction_api)')
    assert response.status_code == 401 and response2.status_code == 200