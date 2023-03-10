"""This module contains necessary function needed"""


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st


@st.cache()
def load_data():
    """This function returns the preprocessed data"""

    
    df = pd.read_csv('https://s3-whjr-curriculum-uploads.whjr.online/b510b80d-2fd6-4c08-bfdf-2a24f733551d.csv')

    
    df.rename(columns = {"BloodPressure": "Blood_Pressure",}, inplace = True)
    df.rename(columns = {"SkinThickness": "Skin_Thickness",}, inplace = True)
    df.rename(columns = {"DiabetesPedigreeFunction": "Pedigree_Function",}, inplace = True)

    
    X = df[["Glucose", "Blood_Pressure", "Insulin", "BMI", "Pedigree_Function", "Age"]]
    y = df['Outcome']

    return df, X, y

@st.cache()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1, 
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )
   
    model.fit(X, y)
    
    score = model.score(X, y)

    
    return model, score

def predict(X, y, features):
   
    model, score = train_model(X, y)
   
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score