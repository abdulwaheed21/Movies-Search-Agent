import requests
import os
from dotenv import load_dotenv
from googlesearch import search

# Load API keys
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_movie_details(title):
    """
    Fetch movie details from OMDb API. If not found, use Google Search.
    """
    base_url = "http://www.omdbapi.com/"
    params = {"apikey": OMDB_API_KEY, "t": title}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            return data  # ✅ Movie found

    google_result = google_movie_check(title)
    return {"Title": google_result, "Exists": True} if google_result else None

def google_movie_check(query):
    """
    Use Google Search to find IMDb or Wikipedia page.
    """
    try:
        search_results = search(f"{query} site:imdb.com OR site:wikipedia.org", num_results=3)
        for link in search_results:
            if "imdb.com/title" in link or "wikipedia.org/wiki" in link:
                return query  # ✅ Assume movie is real
    except Exception:
        pass
    return None

def search_youtube_trailer(query):
    """
    Fetches a YouTube trailer link and title.
    """
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": f"{query} official trailer",
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "maxResults": 1
    }
    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "items" in data and data["items"]:
            video = data["items"][0]
            return video["snippet"]["title"], f"https://www.youtube.com/watch?v={video['id']['videoId']}"
    return "Not Found", None
