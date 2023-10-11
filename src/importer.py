import pandas as pd

def load_data():
    # Read data
    df = pd.read_csv('./Data/new-york-comments.csv', low_memory=False)

    # Get key words from the comments
    df['key_words'] = df['Comment'].str.findall(r'\w{3,}').str.join(' ')

    # Get the key words from the comments
    df['key_words'] = df['key_words'].str.lower()

    # Get the key words from the comments
    df['key_words'] = df['key_words'].str.replace(r'(\w)\1{2,}', r'\1')

    return df

