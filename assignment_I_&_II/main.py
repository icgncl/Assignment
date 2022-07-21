from src.postresql import Postgres
from src.model import Model
from src.constants import Constants
from src.utils import Utils


def main():

    # It downloads csv files from the url if they are not exist
    data = Utils.download_csv_from_url(Constants.csv_localpath, Constants.csv_urlpath)

    db = Postgres()

    # It creates the tables if they are not exist
    db.create_table(Constants.tables_yaml_path)

    # It loads csv data to the database
    db.load_data(Constants.table_name, data)

    # Getting data from postgres
    df = db.get_data(f"SELECT * FROM {Constants.table_name}")

    # It checks missing and inf values in the data
    df = Utils.check_n_clear_data(df)
    
    # It trains the model and saves it as a pickle file
    Model.train_model(df, Constants.model_name, Constants.scalar_name)

    # It predicts the data
    predictions = Model.make_prediction(df, Constants.model_name, Constants.scalar_name)
    
    # It inserts the predictions to the database
    db.insert_prediction(Constants.prediction_table, predictions)




if __name__ == '__main__':
    main()