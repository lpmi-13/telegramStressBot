CONTENT_WORD_TAGS = {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

NUMBER_WORD_TAGS = {'CD', 'JJS', 'RBS'}

#this is a subset of the 'number' words, and should be a not too huge list of order words
NUMBER_ORDER_WORDS = {'next', 'last', 'previous', 'following'}

NOUN_WORD_TAGS = {'NN', 'NNS', 'NNP', 'NNPS'}

#since this tag is used for imperatives, infinitives and old school subjunctives, there might need to be some custom context checking to see if the encountered form is in fact an imperative
IMPERATIVE_VERB_TAG = 'VB'

#since spacy wants to POS tag negation as an adverb (which it technically is, but would be more helpful if there were an easy way to distinguish it), the words are just going to be hardcoded as words here, and the variable name should reflect this
LOUD_FUNCTION_WORDS = {'no', 'not', 'n\'t'}

def predict_stress(array):
   #iterate through the array and use the #NAIL pattern to first find the anchor stress (last content word), then find the preceding stress, if there is one. Then return it all as an array with the two stress marked
    for each item in array:
        #check all the vars above

    return stressMarkedArray 
