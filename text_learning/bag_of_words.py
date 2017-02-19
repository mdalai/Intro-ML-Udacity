# Bag of Words
string1 = "hi Katie the self driving car will be late Best Sebastian"
string2 = "Hi Sebastian the Machine Learning class will be great great great Best Katie"
string3 = "Hi Katie the Machine learning class will be most excellent"
email_list = [string1,string2,string3]
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)


print bag_of_words
print vectorizer.vocabulary_.get("great")

# stopwords from NLTK
from nltk.corpus import stopwords
sw = stopwords.words("english")
print sw[0],sw[10],len(sw)

# Stemming with NLTK
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

print stemmer.stem("responsiveness")
print stemmer.stem("unresponsive")