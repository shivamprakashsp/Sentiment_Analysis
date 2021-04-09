# Sentiment_Analysis 

This project is based on the dataset available at https://www.kaggle.com/c/tweet-sentiment-extraction/overview which is composed of about 20k tweets to train sentiment predictors.

The "TweetsSentimentPredictions.ipynb" notebook will guide you through the process of tweets cleaning (a very basic NLP task when dealing with text data), training a few Deep Learning models with different architectures and doing some sample predictions. 


# Sentiment Predictor Web App (Flask)

### How to run (with Docker)

Step 1 -> git clone

Step 2-> Change the current working directory to the cloned repository's directory

Step 3 -> docker build -t flaskapp .

Step 4 -> docker run -p 8000:8000 flaskapp


### Without docker (must have python 3.7 or above installed)

Step 1 -> git clone

Step 2 -> Install the following python libraries :-

numpy==1.19.2 or later 

tensorflow==2.3.0 or later

Keras ==2.4.3 or later

Flask ==1.1.2 or later

Step 3-> Change the current working directory to the cloned repository's directory

Step 4-> python app.py



