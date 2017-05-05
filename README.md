# telegramStressBot

This is going to be a proof of concept taking a sentence as input and sending back a predicted stress pattern

Using the #NAIL predictive model, there should be either 1 or 2 main sentence stresses (in an informal register), and a simplified version of the algorithm goes like so:

1) find the first main stress by finding the final content word in the sentence.
2) find the second main stress by starting at the beginning of the sentence and moving right until you find one of these (in this order). If you don't find one, move to the next thing to look for. If you find none of them, then there is only one main stress in the sentnece.

- `#` cardinal number (eg, three), ordinal number (eg, third), order words (eg, next/last/previous/following), superlatives (most/Adjective-est/Adverb-est)
- N Noun
- A Adverb, which modifies a verb or a whole phrase
- I Imperative verb (command form)
- L Loud function word (any verb with negation, not, no)
- 1st content word

By "Content word", the project is looking for nouns, adjectives, main verbs (not modals or aux verbs), adverbs, and Wh- question words

based on the work of Dickerson(2015):
https://apling.engl.iastate.edu/alt-content/uploads/2015/05/PSLLT_6th_Proceedings_2014.pdf
