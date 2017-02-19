import pickle

words_file = "../tools/word_data.pkl" 
#authors_file = "../tools/email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
#authors = pickle.load( open(authors_file, "r") )

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit_transform(word_data)
tfldf = vectorizer.get_feature_names()
#idf = vectorizer.idf_
#print tfldf[1:20]
print "How many features---- ", len(tfldf)


print tfldf[34597]
print tfldf[100]