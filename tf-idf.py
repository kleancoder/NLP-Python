from sklearn.feature_extraction.text import TfidfVectorizer
tfVec = TfidfVectorizer()
text_tf = tfVec.fit_transform(data['Phrase'])

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    text_tf, data['Sentiment'], test_size=0.4, random_state= 123
)

from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
clf = MultinomialNB().fit(X_train,Y_train)
predicted = clf.predict(X_test)
predicted("MultinomailNB Accuracy:", metrics.accuracy_score(Y_test,predicted))
