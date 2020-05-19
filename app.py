from flask import Flask,render_template,request,url_for, jsonify, json
import os
import pandas as pd
import numpy as np
import pickle
import string
import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import json
import praw # Python Reddit API Wrapper
import pandas as pd 
import datetime as dt

PATH_TO_UPLOAD_FOLDER = 'static/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PATH_TO_UPLOAD_FOLDER

preds = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def automated():

    def remove_prefix(text, prefix):
        return text[text.startswith(prefix) and len(prefix):]

    # Reddit and subreddit instances
    reddit = praw.Reddit(client_id="_zZVrgo-Rbu5TA", \
                        client_secret="rPt0ZY2LYlS8pYx1IHwl1GKQDsw", \
                        user_agent="flare-detection", \
                        username="skhiearth")

    with open('Models/LSTMTokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = tf.keras.models.load_model('Models/LSTM.h5')

    if request.method == 'POST':
        comment = request.files['upload_file']
        comment.save(os.path.join(app.config['UPLOAD_FOLDER'], 'file.txt'))

        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'file.txt')

        with open(full_filename, 'r') as fp:
            for _, line in enumerate(fp):
                url = line

                line = remove_prefix(line, 'https://www.reddit.com/r/india/comments/')
                line = line.split('/', 1)[0]

                submission = reddit.submission(id=line)
                title = submission.title
                body = submission.selftext

                text_to_classify = title + body

                data = [text_to_classify]
                vect = tokenizer.texts_to_sequences(data)
                vect = pad_sequences(vect, maxlen=250)

                my_prediction = model.predict(vect)

        return my_prediction


@app.route("/resultText", methods=['POST'])  
def resultText():

    with open('Models/LSTMTokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = tf.keras.models.load_model('Models/LSTM.h5')

    if request.method == 'POST':
        comment = request.form['commentText']

        text_to_classify = comment

        data = [text_to_classify]
        vect = tokenizer.texts_to_sequences(data)
        vect = pad_sequences(vect, maxlen=250)
        
        my_prediction = model.predict(vect)
        my_prediction = np.argmax(my_prediction, axis=1)
        print(my_prediction)
    return render_template("resultText.html", prediction=my_prediction, comment=text_to_classify)

@app.route("/result", methods=['POST'])  
def result():

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
        reddit = praw.Reddit(client_id="_zZVrgo-Rbu5TA", \
                            client_secret="rPt0ZY2LYlS8pYx1IHwl1GKQDsw", \
                            user_agent="flare-detection", \
                            username="skhiearth")

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
    return render_template("result.html", prediction=my_prediction, comment=text_to_classify)

if __name__ == '__main__':
    app.run()
