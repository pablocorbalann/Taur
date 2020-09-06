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
from model import Net

# create the cuda
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# open the intents.json file and load it into a diccionary using the json module
with open('groups/chat/data/patt.json', 'r') as f:
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
    train_x.append(bag_of_words(pattern_sentence, all_words))
    # Y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    train_y.append(tags.index(tag))
# convert train_x/y to numpy arrays
train_x = np.array(train_x)
train_y = np.array(train_y)

# Hyper-parameters 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
# net attributes
input_size = len(train_x[0])
hidden_size = 8
output_size = len(tags)

# create the DataSet() class
class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(train_x) 
        self.x_data = train_x
        self.y_data = train_y

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

# create the DataSet()
dataset = ChatDataset()
model = Net(input_size, hidden_size, output_size)
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
# Train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # Forward pass
        outputs = model(words)
        # if y would be one-hot, we must apply
        # labels = torch.max(labels, 1)[1]
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

print(f'final loss: {loss.item():.4f}')

#create the data diccionary
data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "groups/chat/data/data.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}')