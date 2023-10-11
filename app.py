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
st.write('Find the best restaurants in New York City')
st.write('')

# Search bar
search_term = st.text_input('Search for keywords')

# Search button
if st.button('Search'):
    st.balloons()
    search_result = search.search_keyword(search_term, df)
    search_result = search.higher_score(search_result, df)
    if len(search_result) == 0:
        st.write('No results found')
    else:
        # Show first restaurant in search results and recommended restaurants
        st.write('')
        st.subheader('Best restaurant')

        # Show a table with the restaurant
        st.table(search_result[['RestaurantName', 'Address', 'score']])

        # Recommended restaurants
        st.write('Similar restaurants')
        # Get the index of search_result

        st.write(recommender.recommendations(search_result['id'], cosine_sim, indices, df))