# Python Assignment
 Preconditions:
* Python 3
* Docker

Firstly create a environment in assignment_I_&_II directory and activate it. Then install dependencies.

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```


Open Docker and run docker-compose

```
docker-compose up -d
```

Then run main.py in order to create Postgres tables, train and create pickle model files.
```
python3 main.py
```

In order to run test.
```
pytest test_api.py
```

Run server with uvicorn
```
uvicorn app:client --reload
```

> API can be used with POST requests. http://127.0.0.1:8000/prediction

> Example body of API:
```json
{
    "customer_id": 2,
    "main_account_loan_no": 1, 
    "main_account_active_loan_no" : 1,
    "main_account_overdue_no" : 1,
    "main_account_outstanding_loan" : 1,
    "main_account_sanction_loan" : 1,
    "main_account_disbursed_loan" : 1,
    "sub_account_loan_no" : 1,
    "sub_account_active_loan_no" : 1,
    "sub_account_overdue_no" : 1,
    "sub_account_outstanding_loan" : 1,
    "sub_account_sanction_loan" : 1,
    "sub_account_disbursed_loan" : 1,
    "disbursed_amount" : 1,
    "asset_cost" : 1,
    "branch_id" : 1,
    "supplier_id" : 1,
    "manufacturer_id" : 1,
    "area_id" : 1,
    "employee_code_id" : 1,
    "mobileno_flag" : 1,
    "idcard_flag" : 1,
    "Driving_flag" : 1, 
    "passport_flag" : 1, 
    "credit_score" : 1, 
    "main_account_monthly_payment" : 1,
    "sub_account_monthly_payment" : 1, 
    "last_six_month_new_loan_no" : 1, 
    "last_six_month_defaulted_no" : 1, 
    "average_age" : 1,
    "credit_history" : 1, 
    "enquirie_no" : 1,
    "loan_to_asset_ratio" : "1.0",
    "total_account_loan_no" : 1, 
    "sub_account_inactive_loan_no" : 1,
    "total_inactive_loan_no" : 1,
    "main_account_inactive_loan_no" : 1,
    "total_overdue_no" : 1,
    "total_outstanding_loan" : 1,
    "total_sanction_loan": 1,
    "total_disbursed_loan": 1,
    "total_monthly_payment": 1,
    "outstanding_disburse_ratio": "1.0",
    "main_account_tenure": 1,
    "sub_account_tenure": 1, 
    "disburse_to_sactioned_ratio": "1.0",
    "active_to_inactive_act_ratio": "1.0", 	
    "year_of_birth": 1,
    "disbursed_date": 1,
    "Credit_level": 1,
    "employment_type":	1,
    "age":	1
}
```