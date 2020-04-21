from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

lemma = WordNetLemmatizer()
stemma = PorterStemmer()

word = "dancing"
print("Lemmatized word: ", lemma.lemmatize(word, "v"))
print("Stemmed word: ", stemma.stem(word))

word = "eaten"
print("Lemmatized word: ", lemma.lemmatize(word, "v"))
print("Stemmed word: ", stemma.stem(word))

word = "being"
print("Lemmatized word: ", lemma.lemmatize(word, "v"))
print("Stemmed word: ", stemma.stem(word))

# output ===
# Lemmatized word:  dance
# Stemmed word:  danc
# Lemmatized word:  eat
# Stemmed word:  eaten
# Lemmatized word:  be
# Stemmed word:  be
