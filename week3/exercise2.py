import pandas as pd
import numpy as np
import skimage
from skimage import io
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# read the labels in and only keep the rows where the 
# symbol_id is within the inclusive range [70, 80]
labels = pd.read_csv('hasy-data-labels.csv')
labels = labels[(labels['symbol_id'] >= 70) & (labels['symbol_id'] <= 80)]

# suffle tha data
# split data into training and test sets, 
# using the first 80% of the data for training 
# and the rest for evaluation
msk = np.random.rand(len(labels)) < 0.8
train_labels = labels[msk]
test_labels = labels[~msk]

# read the corresponding images as black-and-white 
# images and flatten them so that each image is a 
# single vector of shape 32x32 == 1024
train_images = []
test_images = []
for p in train_labels['path']:
  img = io.imread(p)
  img = img.flatten()
  train_images.append(img)
for p in test_labels['path']:
  img = io.imread(p)
  img = img.flatten()
  test_images.append(img)

# Fit a logistic regression classifier on your data. 
# Note that since logistic regression is a binary 
# classifier, you will have to, for example, use 
# a so-called “one-vs-all” strategy where the prediction 
# task is formulated as “is the input class X or one 
# of the others?” and the classifier selects the 
# class with the highest probability. 
model = LogisticRegression()
model.fit(train_images, train_labels['symbol_id']) 
print(model.score(test_images, test_labels['symbol_id']))

# Olot some of the images that the logistic classifier 
# classified wrongly. Can you think of why this happens? 
# Would you have gotten it right?
prediction = model.predict(test_images)
prediction_fails = (prediction != test_labels['symbol_id'])
failed = test_labels[prediction_fails]
for f in failed['path']:
  img=mpimg.imread(f)
  imgplot = plt.imshow(img)
  plt.show()