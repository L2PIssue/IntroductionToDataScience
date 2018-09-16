import json
import string
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem.snowball import SnowballStemmer

def json_readr(file):
  for line in open(file, mode="r"):
    yield json.loads(line)

# Open the json file in your favorite environment, e.g python.
data = json_readr('reviews_Automotive_5.json')

# Access the reviewText field, and downcase the contents.
# Remove all punctuation, as well as the stop-words. 
# Apply a stemmer on the paragraphs, so that inflected forms are mapped to the base form. 
# For example, for python the popular natural language toolkit nltk has an easy-to-use stemmer.
# Filter the data by selecting reviews where the field overall is 4 or 5, 
# and store the review texts in file pos.txt. Similarly, select reviews with rating 1 or 2 
# and store the reviews in file neg.txt. (Ignore the reviews with overall rating 3.) 
# Each line in the two files should contain exactly one preprocessed review text without the rating.
translator = str.maketrans('', '', string.punctuation)
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

pos = open('pos.txt', 'a')
neg = open('neg.txt', 'a')

for line in data:
  s = line['reviewText']
  line['reviewText'] = s.lower().translate(translator)

  word_tokens = word_tokenize(line['reviewText']) 
  
  filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  filtered_sentence = [] 
    
  for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(stemmer.stem(w)) 
  line['reviewText'] = ' '.join(filtered_sentence)

  overall = line['overall']
  to_be_written = line['reviewText'] + '\n'

  if overall >= 4:
    pos.write(to_be_written)
  elif overall <= 2:
    neg.write(to_be_written)
