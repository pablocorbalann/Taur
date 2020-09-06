# This file is used to store train our neural net (located in ./connections.py) using 
# different modules and a data file to stre the trained segments


# imports
import json
import random
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from nl import bag_of_words, tokenize, stem
from connections import Net

# open the intents.json file and load it into a diccionary using the json module
with open('intents.json', 'r') as f:
    intents = json.load(f)

#create all the lists we need to store our data.
all_words = []
tags = []
xy = []
train_x, train_y = [], []
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    actual_tag = intent['tag']
    # add the actual_tag to our "tags" list
    tags.append(actual_tag)
    # loop the paterns of the tag
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        tokenized_word = tokenize(pattern)
        # add to our words list and to the xy list
        all_words.extend(tokenized_word)
        xy.append((tokenized_word, actual_tag))

# stem and lower each word
all_words = [stem(word) for word in all_words if word not in ['?', '.', '!', ',']] # <= ignore words
# remove duplicates and sort using the sorted() and set() python functions
all_words = sorted(set(all_words))
tags = sorted(set(tags))

# create training data
for (pattern_sentence, tag) in xy:
    # X: bag of words for each pattern_sentence
    X_train.append(bag_of_words(pattern_sentence, all_words))
    # Y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    y_train.append(tags.index(tag))
# convert train_x/y to numpy arrays
train_x = np.array(train_x)
train_y = np.array(train_y)

# Hyper-parameters 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
# net attributes
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
# create the DataSets()
dataset = ChatDataset()
model Net(input_size, hidden_size, output_size)