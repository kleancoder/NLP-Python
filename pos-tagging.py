# Parts of Speech (POS) tagging
# The target of POS tagger is to identify the grammatical group 
# of a given word. For example, Noun, Pronoun, Verb, etc based on the context. 

from nltk import word_tokenize
from nltk import pos_tag

text = """I have seen you drinking with your ex"""
word_tokens = word_tokenize(text)
print(word_tokens)

pos_tags = pos_tag(word_tokens)
print(pos_tags)

# output ===
# ['I', 'have', 'seen', 'you', 'drinking', 'with', 'your', 'ex']
# [('I', 'PRP'), ('have', 'VBP'), ('seen', 'VBN'), ('you', 'PRP'), ('drinking', 'VBG'), ('with', 'IN'), ('your', 'PRP$'), ('ex', 'NN')]
