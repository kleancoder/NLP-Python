# word tokenizer breaks text paragraphs into words. 

from nltk.tokenize import word_tokenize

text = """Hi Mr. John, how are you, please?
I hope you are fine. Tomorrow at 9 am a meeting suggested by Investors."""

tokenized_word = word_tokenize(text)
print("tokenized word => ", tokenized_word)

# output ===
# tokenized word =>  ['Hi', 'Mr.', 'John', ',', 'how', 'are', 'you', ',', 'please', '?', 'I', 'hope', 'you', 'are', 'fine', '.', 'Tomorrow', 'at', '9', 'am', 'a', 'meeting', 'suggested', 'by', 'Investors', '.']
