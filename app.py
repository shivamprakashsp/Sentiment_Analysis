from flask import Flask,url_for,render_template,request

# Importing Required Libaries
import tensorflow as tf
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import spacy
import nltk
import numpy as np
import pandas as pd
from numpy import load



# Env variables 
max_len = 200
max_words = 5000


# load array
data = load('data.npy')
# Loding Model 

best_model = keras.models.load_model("static/models/best_model2.hdf5")


# init app
app = Flask(__name__)

# Route
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/predict',methods = ['GET','POST'])

def predict():
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		# Predictions 
		sentiment = ['Neutral','Negative','Positive']
		tokenizer = Tokenizer(num_words=max_words)
		tokenizer.fit_on_texts(data)
		sequence = tokenizer.texts_to_sequences([rawtext])
		test = pad_sequences(sequence, maxlen=max_len)
		ans = sentiment[np.around(best_model.predict(test), decimals=0).argmax(axis=1)[0]]
	return render_template('index.html',rawtext=rawtext.upper(),result = ans)	
if __name__ =='__main__':
	app.run(debug =False)