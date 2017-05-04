from spacy.en import English

def create_POS_tags(sentence):

    parser = English()
    parsedSentence = parser(sentence)

    taggedArray = []

    for token in parsedSentence:
        taggedArray.append({
            'original': token.orth_,
            'pos': token.tag_
        })

    return taggedArray
