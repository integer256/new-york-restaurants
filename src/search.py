# Function to search keywords in comments
def search_keyword(keyword, df):
    keyword = keyword.lower()
    contains_keyword = df['key_words'].str.contains(keyword)
    indices = [i for i, x in enumerate(contains_keyword) if x]
    return indices
