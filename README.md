# AI-Powered-Music-Recommender-System
An AI-driven music recommendation system that suggests songs based on user input, genre preferences, and trending hits. It integrates with Spotify API to fetch album covers, song links, and trending playlists. Built using Streamlit, Python, and Machine Learning for an interactive experienc


Features
✅ Song Recommendations: Get AI-powered recommendations based on song similarity.
✅ Genre-Based Filtering: Find songs matching your favorite genre.
✅ Spotify Integration: Fetch album covers and play songs directly on Spotify.
✅ Trending Songs: Stay updated with the latest hits from "Today's Top Hits" Spotify playlist.
✅ Discover New Music: Get random song suggestions to explore new artists.
✅ Like & Leaderboard: Save your favorite songs and see community picks.
✅ Coming Soon: Voice Search feature to find songs using voice commands!

🛠️ Tech Stack
#Python 🐍
#Streamlit 🎨 (for UI)
#Spotipy (Spotify API) 🎵
#Machine Learning (TF-IDF & Cosine Similarity) 🤖
#Pandas & Scikit-Learn 📊

🎯 How It Works?
#Load Dataset: Uses a pre-trained dataset (df.pkl) containing songs, artists, and genres.
#Build Similarity Model: Computes song similarity using TF-IDF vectorization and cosine similarity.
#Fetch Spotify Data: Uses Spotify API to get album covers, song links, and trending playlists.
#Streamlit UI: Provides an interactive web-based interface for users to get recommendations.

🚀 Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/Music_Recommender_System.git
cd Music_Recommender_System
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Get Spotify API Credentials
#Go to Spotify Developer Dashboard
#Create an app & get Client ID and Client Secret
#Replace them in app.py:
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
4️⃣ Run the Application
streamlit run app.py


🔍 Recommendations
🛠 Troubleshooting & Common Errors
❌ AttributeError: 'NoneType' object has no attribute 'format'
🔹 Fix: This happens when an album cover is missing. The code now includes a default fallback image.

❌ Spotify API 404 Error
🔹 Fix: Ensure your API keys are correct and have access to playlists & tracks.

❌ Pickle File Not Found
🔹 Fix: Ensure df.pkl exists. You can create one by scraping song data or using an existing dataset.



🏆 Author & Credits
🎤 Developed by Aryaman Garg
