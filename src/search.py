import requests
from bs4 import BeautifulSoup

# Function to search keywords in comments
def search_keyword(keyword, df):
    keyword = keyword.lower()
    contains_keyword = df['key_words'].str.contains(keyword)
    indices = [i for i, x in enumerate(contains_keyword) if x]
    return indices

def higher_score(indices, df):
    df = df.copy()
    df = df.iloc[indices]
    df = df.sort_values(by=['score'], ascending=False)
    # Return the restaurant with higher score
    return df.iloc[0]
