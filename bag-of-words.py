from sklearn.feature_extraction.text import CountVectorizer

# list of text documents
textDocument = ["The quick brown fox jumped over the lazy dog"]

# create the transform
vectorizer = CountVectorizer()

# tokenize and build vocabulary
vectorizer.fit(textDocument)

# summarize and print vocabulary
print(vectorizer.vocabulary_)

# encode text document
vector = vectorizer.transform(textDocument)

# summarize encoded vector
print(vector.shape)
print(type(vector))
print(vector.toarray())
