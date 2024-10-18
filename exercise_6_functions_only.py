#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder,StandardScaler


# a. Load the data

# In[27]:


def load_data():
    df_1 = pd.read_csv("sample_diabetes_mellitus_data.csv")
    return df_1


# b.  Split the data between train and test. (you can use train_test_split from sklearn or any other way)

# In[28]:


def split_data(df_1):
    train_df, test_df = train_test_split(df_1, test_size=0.3, random_state=42)
    return train_df, test_df


# c. Remove those rows that contain NaN values in the columns: age, gender, ethnicity

# In[29]:


def remove_nan_age_gender_ethnicity(df_1):
    df_2 = df_1.dropna(subset=['age', 'gender', 'ethnicity'])
    return df_2


# d. Fill NaN with the mean value of the column in the columns: height, weight.

# In[30]:


def fill_nan(df_2):
    df_2.loc[:, 'height'] = df_2['height'].fillna(df_2['height'].mean())
    df_2.loc[:, 'weight'] = df_2['weight'].fillna(df_2['weight'].mean())
    return df_2


# e. Generate dummies for ethnicity column (One hot encoding).

# In[31]:


def generate_dummies_ethnicity(df_2):
# Apply one-hot encoding
    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(df_2[['ethnicity']]).toarray()
# Convert the encoded data back to a dataframe
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['ethnicity']))
# Concatenate the encoded dataframe with the 'id' column
    encoded_df = pd.concat([df_2['encounter_id'].reset_index(drop=True), encoded_df], axis=1)
    
    df_3 = pd.merge(df_2, encoded_df, on='encounter_id', how='left')
    return df_3


# f. Create a binary variable for gender M/F.

# In[32]:


def binary_sex(df_3):
    df_3['gender_binary'] = df_3['gender'].map({'M': 1, 'F': 0})
    return df_3


# g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’, ‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target the column: ‘diabetes_mellitus’

# In[33]:


def train_model(df_3):
    features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
    X = df_3[features]
    y = df_3['diabetes_mellitus']

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    return X_train, X_test, y_train, y_test, model
    
    


# h.  Predict the targets for both the train and test sets and add the prediction as a new column (use predict_proba from the model to get the predicted probabilities) name the new column something like predictions

# In[34]:


def predict_prob(X_train, X_test, model, df_3):
# Predict the probabilities for both training and testing sets
    train_prob = model.predict_proba(X_train)[:, 1]  
    test_prob = model.predict_proba(X_test)[:, 1]    

# Combine train and test probabilities into a single array
    all_prob = np.concatenate([train_prob, test_prob])

# Create a new column in df_3 for the combined probabilities
    df_3['probabilities'] = all_prob

# Optionally, print the first few rows to check the results
    print(df_3[['probabilities']].head())
    
    return train_prob, test_prob,  df_3


# i.  Compute the train and test roc_auc metric using roc_auc_score from sklearn

# In[35]:


def roc_auc_score_train_test(y_train, y_test, train_prob, test_prob):
#ROC AUC for the train set
    train_roc_auc = roc_auc_score(y_train, train_prob)

#ROC AUC for the test set
    test_roc_auc = roc_auc_score(y_test, test_prob)

    print(f"Training ROC AUC Score: {train_roc_auc:.2f}")
    print(f"Test ROC AUC Score: {test_roc_auc:.2f}")
    
    return train_roc_auc, test_roc_auc

