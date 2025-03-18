import requests

GENIUS_API_KEY = "QWf6ktkoTBXTAe8kHTrh--W9cuh4ZBFvhtTG6o6NgTvwqi8gKa5_BXKsOPRfZnf6"

def test_genius_api(song_name, artist_name):
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
    search_url = f"https://api.genius.com/search?q={song_name} {artist_name}"
    response = requests.get(search_url, headers=headers)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("Full Response:", data)

        if "response" in data and "hits" in data["response"] and len(data["response"]["hits"]) > 0:
            song_data = data["response"]["hits"][0]["result"]
            print("Extracted Image URL:", song_data.get("song_art_image_url", "No Image Found"))
        else:
            print("⚠️ No image found in API response.")
    else:
        print("❌ Genius API Error:", response.json())

# Test with a song
test_genius_api("Shape of You", "Ed Sheeran")
