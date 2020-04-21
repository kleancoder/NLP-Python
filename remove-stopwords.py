from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import wordnet
from nltk.corpus import stopwords

text = """Hi Mr. John, how are you, please?
I hope you are fine. Tomorrow at 9 am a meeting suggested by Investors."""

# Remove the stop words from a text
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)
print("Words: => ", words)
without_stop_words = [word for word in words if not word in stop_words]
print("Without Stop Words: ", without_stop_words)


# output ===
# Words: =>  ['Hi', 'Mr.', 'John', ',', 'how', 'are', 'you', ',', 'please', '?', 'I', 'hope', 'you', 'are', 'fine', '.', 'Tomorrow', 'at', '9', 'am', 'a', 'meeting', 'suggested', 'by', 'Investors', '.']
# Without Stop Words:  ['Hi', 'Mr.', 'John', ',', ',', 'please', '?', 'I', 'hope', 'fine', '.', 'Tomorrow', '9', 'meeting', 'suggested', 'Investors', '.']
