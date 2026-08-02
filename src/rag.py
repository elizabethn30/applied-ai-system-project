import logging
import os
from typing import List, Dict, Tuple
from google import genai
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


def retrieve_songs(user_input: str, songs: List[Dict], k: int = 5) -> List[Dict]:
    """
    Retrieve songs matching user input keywords.
    Searches by mood, genre, and title.
    """
    logger.info(f"Retrieving songs for user input: '{user_input}'")

    query_lower = user_input.lower()
    matching_songs = []

    # Search by mood, genre, or title
    for song in songs:
        mood_match = query_lower in song.get('mood', '').lower()
        genre_match = query_lower in song.get('genre', '').lower()
        title_match = query_lower in song.get('title', '').lower()

        if mood_match or genre_match or title_match:
            matching_songs.append(song)

    # If no matches, use default songs
    if not matching_songs:
        logger.warning(f"No songs matched '{user_input}', using default songs")
        matching_songs = songs

    # Return top k
    result = matching_songs[:k]
    logger.info(f"Retrieved {len(result)} songs: {[s['title'] for s in result]}")
    return result


def generate_recommendation(user_input: str, retrieved_songs: List[Dict]) -> str:
    """
    Use LLM (Google Gemini) to generate recommendation using retrieved songs.
    The LLM actively reads song attributes to explain its recommendation.
    """
    logger.info(f"Calling LLM with {len(retrieved_songs)} retrieved songs")

    try:
        # Initialize Gemini API client
        client = genai.Client()

        # Format songs for LLM context
        songs_text = "\n".join([
            f"- {song['title']} by {song['artist']} "
            f"(Genre: {song['genre']}, Mood: {song['mood']}, Energy: {song['energy']}, Acousticness: {song['acousticness']})"
            for song in retrieved_songs
        ])

        # Prompt LLM to use the retrieved songs
        prompt = f"""Based on these songs, recommend the best match for the user's request: "{user_input}"

Available songs:
{songs_text}

Analyze the song attributes and explain which song best matches the request and why. Use specific song characteristics in your explanation."""

        logger.info("Sending prompt to LLM")
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )
        recommendation = response.text

        logger.info(f"LLM response received ({len(recommendation)} chars)")
        return recommendation

    except Exception as e:
        logger.error(f"LLM error: {type(e).__name__}: {e}")
        raise


def rag_recommend(user_input: str, songs: List[Dict], k: int = 5) -> Tuple[str, List[Dict]]:
    """
    Full RAG pipeline: retrieve relevant songs, then use LLM to generate recommendation.

    Returns:
        (recommendation_text, retrieved_songs)
    """
    logger.info(f"Starting RAG pipeline for user input: '{user_input}'")

    try:
        # Step 1: Retrieve matching songs
        retrieved_songs = retrieve_songs(user_input, songs, k)

        # Step 2: Generate recommendation using LLM
        recommendation = generate_recommendation(user_input, retrieved_songs)

        logger.info("RAG pipeline completed successfully")
        return recommendation, retrieved_songs

    except Exception as e:
        logger.error(f"RAG pipeline failed: {type(e).__name__}: {e}")
        raise
