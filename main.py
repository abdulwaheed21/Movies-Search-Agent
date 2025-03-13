import streamlit as st
import time
from search_apis import fetch_movie_details, search_youtube_trailer
from language_model import extract_movie_name, generate_summary

st.set_page_config(page_title="🎬 AI Movie Research Assistant", layout="centered")

st.markdown("""
    <h1 style='text-align: center;'>🎬 AI Movie Research Assistant</h1>
    <p style='text-align: center;'>Ask about any movie, and I will provide details, trailers, and expert responses.</p>
    <hr>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about a movie..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Extract movie name using AI
    movie_name = extract_movie_name(prompt)

    if not movie_name:
        response = "🤔 I couldn't detect a movie title. Please specify."
    else:
        # Fetch Movie Data
        movie_details = fetch_movie_details(movie_name)
        trailer_title, trailer_url = search_youtube_trailer(movie_name)
        ai_summary = generate_summary(movie_details)

        # Format Output
        response = f"🎬 **Title:** {movie_details.get('Title', 'N/A')}\n\n"
        response += f"⭐ **IMDb Rating:** {movie_details.get('imdbRating', 'N/A')}\n\n"
        response += f"🎭 **Genre:** {movie_details.get('Genre', 'N/A')}\n\n"
        response += f"📅 **Release Date:** {movie_details.get('Released', 'N/A')}\n\n"
        response += f"🎭 **Actors:** {movie_details.get('Actors', 'N/A')}\n\n"
        response += f"🎬 **Director:** {movie_details.get('Director', 'N/A')}\n\n"
        response += f"🎥 **Trailer:** [{trailer_title}]({trailer_url})\n\n"
        response += f"📝 **Summary:** {ai_summary}\n\n"

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
