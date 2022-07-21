from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from fastapi.encoders import jsonable_encoder
from src.constants import Constants


class Model:

    # TODO : Improve this ML model
    # As indicated in the documentation, I have not spend much time for the model.
    # Hyperparameter tuning can be done in order to make this model better.
    # Also, most of the columns are used. With examining the data, the most valuable data can be used for training purpose. 

    @staticmethod
    def train_model(data, model_name, scalar_name):
        # Unnecessary columns for training is dropped
        data.drop(columns=Constants.dropped_columns,axis=1, inplace=True)

        # Checking if the dataset is balanced or not
        # Dataset is imbalanced
        target_count = data.iloc[:,-1].value_counts()
        print("----------------------------------------------------")
        print("The dataset is imbalanced!")
        print("Therefore downsampling will be applied before training!")
        print('Loan-Default :0 Class :', target_count[0])
        print('Loan-Default :1 Class :', target_count[1])

        # HANDLING IMBALANCED DATA
        # Divide by class
        df_class_0 = data[data['loan_default'] == 0]
        df_class_1 = data[data['loan_default'] == 1]

        # Divide by class again
        df_class_0_under = df_class_0.sample(target_count[1])
        df_train_resampled = pd.concat([df_class_0_under, df_class_1], axis=0)


        data_y = df_train_resampled.iloc[:,-1]
        data_x = df_train_resampled.iloc[:,:-1]
        #

        scalar = StandardScaler()
        logistic_model = LogisticRegression(max_iter=3000)
        gaussian_model = GaussianNB()
        decission_model = DecisionTreeClassifier()

        scalar.fit_transform(data_x)

        max_f1_score = 0
        # Train the models 
        logistic_model.fit(data_x, data_y)
        gaussian_model.fit(data_x, data_y)
        decission_model.fit(data_x, data_y)
        # Calculate f1 score
        f1_score_logistic = f1_score(data.iloc[:,-1], logistic_model.predict(data.iloc[:,:-1]), average='weighted')
        f1_score_gaussian = f1_score(data.iloc[:,-1], gaussian_model.predict(data.iloc[:,:-1]), average='weighted')
        f1_score_decission = f1_score(data.iloc[:,-1], decission_model.predict(data.iloc[:,:-1]), average='weighted')
        model = logistic_model
        if f1_score_logistic > max_f1_score:
            max_f1_score = f1_score_logistic
            model_name = 'logistic'
            model = logistic_model
        if f1_score_gaussian > max_f1_score:
            max_f1_score = f1_score_gaussian
            model_name = 'gaussian'
            model = gaussian_model
        if f1_score_decission > max_f1_score:
            max_f1_score = f1_score_decission
            model_name = 'decission'
            model = decission_model

        print("--------------------------------------------------")
        print(f"Best model is found as {model_name}. It will be used in the following steps.")
        # Saving the model
        with open('classifier.pkl','wb') as file:
            pickle.dump(model,file)

        # Saving the scalar
        with open(scalar_name,'wb') as file:
            pickle.dump(scalar,file)
        
    @staticmethod
    def make_prediction(data, model_name, scalar_name):
        # Load pickle files for model and standardscalar
        with open(model_name,'rb') as file:
            model = pickle.load(file)
        with open(scalar_name,'rb') as file:
            scalar = pickle.load(file)
        
        scalar.transform(data.iloc[:,:-1])
        predictions = model.predict(data.iloc[:,:-1])
        print("--------------------------------------------------")
        print(f"Accuracy is {model.score(data.iloc[:,:-1], data.iloc[:,-1])}")
        print(f"Confusion matrix is :\n{confusion_matrix(data.iloc[:,-1], predictions)}")
        print(f"F1 score is {f1_score(data.iloc[:,-1], model.predict(data.iloc[:,:-1]), average='weighted')}")
        df_prediction=pd.DataFrame(data={"customer_id":data["customer_id"],"label":data["loan_default"],"predictions":predictions})
        return df_prediction

    @staticmethod
    def make_pred_api(data, model, scalar):
        data = pd.DataFrame(jsonable_encoder(data), index=[0])
        data.drop(columns=Constants.dropped_columns,axis=1, inplace=True)
        scalar.transform(data)
        predictions = int(model.predict(data)[0])
        return predictions

