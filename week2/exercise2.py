import pandas as pd

data = pd.read_csv('cleaned_data.csv')

# First consider each feature variable in turn. For categorical variables, 
# find out the most frequent value, i.e., the mode. For numerical variables, 
# calculate the median value.
mode_survived = data['Survived'].mode()
print(mode_survived)
mode_pclass = data['Pclass'].mode()
print(mode_pclass)
mode_sex = data['Sex'].mode()
print(mode_sex)
mode_embarked = data['Embarked'].mode()
print(mode_embarked)
mode_deck = data['Deck'].mode()
print(mode_deck)

mean_age = data['Age'].mean()
print(mean_age)
mean_sibsp = data['SibSp'].mean()
print(mean_sibsp)
mean_parch = data['Parch'].mean()
print(mean_parch)

# Combining the modes of the categorical variables, and the medians of the numerical 
# variables, construct an imaginary “average survivor” on board of the ship. 
# Also following the same procedure for using subsets of the passengers, 
# construct the the “average non-survivor”.


# Now study the distributions of the variables in the two groups. 
# How well do the average cases represent the respective groups? 
# Can you find actual passengers that are very similar to the representative 
# of their own group (survivor/non- survivor)? Can you find passengers 
# that are very similar to the representative of the other group? 


# To give a more complete picture of the two groups, provide graphical 
# displays of the distribution of the variables in each group whenever 
# appropriate (not, e.g., on the ticket number).


# One step further is the analysis of pairwise and multivariate relationships 
# between the variables in the two groups. Try to visualize two variables 
# at a time using, e.g., scatter plots and use a different color 
# to display the survival status. 


# Finally, recall the preprocessing that was carried out in last week’s exercises. 
# Can you say something about the effect of the choices that were made, 
# in particular, to use the mode or the mean to impute missing values, 
# instead of, for example, ignoring passengers with missing data?
    # 1.  Since a lot of the passengers are missin data, I'd say ignoring those passengers
    #     completely is not such a good idea (too little data).
    # 2.  Only a small number of the passengers have info about the Cabin 
    #     (and thus the Deck) so I'd think it might be wiser to ignore the Cabin data.