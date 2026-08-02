"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = [
        {"genre": "pop", "mood": "happy", "energy": 0.8}, 
        {"genre": "pop", "mood": "happy", "energy": 0.8, "danceability": 0.8},
        {"genre": "lofi", "mood": "chill", "energy": 0.3, "danceability": 0.2},
        {"genre": "rock", "mood": "intense", "energy": 0.9, "danceability": 0.6},
        {"genre": "pop", "mood": "sad", "energy": 0.9, "danceability": 0.1}
    ]

    user_prefs_names = [
        "Original Profile",
        "High Energy Pop", 
        "Acoustic Chill",
        "Energetic Rock", 
        "Happy But Sad (Edge Case)"
    ]

    for i, prefs in enumerate(user_prefs):
        print(f"User Profile: {user_prefs_names[i]}")
        recommendations = recommend_songs(prefs, songs, k=5)
        print("Top recommendations: ")

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song['title']}")
            print(f"   Artist: {song['artist']}")
            print(f"   Score: {score:.2f}/4.5")
            print(f"   Why: {explanation}")
            print("-"*60)
            print()


if __name__ == "__main__":
    main()
