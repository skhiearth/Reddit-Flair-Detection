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

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=['POST'])
def predict():

    with open('Models/LSTMTokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = tf.keras.models.load_model('Models/LSTM.h5')

    if request.method == 'POST':
        comment = request.form['comment']
        data = [comment]
        vect = tokenizer.texts_to_sequences(data)
        vect = pad_sequences(vect, maxlen=250)
        
        my_prediction = model.predict(vect)
        my_prediction = np.argmax(my_prediction, axis=1)
        print(my_prediction)
    return render_template("results.html", prediction=my_prediction, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
