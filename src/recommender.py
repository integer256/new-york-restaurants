import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def create_model(df):

    # Train model with the key words
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df['key_words'])

    # Get the cosine similarity matrix from the key words
    from sklearn.metrics.pairwise import cosine_similarity

    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # Get the cosine similarity matrix from the key words
    indices = pd.Series(df.index)

    return cosine_sim, indices


def recommendations(id, cosine_sim, indices, df):

    # Get the cosine similarity matrix from the key words
    id = indices[indices == id].index[0]

    # Get the cosine similarity matrix from the key words
    similarity_scores = pd.Series(cosine_sim[id]).sort_values(ascending=False)

    # Get the cosine similarity matrix from the key words
    top_10 = list(similarity_scores.iloc[1:11].index)

    # Get the cosine similarity matrix from the key words
    return df.iloc[top_10]
