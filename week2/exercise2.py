import pandas as pd

data = pd.read_csv('cleaned_data.csv')

# First consider each feature variable in turn. For categorical variables, 
# find out the most frequent value, i.e., the mode. For numerical variables, 
# calculate the median value.
print(data.describe(include='all'))

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