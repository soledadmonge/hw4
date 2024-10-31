# %% [markdown]
# ### Exercise 1:
# Create a function called "count_simba" that counts and returns the number of times that Simba appears in a list of strings. Example: "Simba and Nala are lions.", "I laugh in the face of danger.",  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."

# %%
from functools import reduce
listofstrings = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two"]

def count_simba(listofstrings,word): # Function takes a list of strings and counts how many times a certain word appears in the list
    counts_list = list(map(lambda single_string: single_string.count(word), listofstrings)) # Outputs a list of numbers that represent the count of the word in each string
    count = reduce(lambda x,y: x+y, counts_list) # Adds up the numbers in the list produced above
    print(f"The word '{word}' appears {count} times.")

#user_word = input("Enter word: ") #This line will run in a .py file, but need to change "Simba" in next line to user_word
count_simba(listofstrings,"Simba")

# %% [markdown]
# ### Exercise 2:
# Create a function called "get_day_month_year" that takes a list of datetimes.date and returns a pandas dataframe with 3 columns (day, month, year) in which each of the rows is an element of the input list and has as value its  day, month, and year.

# %%
import pandas as pd
import datetime 
from datetime import date
from functools import reduce

num_of_dates = 10
today = datetime.datetime.today()
date_list = [date.today() + datetime.timedelta(days=x) for x in range(num_of_dates)]

def get_day_month_year(dates):
    day_month_year = list(map(lambda dmy: {'day': dmy.day, 'month': dmy.month, 'year': dmy.year}, dates)) # Use map to extract the day, month, and year from each date in the list
    #day_month_year_list = reduce(lambda acc, x: acc + [x], day_month_year, []) # Reduce the mapped results to a list of dictionaries
    
# Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(day_month_year)
    dates = date_list  
    return df

get_day_month_year(date_list)

# %% [markdown]
# ### Exercise 3:
# Create a function called "compute_distance" that takes a list of tuple pairs with latitude and longitude coordinates and returns a list with the distance between the two pairs example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))] HINT: You can use geopy.distance in order to compute the distance

# %%
import geopy
from geopy.distance import geodesic

# To calculate the distance of two points we can use "geodesic" or "great_circle". We are going to use the first one:
def compute_distance(pairs):
    # We use lambda to calculate the distance between each pair of coord (in this case, coords[0] and coords[1]). 
    # "map" applies this lambda to each element of "pairs". 
    # The result is an iterable with the distances, which we then convert to a list.
    return list(map(lambda coords: geodesic(coords[0], coords[1]).kilometers, pairs))

pairs = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
dist_km = compute_distance(pairs)
dist_km

# %% [markdown]
# ### Exercise 4:
# Consider a list that each element can be an integer or a list that contains integers or more lists with integers example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. Create a recursive function called "sum_general_int_list" that takes as input this type of list and returns the sum of all the integers within the lists for instance for list_1=[[2], 3, [[1,2],5]] the result should be 13.

# %%
def sum_general_int_list(list_ex):
    # We use lambda and isistance to check if an element "x" is a list or an integer:
     # a) If "x" is a list, the function makes a recursive call to sum_general_int_list(x) to decompose that list and sum its elements.
     # b) If "x" is an integer, lambda returns the value of "x" and adds it.
    # "map" applies this lambda to each element of "list". 
    # The result is the sum of all the elements.
    return sum(map(lambda x: sum_general_int_list(x) if isinstance(x, list) else x, list_ex))

list_ex = [[2], 3, [[1, 2], 5]]
result = sum_general_int_list(list_ex)
result

# %% [markdown]
# ### Exercise 5

# %% [markdown]
# a. Load the data

# %%
df_1 = pd.read_csv("/Users/newmac/Documents/DSDM/01_Computing_for_DS/hw4-1/sample_diabetes_mellitus_data.csv")
df_1.shape

# %%
train_df, test_df = train_test_split(df_1, test_size=0.3, random_state=42)

# %%
df_2.loc[:, 'height'] = df_2['height'].fillna(df_2['height'].mean())
df_2.loc[:, 'weight'] = df_2['weight'].fillna(df_2['weight'].mean())

# %%
# Apply one-hot encoding
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df_2[['ethnicity']]).toarray()
# Convert the encoded data back to a dataframe
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['ethnicity']))
# Concatenate the encoded dataframe with the 'id' column
encoded_df = pd.concat([df_2['encounter_id'].reset_index(drop=True), encoded_df], axis=1)
encoded_df.shape

# %%
df_3 = pd.merge(df_2, encoded_df, on='encounter_id', how='left')
df_3.shape

# %%
df_3['gender_binary'] = df_3['gender'].map({'M': 1, 'F': 0})
df_3.shape

# %%
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

# %%
# Predict the probabilities for both training and testing sets
train_prob = model.predict_proba(X_train)[:, 1]  
test_prob = model.predict_proba(X_test)[:, 1]    

# Combine train and test probabilities into a single array
all_prob = np.concatenate([train_prob, test_prob])

# Create a new column in df_3 for the combined probabilities
df_3['probabilities'] = all_prob

# Optionally, print the first few rows to check the results
print(df_3[['probabilities']].head())

# %%
#ROC AUC for the train set
train_roc_auc = roc_auc_score(y_train, train_prob)

#ROC AUC for the test set
test_roc_auc = roc_auc_score(y_test, test_prob)

print(f"Training ROC AUC Score: {train_roc_auc:.2f}")
print(f"Test ROC AUC Score: {test_roc_auc:.2f}")

# %% [markdown]
# ### Exercise 7

# %%
from eda_lib.eda_func_1 import *

# %%
df_1 = load_data('sample_diabetes_mellitus_data.csv')

# %%
train_df, test_df = split_data(df_1)

# %%
df_2 = remove_nan(df_1, ['age', 'gender', 'ethnicity'])

# %%
df2_nan_filled = fill_nan(df_2, ['height', 'weight'])

# %%
df_3 = generate_dummies_hot_encoder(df2_nan_filled, ['ethnicity'])

# %%
df_3_sex_bin = binary_sex(df_3, 'gender')

# %%
features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
target = 'diabetes_mellitus'
X_train, X_test, y_train, y_test, model = train_model_LogisticRegresion(df_3_sex_bin,features, target )

# %%
train_prob, test_prob, new_df_3 = predict_prob(X_train, X_test, model, df_3_sex_bin)

# %%
train_roc_auc, test_roc_auc = roc_auc_score_train_test(y_train, y_test, train_prob, test_prob)

# %%
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder,StandardScaler
a. Load the data
df_1 = pd.read_csv("sample_diabetes_mellitus_data.csv")
df_1.shape
b.  Split the data between train and test. (you can use train_test_split from sklearn or any other way)
train_df, test_df = train_test_split(df_1, test_size=0.3, random_state=42)
c. Remove those rows that contain NaN values in the columns: age, gender, ethnicity
df_2 = df_1.dropna(subset=['age', 'gender', 'ethnicity'])
df_2.shape
d. Fill NaN with the mean value of the column in the columns: height, weight.
df_2.loc[:, 'height'] = df_2['height'].fillna(df_2['height'].mean())
df_2.loc[:, 'weight'] = df_2['weight'].fillna(df_2['weight'].mean())
e. Generate dummies for ethnicity column (One hot encoding).
# Apply one-hot encoding
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df_2[['ethnicity']]).toarray()
# Convert the encoded data back to a dataframe
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['ethnicity']))
# Concatenate the encoded dataframe with the 'id' column
encoded_df = pd.concat([df_2['encounter_id'].reset_index(drop=True), encoded_df], axis=1)
encoded_df.shape
df_3 = pd.merge(df_2, encoded_df, on='encounter_id', how='left')
df_3.shape
f. Create a binary variable for gender M/F.
df_3['gender_binary'] = df_3['gender'].map({'M': 1, 'F': 0})
df_3.shape
g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’, ‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target the column: ‘diabetes_mellitus’
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
h.  Predict the targets for both the train and test sets and add the prediction as a new column (use predict_proba from the model to get the predicted probabilities) name the new column something like predictions
# Predict the probabilities for both training and testing sets
train_prob = model.predict_proba(X_train)[:, 1]  
test_prob = model.predict_proba(X_test)[:, 1]    

# Combine train and test probabilities into a single array
all_prob = np.concatenate([train_prob, test_prob])

# Create a new column in df_3 for the combined probabilities
df_3['probabilities'] = all_prob

# Optionally, print the first few rows to check the results
print(df_3[['probabilities']].head())
i.  Compute the train and test roc_auc metric using roc_auc_score from sklearn
#ROC AUC for the train set
train_roc_auc = roc_auc_score(y_train, train_prob)

#ROC AUC for the test set
test_roc_auc = roc_auc_score(y_test, test_prob)

print(f"Training ROC AUC Score: {train_roc_auc:.2f}")
print(f"Test ROC AUC Score: {test_roc_auc:.2f}")


