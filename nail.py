CONTENT_WORD_TAGS = {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

NUMBER_WORD_TAGS = {'CD', 'JJS', 'RBS'}

#this is a subset of the 'number' words, and should be a not too huge list of order words
NUMBER_ORDER_WORDS = {'next', 'last', 'previous', 'following'}

NOUN_WORD_TAGS = {'NN', 'NNS', 'NNP', 'NNPS'}

ADVERB_WORD_TAGS = {'RB', 'RBR'}

#since this tag is used for imperatives, infinitives and old school subjunctives, there might need to be some custom context checking to see if the encountered form is in fact an imperative
IMPERATIVE_VERB_TAG = 'VB'

#since spacy wants to POS tag negation as an adverb (which it technically is, but would be more helpful if there were an easy way to distinguish it), the words are just going to be hardcoded as words here, and the variable name should reflect this
LOUD_FUNCTION_WORDS = {'no', 'not', 'n\'t'}

def predict_stress(array):
   #iterate through the array and use the #NAIL pattern to first find the anchor stress (last content word), then find the preceding stress, if there is one. Then return it all as an array with the two stress marked

    print array

    last_content_word = find_anchor(array)

    if last_content_word:
        print 'found last content word at position: ' + str(last_content_word)

    

    check_for_number = find_number(array)

    if check_for_number and check_for_number != last_content_word:
        print 'found number word at position: ' + str(check_for_number)

    check_for_noun = find_noun(array)

    if check_for_noun and check_for_noun != last_content_word:
        print 'found noun at position: ' + str(check_for_noun)

    check_for_adverb = find_adverb(array)

    if check_for_adverb and check_for_adverb != last_content_word:
        print 'found adverb at position: ' + str(check_for_adverb)


#####still not sure how to approach this, since 'imperative tagging
#####will require context-based processing, possibly bi/tri-grams
#    check_for_imperative = find_imperative(array)

#    if check_for_imperative:
#        print 'found imperative at position: ' + str(check_for_imperative)

    check_for_loud_function_word = find_loud_function_word(array)

    if check_for_loud_function_word and check_for_loud_function_word != last_content_word:
        print 'found loud function word at position: ' + str(check_for_loud_function_word)

    check_for_content_word = find_other_content_word(array)

    if check_for_content_word and check_for_content_word != last_content_word:
        print 'found second to last content word at position: ' + str(check_for_content_word)

def find_anchor(array):

    array.reverse()

    final = next((x for x in array if x[1] in CONTENT_WORD_TAGS), None)
    if final == None:
        return None
    else:
        array.reverse()

        return array.index(final)

def find_number(array):

    number_word = next((x for x in array if x[1] in NUMBER_WORD_TAGS or x[0] in NUMBER_ORDER_WORDS), None)

    if number_word == None:
        return None
    else:
        return array.index(number_word)

def find_noun(array):

    noun = next((x for x in array if x[1] in NOUN_WORD_TAGS), None)
    if noun == None:
        return None
    else:
        return array.index(noun)

def find_adverb(array):

    adverb = next((x for x in array if x[1] in ADVERB_WORD_TAGS), None)

    if adverb == None:
        return None
    else:
        return array.index(adverb)

#skeleton of this function
#def find_imperative(array):

#    imperative = next((x for x in array if x[1] == 'VB'), None)

#    if imperative == None:
#        return None
#    else:
#        adverb_position = array.index(imperative)

#        word_before_position = array[adverb_position - 1]

#        if word_before_position[0] and word_before_position[0].lower() != 'to':
#            return adverb_position
#        else:
#            return None

def find_loud_function_word(array):

    loud_function_word = next((x for x in array if x[0] in LOUD_FUNCTION_WORDS), None)

    if loud_function_word == None:
        return None
    else:
        return array.index(loud_function_word)

def find_other_content_word(array):

    content_word = next((x for x in array if x[1] in CONTENT_WORD_TAGS), None)

    if content_word == None:
        return None
    else:
        return array.index(content_word)
