from select import select
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_img(movie_id):
    response = requests.get('http://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    rmovie_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x: x[1])[1:6]
    recommendation = []
    rec_image = []
    for i in rmovie_list:
        movie_id = movie_list.iloc[i[0]]['movie_id']
        recommendation.append(movie_list.iloc[i[0]]['title'])
        rec_image.append(fetch_img(movie_id))
    return recommendation,rec_image

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movie_list = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Movies-Recommender System")
selected_Movie_Name = st.selectbox(
    'Select Your Movie :',
    movie_list['title'].values)
if st.button("Recommend"):
    recommended_movie,posters = recommend(selected_Movie_Name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(posters[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(posters[1])
    with col3:
        st.text(recommended_movie[2])
        st.image(posters[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(posters[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(posters[4])    

    