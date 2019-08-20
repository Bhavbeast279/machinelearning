import nltk
import numpy as np
import random
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open('info.txt', 'r')
raw = f.read()

sentence_tokens = nltk.sent_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()


def len_tokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def len_normalize(text):
    return len_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS =("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ("hi", "hey", "*nods*", "hi there", "hello", "I am glad! you are talking to me")


def greeting(sentence):
    sentence = re.sub('[^\w\s]', '', sentence)
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_input):
    sentence_tokens.append(user_input)
    TfidfVec = TfidfVectorizer(tokenizer = len_normalize)
    tfidf = TfidfVec.fit_transform(sentence_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)
    flat = vals.flatten()
    idx = flat.argsort()[-2]
    flat.sort()
    best_response = flat[-2]

    if best_response == 0:
        return sentence_tokens[idx]
    else:
        return sentence_tokens[idx]
    return None

print("GODBOT: I am the godbot. I can answer any of your questions about the Boston Bruins! I f you would like to leave, type bye.")
name = input("What's your name" )
while True:
    user_input = input(name + ": ").lower()
    print("GODBOT: ", end="") 
    if user_input != 'bye':
        if greeting(user_input) != None:
            print(greeting(user_input))
        else:
            print(response(user_input))
            sentence_tokens.remove(user_input)
    else:
        print('good-bye')
        break
