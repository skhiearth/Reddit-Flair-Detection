from flask import Flask,render_template,request,url_for
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle
import string
import re
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_recall_fscore_support as score

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=['POST'])
def predict():
    url = "https://raw.githubusercontent.com/skhiearth/SMS-Spam-Classification-NLP/master/SMSSpamCollection"
    df_data = pd.read_csv(url, sep = "\t", header = None) 
    df_data.columns = ["label", "body"] 

    # Extract Feature With TFIDFVectorizer
    stopword = nltk.corpus.stopwords.words('english') # Defining Stopwords
    ps = nltk.PorterStemmer() # Defining the Porter Stemmer
    wn = nltk.WordNetLemmatizer() # Defining the Word Net Lemmatizer

    def clean_text(text): # This Cleaning Function is called by the Vectorizer
        text_nopunct = "".join([char.lower() for char in text if char not in string.punctuation])
        token = re.split(r"\W+", text_nopunct)
        text_nostopword = [word for word in token if word not in stopword]
        clean_text = [wn.lemmatize(word) for word in text_nostopword]
        return clean_text

    vect = TfidfVectorizer(analyzer = clean_text)
    tfidf_total = vect.fit(df_data['body'])

    model = pickle.load(open('Model/model.pkl', 'rb'))

    if request.method == 'POST':
        comment = request.form['comment']
        data = [comment]
        vect = tfidf_total.transform(data).toarray()
        my_prediction = model.predict(vect)
    return render_template("results.html", prediction=my_prediction, comment=comment)

if __name__ == '__main__':
    app.run()
