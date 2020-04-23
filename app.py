from flask import Flask,render_template,request,url_for
import pandas as pd
import numpy as np
import pickle
import string
import re
import nltk
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf

from account import id, secret, appName, username
import praw # Python Reddit API Wrapper
import pandas as pd 
import datetime as dt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/automated_testing", methods=['POST'])  
def predict():

    with open('Models/LSTMTokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = tf.keras.models.load_model('Models/LSTM.h5')

    if request.method == 'POST':
        comment = request.form['comment']

        def remove_prefix(text, prefix):
            return text[text.startswith(prefix) and len(prefix):]

        comment = remove_prefix(comment, 'https://www.reddit.com/r/india/comments/')
        comment = comment.split('/', 1)[0]

        # Reddit and subreddit instances
        reddit = praw.Reddit(client_id=id, \
                            client_secret=secret, \
                            user_agent=appName, \
                            username=username)

        submission = reddit.submission(id=comment)
        title = submission.title
        body = submission.selftext

        text_to_classify = title + body

        data = [text_to_classify]
        vect = tokenizer.texts_to_sequences(data)
        vect = pad_sequences(vect, maxlen=250)
        
        my_prediction = model.predict(vect)
        my_prediction = np.argmax(my_prediction, axis=1)
        print(my_prediction)
    return render_template("automated_testing.html", prediction=my_prediction, comment=text_to_classify)

if __name__ == '__main__':
    app.run(debug=True)
