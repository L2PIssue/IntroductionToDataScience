from collections import Counter
from nltk.tokenize import word_tokenize 
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Find the most common words in each file. What are they? Are some of them clearly
# general terms relating to the nature of the data, and not just the emotion?
with open("../week1/pos.txt") as input_file:
  count = Counter(word for line in input_file
                       for word in line.split())
print('The most common words in positive reviews:\n', count.most_common(10))
with open("../week1/neg.txt") as input_file:
  count = Counter(word for line in input_file
                       for word in line.split())
print('The most common words in negative reviews:\n', count.most_common(10))

# Compute a TF/IDF vector for each of the text files, and make them into a 
# 2 x m matrix, where m is the number of unique words in the data. 
# List the words with the highest TF/IDF score in each class

# positive
with open("../week1/pos.txt") as input_file:
  pos = input_file.read().replace('\n', '')
pos_tokens = word_tokenize(pos)
vectorizer = TfidfVectorizer()
pos_matrix = vectorizer.fit_transform(pos_tokens)

indices = np.argsort(vectorizer.idf_)[::-1]
features = vectorizer.get_feature_names()
top_n = 10
top_features = [features[i] for i in indices[:top_n]]
print(top_features)

# negative
with open("../week1/neg.txt") as input_file:
  neg = input_file.read().replace('\n', '')
neg_tokens = word_tokenize(neg)
vectorizer = TfidfVectorizer()
neg_matrix = vectorizer.fit_transform(neg_tokens)

indices = np.argsort(vectorizer.idf_)[::-1]
features = vectorizer.get_feature_names()
top_n = 10
top_features = [features[i] for i in indices[:top_n]]
print(top_features)

# Plot the words in each class and their corresponding TF/IDF scores. 
# Note that there will be a lot of words, so you’ll have to think 
# carefully to make your chart clear! If you can’t plot them all, 
# plot a subset – think about how you should choose this subset.