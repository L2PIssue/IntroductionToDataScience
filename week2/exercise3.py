from collections import Counter

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