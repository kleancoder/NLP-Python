from nltk.propability import FreqDist 

text = """Hi Mr. John, how are you, please?
I hope you are fine. Tomorrow at 9 am a meeting suggested by Investors."""

tokenized_text = sent_tokenize(text)
# print("tokenized text => ", tokenized_text)

tokenized_word = word_tokenize(text)
# print("tokenized word => ", tokenized_word)

fdist = FreqDist(tokenized_word)
print("Frequency distribution => ", fdist)
print("Most common (2) => ", fdist.most_common(2))

# output ===
# Frequency distribution =>  <FreqDist with 22 samples and 26 outcomes>
# Most common (2) =>  [(',', 2), ('are', 2)]
