import nltk
from nltk import word_tokenize

def create_POS_tags(sentence):

    parsedSentence = word_tokenize(sentence)

    return nltk.pos_tag(parsedSentence)
