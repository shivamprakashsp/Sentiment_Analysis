# Sentiment_Analysis 

This project is based on the dataset available at https://www.kaggle.com/c/tweet-sentiment-extraction/overview which is composed of about 20k tweets to train sentiment predictors.

The "TweetsSentimentPredictions.ipynb" notebook will guide you through the process of tweets cleaning (a very basic NLP task when dealing with text data), training a few Deep Learning models with different architectures.


# Sentiment Predictor Web App (Flask)

### How to use (with Docker)

Step 1 -> git clone

Step 2 -> docker build -t flaskapp .

Step 3 -> docker run -p 8000:8000 flaskapp


### Without docker (Install the following libraries before running the app)

numpy==1.19.2 or later

tensorflow==2.3.0 or later

Keras ==2.4.3 or later

Flask ==1.1.2 or later



