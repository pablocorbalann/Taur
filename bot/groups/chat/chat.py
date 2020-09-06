# This is the main file of the neural net implementation. It contains the main function
# f:aswer() that uses the BOG algorithm and a net to answer a sentence.

#imports
import random
import numpy as np 
import json
import torch
import os
import torch.nn as nn
from groups.chat.model import Net
from groups.chat.nl import bag_of_words, tokenize

# create a device using torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('The directory is: ', os.getcwd())
# open the intents.json file and store its data inside a diccionary using the json module
with open('groups/chat/data/patt.json', 'r') as json_data:
    intents = json.load(json_data)

# create a constant for our file route and load it.
FILE = "groups/chat/data/data.pth"
data = torch.load(FILE)

# create smaller list using the "data" diccionary
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]

# create a neural net using the NN() class
model = Net(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def answer(sentence):
	"""
	This is the main function of all the project, it recibes a sentence:

		p:sentence

	And using other functions in our project, implements the bag of words
	algorithm to answer it.
	"""
	# check if the user wants to exit the chat
	if sentence == 'STOP':
		# break the program
		print('BOG return: 0')
		return 'See you later!'
	# tokenize the sentence
	sentence = tokenize(sentence)
	bog = bag_of_words(sentence, all_words)
	bog = bog.reshape(1, bog.shape[0])
	bog = torch.from_numpy(bog).to(device)
	# create the output using model()
	output = model(bog)
	_, predicted = torch.max(output, dim=1)
	# clasify the tag
	tag = tags[predicted.item()]
	# calculate the probability
	probs = torch.softmax(output, dim=1)
	prob = probs[0][predicted.item()]
	if prob.item() > 0.75:
    	#as the probability is greater than 75%, we answer the sentence
		for intent in intents['intents']:
			if tag == intent["tag"]:
				print('BOG return: 1')
				return str(random.choice(intent['responses']))
	else:
		print('BOG return: 2')
		return "Sorry, I can't understand you..."