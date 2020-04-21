from nltk.propability import FreqDist 
from matplotlib.pyplot as plt

text = """Hi Mr. John, how are you, please?
I hope you are fine. Tomorrow at 9 am a meeting suggested by Investors."""

tokenized_text = sent_tokenize(text)
# print("tokenized text => ", tokenized_text)

tokenized_word = word_tokenize(text)
# print("tokenized word => ", tokenized_word)

fdist = FreqDist(tokenized_word)

fdist.plot(30,cumulative=False)
plt.show()
