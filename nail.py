# These are the POS tags used by the Penn Treebank coding system
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

#CC	Coordinating conjunction
#CD	Cardinal number
#DT	Determiner
#EX	Existential there
#FW	Foreign word
#IN	Preposition or subordinating conjunction
#JJ	Adjective
#JJR	Adjective, comparative
#JJS	Adjective, superlative
#LS	List item marker
#MD	Modal
#NN	Noun, singular or mass
#NNS	Noun, plural
#NNP	Proper noun, singular
#NNPS	Proper noun, plural
#PDT	Predeterminer
#POS	Possessive ending
#PRP	Personal pronoun
#PRP$	Possessive pronoun
#RB	Adverb
#RBR	Adverb, comparative
#RBS	Adverb, superlative
#RP	Particle
#SYM	Symbol
#TO	to
#UH	Interjection
#VB	Verb, base form
#VBD	Verb, past tense
#VBG	Verb, gerund or present participle
#VBN	Verb, past participle
#VBP	Verb, non-3rd person singular present
#VBZ	Verb, 3rd person singular present
#WDT	Wh-determiner
#WP	Wh-pronoun
#WP$	Possessive wh-pronoun
#WRB	Wh-adverb

# Searching for the anchor stress, and also for the other content word if none of '#NAIL' found
CONTENT_WORD_TAGS = {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

# Searching for the '#' in #NAIL
NUMBER_WORD_TAGS = {'CD', 'JJS', 'RBS'}
#this is a subset of the 'number' words, and should be a not too huge list of order words
NUMBER_ORDER_WORDS = {'next', 'last', 'previous', 'following'}

# Searching for the 'N' in #NAIL
NOUN_WORD_TAGS = {'NN', 'NNS', 'NNP', 'NNPS'}

# Searching for the 'A' in #NAIL
ADVERB_WORD_TAGS = {'RB', 'RBR'}

'''
since this tag is used for imperatives, infinitives and old school subjunctives, there might need to be some custom context checking to see if the encountered form is in fact an imperative
'''
# Searching for the 'I' in #NAIL
IMPERATIVE_VERB_TAG = 'VB'

'''
since the Penn Tree bank decided to POS tag negation as an adverb (which it technically is, but would be more helpful if there were an easy way to distinguish it), the words are just going to be hardcoded as words here, and the variable name should reflect this
'''
# Searching for the 'L' in #NAIL
LOUD_FUNCTION_WORDS = {'no', 'not', 'n\'t'}

def predict_stress(array):
    '''
    iterate through the array and use the #NAIL pattern to first find the anchor stress (last content word),
    then find the preceding stress, if there is one. Then return it all as an array with the two stresses marked
    '''

    stress_array = []

    last_content_word = find_anchor(array)

    if last_content_word:

        stress_array.append(last_content_word)

        # '#'
        check_for_number = find_number(array)

        if check_for_number and check_for_number != last_content_word:

            stress_array.append(check_for_number)

        else:

            # 'N'
            check_for_noun = find_noun(array)

            if check_for_noun and check_for_noun != last_content_word:

                stress_array.append(check_for_noun)

            else:

                # 'A'
                check_for_adverb = find_adverb(array)

                if check_for_adverb and check_for_adverb != last_content_word:

                    stress_array.append(check_for_adverb)

                else:

                    # 'I'
                    check_for_imperative = find_imperative(array)

                    if check_for_imperative or check_for_imperative == 0 and check_for_imperative != last_content_word:

                        stress_array.append(check_for_imperative)

                    else:

                        # 'L'
                        check_for_loud_function_word = find_loud_function_word(array)

                        if check_for_loud_function_word and check_for_loud_function_word != last_content_word:

                            stress_array.append(check_for_loud_function_word)

                        else:

                            check_for_content_word = find_other_content_word(array)

                            if check_for_content_word and check_for_content_word != last_content_word:

                                stress_array.append(check_for_content_word)

                            else:

                                return
        return stress_array

    else:
        print 'sentence too weird to predict stress.'

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

# this function could most definitely be better optimized
def find_imperative(array):

    imperative = next((x for x in array if x[1] == 'VB'), None)

    if imperative == None:
        return None
    else:
        possible_imperative_position = array.index(imperative)

        if possible_imperative_position == 0:

            return possible_imperative_position

        else:

            word_before_possible_imperative_position = array[possible_imperative_position - 1]

            # checking to see that the identified word is not an infinitive, following a modal, or matched with a subject
            if word_before_possible_imperative_position[0] and word_before_possible_imperative_position[0].lower() != 'to' and word_before_possible_imperative_position[1] != 'MD' and word_before_possible_imperative_position[1] != 'PRP' and word_before_possible_imperative_position[1] not in NOUN_WORD_TAGS:
                return possible_imperative_position
            else:
                return None

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
