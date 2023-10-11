import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import streamlit as st

@st.cache_data
def load_data():
    # Read data
    df = pd.read_csv('./Data/new-york-comments.csv', low_memory=False)

    # Get key words from the comments
    df['key_words'] = df['Comment'].str.findall(r'\w{3,}').str.join(' ')

    # Get the key words from the comments
    df['key_words'] = df['key_words'].str.lower()

    # Get the key words from the comments
    df['key_words'] = df['key_words'].str.replace(r'(\w)\1{2,}', r'\1')

    # Get the key words from the comments
    nltk.download('vader_lexicon')

    # Get the score for each comment
    df['score'] = df['key_words'].apply(get_sentiment_score)

    # New column with the id
    df['id'] = df.index

    return df


def get_sentiment_score(sentence):
    sid = SentimentIntensityAnalyzer()
    sentiment_dict = sid.polarity_scores(sentence)
    score = sentiment_dict['compound'] * 100
    return score
