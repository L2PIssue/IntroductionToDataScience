import pandas as pd

# Read the data in your favorite language. 
data = pd.read_csv('all/train.csv')

# Have a look at the data. We will build new representations of the dataset 
# that are better suited for a particular purpose. Some of the columns, 
# e.g Name, simply identify a person and cannot be useful for prediction 
# tasks - remove them.
data = data.drop(['Name'], axis=1)
#data = data.drop(['PassengerId'], axis=1)
data = data.drop(['Ticket'], axis=1)
data = data.drop(['Fare'], axis=1)

# The column Cabin contains a letter and a number. A clever data scientist 
# might conclude that the letter stands for a deck on the ship (which is indeed true)
# and that having just the deck information might improve the results of a classifier 
# predicting an output variable. Add a new column to the dataset, which is simply 
# the deck letter.
data['Deck'] = data['Cabin'].str.replace('\d+', '').astype('category')
data = data.drop(['Cabin'], axis=1)

print(data.describe(include='all'))
# a)  For continous values, replace the missing values with the average of the 
#     non-missing values of that column.
data.fillna(data.mean())

# b)  For discrete and categorical values, replace the missing values with 
#     the mode of the column.
data['Deck'] = data['Deck'].fillna(data['Deck'].value_counts().index[0])
data['Age'] = data['Age'].fillna(data['Age'].value_counts().index[0])

# Write the data, with the modifications, to a .csv file.
data.to_csv('cleaned_data.csv')
# Then, write another file, this time in the json format.
data.to_json('json_data.json', orient="records")