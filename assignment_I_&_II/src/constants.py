class Constants:
    table_name = "car_load"
    prediction_table = "car_load_prediction"
    tables_yaml_path = "tables.yaml"
    test_table_yaml_path = "test.yaml"
    csv_urlpath = "https://october-data-exercises.s3.eu-west-1.amazonaws.com/datasets/car_loan_trainset.csv"
    csv_localpath = "data.csv"
    model_name = "classifier.pkl"
    scalar_name = "scalar.pkl"
    dropped_columns = [
            'branch_id',
            'supplier_id',
            'manufacturer_id',
            'year_of_birth',
            'disbursed_date',
            'area_id',
            'employee_code_id',
            'mobileno_flag',
            'idcard_flag',
            'Driving_flag',
            'passport_flag'
        ]
    payload = ({
        "customer_id": 1,
        "main_account_loan_no": 1,
        "main_account_active_loan_no": 1,
        "main_account_overdue_no": 1,
        "main_account_outstanding_loan": 1,
        "main_account_sanction_loan": 1,
        "main_account_disbursed_loan": 1,
        "sub_account_loan_no": 1,
        "sub_account_active_loan_no": 1,
        "sub_account_overdue_no": 1,
        "sub_account_outstanding_loan": 1,
        "sub_account_sanction_loan": 1,
        "sub_account_disbursed_loan": 1,
        "disbursed_amount": 1,
        "asset_cost": 1,
        "branch_id": 1,
        "supplier_id": 1,
        "manufacturer_id": 1,
        "area_id": 1,
        "employee_code_id": 1,
        "mobileno_flag": 1,
        "idcard_flag": 1,
        "Driving_flag": 1,
        "passport_flag": 1,
        "credit_score": 1,
        "main_account_monthly_payment": 1,
        "sub_account_monthly_payment": 1,
        "last_six_month_new_loan_no": 1,
        "last_six_month_defaulted_no": 1,
        "average_age": 1,
        "credit_history": 1,
        "enquirie_no": 1,
        "loan_to_asset_ratio": "1.0",
        "total_account_loan_no": 1,
        "sub_account_inactive_loan_no": 1,
        "total_inactive_loan_no": 1,
        "main_account_inactive_loan_no": 1,
        "total_overdue_no": 1,
        "total_outstanding_loan": 1,
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
        "employment_type": 1,
        "age": 1
    })