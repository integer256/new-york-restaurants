import streamlit as st
import sys
sys.path.append("./src")

import importer
import recommender
import search


df = importer.load_data()
cosine_sim, indices = recommender.create_model(df)

# Title
st.title('New York City Restaurant Recommender')

# Subtitle
st.subheader('Find the best restaurants in New York City')

# Search bar
search_term = st.text_input('Search for a restaurant')

# Search button
if st.button('Search'):
    indices = search.search_keyword(search_term, df)
    if len(indices) == 0:
        st.write('No results found')
    else:
        for i in indices:
            st.write(df.iloc[i]['RestaurantName'])