import streamlit as st
import pickle
import difflib

# Load the saved data
movies_data = pickle.load(open('movies_data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# App title
st.title('🎬 Movie Recommendation System')

# Text input
movie_name = st.text_input('Enter your favorite movie name:')

if movie_name:
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.subheader('Top 30 Movie Recommendations for you:')
        i = 0
        for movie in sorted_similar_movies:
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            if i < 30:
                st.write(f"{i+1}. {title_from_index}")
                i += 1
    else:
        st.error("No similar movie found. Please check your spelling.")
