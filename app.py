

# import pickle
# import streamlit as st
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import requests
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Replace with your Spotify API credentials
# SPOTIFY_CLIENT_ID = ""
# SPOTIFY_CLIENT_SECRET = ""

# # Initialize Spotify API client
# client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# # Function to fetch album cover from Spotify
# def get_song_album_cover_url(song_name, artist_name):
#     try:
#         search_query = f"track:{song_name} artist:{artist_name}"
#         results = sp.search(q=search_query, type="track", limit=1)

#         if results and results["tracks"]["items"]:
#             track = results["tracks"]["items"][0]
#             images = track["album"]["images"]
#             if images:
#                 return images[0]["url"]  # Get highest resolution image

#         return "https://i.postimg.cc/0QNxYz4V/social.png"  # Default image if not found
#     except Exception as e:
#         print(f"Error fetching album cover from Spotify: {e}")
#         return "https://i.postimg.cc/0QNxYz4V/social.png"

# # Load dataset
# try:
#     music = pickle.load(open('df.pkl', 'rb'))
#     music.columns = music.columns.str.strip().str.lower()

#     if 'song-name' in music.columns:
#         music.rename(columns={'song-name': 'song'}, inplace=True)

#     if 'text' not in music.columns:
#         if {'song', 'singer/artists', 'genre'}.issubset(music.columns):
#             music['text'] = music['song'] + " " + music['singer/artists'] + " " + music['genre']
#         else:
#             st.error("⚠️ 'text' column is missing and cannot be created!")
#             st.stop()
    
#     music['text'] = music['text'].fillna('').astype(str)
#     pickle.dump(music, open('df.pkl', 'wb'))

# except Exception as e:
#     st.error(f"⚠️ Error loading dataset: {e}")
#     st.stop()

# # Load or Generate Similarity Matrix
# try:
#     similarity = pickle.load(open('similarity.pkl', 'rb'))
#     if similarity is None or not hasattr(similarity, "shape"):
#         raise ValueError("Invalid similarity matrix.")
# except:
#     st.warning("⚠️ Similarity matrix not found. Regenerating it now...")

#     tfidvector = TfidfVectorizer(analyzer='word', stop_words='english')
#     matrix = tfidvector.fit_transform(music['text'])
#     similarity = cosine_similarity(matrix)

#     with open('similarity.pkl', 'wb') as f:
#         pickle.dump(similarity, f)

#     st.success("✅ Similarity matrix successfully generated!")

# # Recommendation function
# def recommend(song):
#     try:
#         if song not in music['song'].values:
#             return [], []

#         index = music[music['song'] == song].index[0]
#         distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#         recommended_music_names = []
#         recommended_music_posters = []

#         for i in distances[1:6]:  # Top 5 recommendations
#             artist = music.iloc[i[0]]['singer/artists']
#             song_name = music.iloc[i[0]]['song']
#             poster_url = get_song_album_cover_url(song_name, artist)  # Fetch correct poster

#             recommended_music_posters.append(poster_url)
#             recommended_music_names.append(song_name)

#         return recommended_music_names, recommended_music_posters

#     except Exception as e:
#         st.error(f"⚠️ Error in recommendation function: {e}")
#         return [], []

# # Custom CSS for better UI
# st.markdown("""
#     <style>
#         body {
#             background-color: #121212;
#             color: white;
#         }
#         .title {
#             text-align: center;
#             font-size: 40px;
#             font-weight: bold;
#             color: #1DB954;
#         }
#         .song-box {
#             background: rgba(255, 255, 255, 0.1);
#             padding: 15px;
#             border-radius: 10px;
#             box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .song-box img {
#             width: 100%;
#             border-radius: 10px;
#         }
#         .song-box:hover {
#             transform: scale(1.05);
#             transition: 0.3s ease-in-out;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Streamlit UI
# st.markdown('<h1 class="title">🎵 Music Recommender System</h1>', unsafe_allow_html=True)

# if 'song' in music.columns:
#     music_list = music['song'].dropna().unique()
#     selected_song = st.selectbox("Type or select a song:", music_list)

#     if st.button('Show Recommendation'):
#         recommended_music_names, recommended_music_posters = recommend(selected_song)
        
#         if recommended_music_names:
#             col1, col2, col3 = st.columns(3)

#             for i in range(len(recommended_music_names)):
#                 with (col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3):
#                     with st.container():
#                         st.markdown(f'<div class="song-box">', unsafe_allow_html=True)
#                         st.image(recommended_music_posters[i], width=200, caption=recommended_music_names[i])
#                         st.markdown('</div>', unsafe_allow_html=True)
#         else:
#             st.error("⚠️ No recommendations found. Try another song.")
# else:
#     st.error("⚠️ Dataset does not contain 'song' column.")  


import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import random
import time

# 🎵 Spotify API Credentials (Replace with your own)
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"

# 🎧 Initialize Spotify API Client
try:
    client_credentials_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
except Exception as e:
    st.error(f"⚠️ Spotify API Initialization Error: {e}")
    st.stop()

# 📁 Load Dataset
try:
    music = pickle.load(open("df.pkl", "rb"))
    music.columns = music.columns.str.strip().str.lower()
    if "song-name" in music.columns:
        music.rename(columns={"song-name": "song"}, inplace=True)

    # Ensure required columns exist
    required_columns = {"song", "singer/artists", "genre"}
    if not required_columns.issubset(music.columns):
        st.error(f"⚠️ Missing required columns: {required_columns - set(music.columns)}")
        st.stop()
except Exception as e:
    st.error(f"⚠️ Error loading dataset: {e}")
    st.stop()

# 🔍 Generate Similarity Matrix if not available
try:
    similarity = pickle.load(open("similarity.pkl", "rb"))
except:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    st.warning("⚠️ Similarity matrix not found. Generating...")
    tfidvector = TfidfVectorizer(analyzer="word", stop_words="english")
    matrix = tfidvector.fit_transform(
        music["song"] + " " + music["singer/artists"] + " " + music["genre"]
    )
    similarity = cosine_similarity(matrix)
    pickle.dump(similarity, open("similarity.pkl", "wb"))
    st.success("✅ Similarity matrix generated!")

# 🎵 Fetch Album Cover from Spotify
def get_song_album_cover_url(song_name, artist_name):
    try:
        results = sp.search(q=f"track:{song_name} artist:{artist_name}", type="track", limit=1)
        if results and results["tracks"]["items"]:
            return results["tracks"]["items"][0]["album"]["images"][0]["url"]
    except Exception as e:
        print(f"⚠️ Error fetching album cover: {e}")
        return None  # Return None explicitly if no image found

# 🔗 Fetch Spotify Link
def get_spotify_link(song_name, artist_name):
    try:
        results = sp.search(q=f"track:{song_name} artist:{artist_name}", type="track", limit=1)
        if results["tracks"]["items"]:
            return results["tracks"]["items"][0]["external_urls"]["spotify"]
    except:
        return None

# 🔍 Recommendation System
def recommend(song, genre_filter=None):
    try:
        if song not in music["song"].values:
            return []
        index = music[music["song"] == song].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_songs = []

        for i in distances[1:10]:  # Top recommendations
            song_data = music.iloc[i[0]]
            if genre_filter and song_data["genre"] != genre_filter:
                continue
            recommended_songs.append(song_data["song"])

        return recommended_songs[:5]  # Limit to 5
    except Exception as e:
        st.error(f"⚠️ Error in recommendation function: {e}")
        return []

# 🔥 Get Trending Songs (Fixed)
def get_trending_songs():
    try:
        results = sp.search(q="Today's Top Hits", type="playlist", limit=1, market="US")
        if results["playlists"]["items"]:
            playlist_id = results["playlists"]["items"][0]["id"]
            tracks = sp.playlist_tracks(playlist_id, limit=5)
            return [track["track"]["name"] for track in tracks["items"] if track["track"]]
        return ["No trending songs found"]
    except Exception as e:
        print(f"⚠️ Error fetching trending songs: {e}")
        return ["Error fetching trending songs"]

# 🎶 Streamlit UI
st.title("🎵 AI-Powered Music Recommender")

# 🎶 Genre Filter
genres = music["genre"].dropna().unique().tolist()
selected_genre = st.selectbox("🎶 Select Genre (Optional)", ["All"] + genres)

# 🎤 Select Song
selected_song = st.selectbox("🎤 Type or Select a Song", music["song"].dropna().unique())

# 🔍 Show Recommendations Button
if st.button("🔍 Show Recommendations"):
    with st.spinner("🎶 Finding the best songs for you..."):
        time.sleep(2)  # Simulate Loading
        recommended_songs = recommend(
            selected_song, genre_filter=None if selected_genre == "All" else selected_genre
        )

        if recommended_songs:
            for song in recommended_songs:
                artist = music[music["song"] == song]["singer/artists"].values[0]
                image_url = get_song_album_cover_url(song, artist)

                # ✅ FIX: Ensure image_url is valid before displaying
                if not image_url:
                    image_url = "https://i.postimg.cc/0QNxYz4V/social.png"  # Default image

                spotify_url = get_spotify_link(song, artist)

                st.image(image_url, width=200)
                st.write(f"🎵 **{song}** - {artist}")
                if spotify_url:
                    st.markdown(f"[🎧 Listen on Spotify]({spotify_url})", unsafe_allow_html=True)
        else:
            st.error("⚠️ No recommendations found! Try another song.")

# 🔥 Trending Songs
st.subheader("🔥 Trending Songs")
trending_songs = get_trending_songs()
st.write(", ".join(trending_songs))

# 🎲 Discover New Song
if st.button("🎲 Discover New Song"):
    random_song = random.choice(music["song"].values)
    st.success(f"🔄 Try listening to **{random_song}**")

# 🎙️ Voice Search (Placeholder)
st.subheader("🎙️ Voice Search (Coming Soon!)")

# 👍 Like/Dislike System
st.subheader("❤️ Liked Songs")
liked_songs = st.session_state.get("liked_songs", [])

if liked_songs:
    st.write(", ".join(liked_songs))

if st.button("❤️ Like This Song"):
    liked_songs.append(selected_song)
    st.session_state["liked_songs"] = liked_songs

# 🏆 Leaderboard
st.subheader("🏆 Community Picks")
if "liked_songs" in st.session_state:
    st.write(", ".join(st.session_state["liked_songs"][:5]))  # Show top 5
