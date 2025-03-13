# 🎬 AI Movie Research Assistant

Welcome to the **AI Movie Research Assistant**! This tool helps you search for movies effortlessly. Just type a query, and it will **extract the movie name**, find relevant details (IMDb rating, genre, release date, director, actors), fetch a YouTube trailer, and even **generate a smart AI-powered summary**.

---

## 🚀 Features

✅ **Understands natural language queries** (AI extracts movie name from user input)  
✅ **Finds IMDb, Wikipedia, and Rotten Tomatoes links** (Google Search backup)  
✅ **Fetches YouTube trailer links**  
✅ **Retrieves structured movie data (Title, Genre, Director, Actors, etc.)**  
✅ **Generates AI summaries for movies**  
✅ **Stores session history (tracks user queries & responses)**  
✅ **Chat-style UI with a clean and minimal design**  

---

## 📂 Project Structure

```
movie_search_agent/
│── main.py             # Streamlit GUI
│── search_apis.py      # Fetch IMDb, Wikipedia, and YouTube data
│── language_model.py   # AI-based Name Extraction + Summary (GPT-3.5-Turbo)
│── utils.py            # Session Logging
│── .env                # API Keys Storage
│── requirements.txt    # Required Python Packages
│── README.md           # Project Documentation
```

---

## 📌 Installation & Setup

### 1️⃣ Install Dependencies
Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### 2️⃣ Set Up API Keys
Create a `.env` file in the project folder and add:

```
OMDB_API_KEY=your_omdb_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

**🔹 Replace `your_api_key_here` with your actual API keys.**  

---

### 3️⃣ Run the Assistant

```bash
streamlit run main.py
```

---

## 🔥 Example Usage

### **User Query:**
💬 **"Tell me about the movie where Batman fights the Joker."**

### **AI Output:**
```
🎬 Title: The Dark Knight  

⭐ IMDb Rating: 9.0  

🎭 Genre: Action, Crime, Drama  

📅 Release Date: July 18, 2008  

🎭 Actors: Christian Bale, Heath Ledger, Aaron Eckhart  

🎬 Director: Christopher Nolan  

🎥 Trailer: [Watch Here](https://www.youtube.com/watch?v=EXeTwQWrcwY)  

📝 Summary: The Dark Knight follows Batman as he battles the Joker, a criminal mastermind seeking to create chaos in Gotham. The film explores themes of morality and heroism, with a stunning performance by Heath Ledger.
```

---

## 🛠 Tech Stack

- **Python**
- **Streamlit (for UI)**
- **GPT-3.5-Turbo (OpenAI)**
- **Google Search API**
- **OMDb API**
- **YouTube Data API**
- **JSON-based session logging**

---

## 📌 Future Improvements

✅ **Improve movie recommendations** based on user history  
✅ **Support for TV series** (not just movies)  
✅ **Enhance AI query understanding** for even smarter responses  
✅ **Multi-language support** for global users  


## Contributing

Want to improve this project? Feel free to fork, modify, and send a pull request! 🚀  

If you have **any issues or suggestions**, open an issue, and I’ll be happy to help.  


## 📜 License

This project is **open-source** and free to use. Feel free to modify and enhance it! 🎬🔥  
