import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def extract_movie_name(user_prompt):
    """
    Uses GPT-3.5-Turbo to extract the most relevant movie name from the user prompt.
    """
    prompt = f"Extract the name of the movie from the following user input: '{user_prompt}'. Only return the movie name and nothing else."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are an AI that extracts movie names from text."},
                      {"role": "user", "content": prompt}],
            max_tokens=20
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return None  # If extraction fails, return None

def generate_summary(movie_details):
    """
    Uses GPT-3.5-Turbo to generate a summary based on structured movie details.
    """
    prompt = (
        f"Title: {movie_details.get('Title', 'N/A')}\n"
        f"IMDb Rating: {movie_details.get('imdbRating', 'N/A')}\n"
        f"Genre: {movie_details.get('Genre', 'N/A')}\n"
        f"Release Date: {movie_details.get('Released', 'N/A')}\n"
        f"Actors: {movie_details.get('Actors', 'N/A')}\n"
        f"Director: {movie_details.get('Director', 'N/A')}\n\n"
        "Provide a professional and engaging summary of this movie."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a movie expert generating summaries."},
                      {"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"🚫 AI Summary Error: {e}"
