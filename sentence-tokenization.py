from nltk.tokenize import sent_tokenize

# Sentence tokenizer breaks text paragraphs into sentences

text = """Hi Mr. John, how are you, please?
I hope you are fine. Tomorrow at 9 am a meeting suggested by Investors."""

tokenized_text = sent_tokenize(text)
print("tokenized text => ", tokenized_text)

# output === 
# tokenized text =>  ['Hi Mr. John, how are you, please?', 'I hope you are fine.', 'Tomorrow at 9 am a meeting suggested by Investors.']
