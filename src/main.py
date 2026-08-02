"""
RAG Music Recommender - Command line runner.

Uses Retrieval-Augmented Generation to recommend songs:
1. Retrieves matching songs from CSV based on user input
2. Uses LLM (Google Gemini) to generate personalized recommendations
3. LLM actively uses song attributes in its explanation
"""

import logging
from recommender import load_songs, recommend_songs
from rag import rag_recommend

logger = logging.getLogger(__name__)


def main() -> None:
    songs = load_songs("data/songs.csv")

    # RAG EXTENSION
    test_queries = [
        "I want chill acoustic music",
        "I'm looking for upbeat pop songs",
        "Give me something intense and energetic",
        "I want relaxed jazz vibes",
        "Recommend something melancholic"
    ]

    print("\n" + "="*70)
    print("RAG MUSIC RECOMMENDER SYSTEM")
    print("="*70 + "\n")

    for i, query in enumerate(test_queries, 1):
        print(f"Query {i}: {query}")
        print("-" * 70)

        try:
            recommendation, retrieved_songs = rag_recommend(query, songs, k=5)

            print("\nRetrieved Songs:")
            for song in retrieved_songs:
                print(f"  • {song['title']} by {song['artist']} ({song['genre']}, {song['mood']})")

            print(f"\nLLM Recommendation:\n{recommendation}")

        except Exception as e:
            print(f"Error: {e}")

        print("\n" + "="*70 + "\n")

    # ORIGINAL CODE FOR PROJECT 3 MUSIC RECOMMENDER
    # user_prefs = [
    #     {"genre": "pop", "mood": "happy", "energy": 0.8},
    #     {"genre": "pop", "mood": "happy", "energy": 0.8, "danceability": 0.8},
    #     {"genre": "lofi", "mood": "chill", "energy": 0.3, "danceability": 0.2},
    #     {"genre": "rock", "mood": "intense", "energy": 0.9, "danceability": 0.6},
    #     {"genre": "pop", "mood": "sad", "energy": 0.9, "danceability": 0.1}
    # ]
    #
    # user_prefs_names = [
    #     "Original Profile",
    #     "High Energy Pop",
    #     "Acoustic Chill",
    #     "Energetic Rock",
    #     "Happy But Sad (Edge Case)"
    # ]
    #
    # for i, prefs in enumerate(user_prefs):
    #     print(f"User Profile: {user_prefs_names[i]}")
    #     recommendations = recommend_songs(prefs, songs, k=5)
    #     print("Top recommendations: ")
    #
    #     for i, rec in enumerate(recommendations, 1):
    #         song, score, explanation = rec
    #         print(f"{i}. {song['title']}")
    #         print(f"   Artist: {song['artist']}")
    #         print(f"   Score: {score:.2f}/4.5")
    #         print(f"   Why: {explanation}")
    #         print("-"*60)
    #         print()


if __name__ == "__main__":
    main()
