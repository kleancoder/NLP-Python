from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

text2 = """I have seen you drinking with your ex"""
porterStemmer = PorterStemmer()

stop_words2 = set(stopwords.words("english"))
words2 = word_tokenize(text2)
without_stop_words2 = [word for word in words2 if not word in stop_words2]

stemmed_words = []
for tw in without_stop_words2:
    stemmed_words.append(porterStemmer.stem(tw))

print("Filtered Sentence => ", without_stop_words2)
print("Stemmed Sentence => ", stemmed_words)

# output ===
# Filtered Sentence =>  ['I', 'seen', 'drinking', 'ex']
# Stemmed Sentence =>  ['I', 'seen', 'drink', 'ex']
