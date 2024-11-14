import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
nt = pd.read_csv('netflix.csv')  # Replace with the path to your dataset
# Make sure you have 'nt' dataframe available, you may load it manually or process it before

# Streamlit App title
st.title('Netflix Content Dashboard')

# Sidebar for user inputs
st.sidebar.header('User Inputs')

# Dropdown for selecting content type (Movies or TV Shows)
content_type = st.sidebar.selectbox(
    'Select Content Type',
    ['All', 'Movies', 'TV Shows']
)

# Filter the dataset based on selected content type
if content_type != 'All':
    filtered_data = nt[nt['type'] == content_type]
else:
    filtered_data = nt

# Show basic data info
st.subheader('Basic Dataset Information')
st.write(filtered_data.info())

# Content Distribution (Movies vs TV Shows)
st.subheader('Content Distribution (Movies vs TV Shows)')
content_count = filtered_data['type'].value_counts()
st.bar_chart(content_count)

# Genre Popularity Visualization
st.subheader('Genre Popularity')
# Count the occurrences of each genre in the 'listed_in' column (assuming you split genres into columns)
genre_count = filtered_data[['listed_in']].apply(lambda x: x.str.split(',')).explode('listed_in').value_counts()
genre_count = genre_count.reset_index()
genre_count.columns = ['Genre', 'Count']
st.bar_chart(genre_count.set_index('Genre')['Count'])

# Ratings Distribution Visualization
st.subheader('Ratings Distribution')
rating_count = filtered_data['rating'].value_counts()
st.bar_chart(rating_count)

# Duration Analysis
st.subheader('Duration Analysis')
# For Movies, analyze duration
if content_type == 'Movies' or content_type == 'All':
    movie_duration = filtered_data[filtered_data['type'] == 'Movie']['duration'].str.extract('(\d+)').astype(float)
    st.write('Average Movie Duration:', movie_duration.mean().values[0])
    st.write('Min Movie Duration:', movie_duration.min().values[0])
    st.write('Max Movie Duration:', movie_duration.max().values[0])

# TV Shows Season Analysis
if content_type == 'TV Shows' or content_type == 'All':
    tv_seasons = filtered_data[filtered_data['type'] == 'TV Show']['duration'].str.extract('(\d+)').astype(float)
    st.write('Average Number of Seasons for TV Shows:', tv_seasons.mean().values[0])
    st.write('Min Number of Seasons for TV Shows:', tv_seasons.min().values[0])
    st.write('Max Number of Seasons for TV Shows:', tv_seasons.max().values[0])

# Interactive plot for Ratings vs Duration (For Movies)
if content_type == 'Movies' or content_type == 'All':
    st.subheader('Ratings vs Movie Duration')
    sns.scatterplot(x='duration', y='rating', data=filtered_data[filtered_data['type'] == 'Movie'])
    st.pyplot()

# Footer
st.write("Dashboard built using Streamlit")
