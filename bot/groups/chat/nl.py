# In this file natural language tool kit (nltk) utils are stored in different
# functions. 

# imports
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
	"""
	Using the bag words algorithm, every sentence has to be deconstructed to a
	list of relevant particles. This function ecibes a sequence and uses the
	nltk.word_tokenize() functtion to return a tokenized list.

	>>>tokenize('How are you?')
	['how', 'are', 'you', '?']
	"""
	return nltk.word_tokenize(sentence)

def stem(word):
	"""
	The second step using the bag word algorithm is to stem every single tokenized
	word to get it's root. For example:

	>>>stem('organ')
	orga
	>>>stem('organization')
	orga
	"""
	return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
	"""
	This is the final step in the pre-bag of words algorithm. It recibes two parameters:

		p:tokenized_sentence => a tokenized sentence
		p:words => a set of words

	Let's see an example:
	tokenized_sentence .... ['hello', 'how', 'are', 'you']
	words ................. ['hi', 'hello', 'i', 'how', 'bye', 'thank', 'cool']
	bag ................... [0, 1, 0, 1, 0, 0, 0]
	"""
	tokenized_sentence = [stem(word) for word in tokenized_sentence]
	bag = np.zeros(len(words), dtype=np.float32)
	for idx, word in enumerate(words):
		if word in tokenized_sentence:
			bag[idx] = 1.0

	return bag