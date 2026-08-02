from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and convert numerical values to appropriate types."""
    import csv

    songs = []
    numerical_fields = {'id', 'energy', 'tempo_bpm', 'valence', 'danceability', 'acousticness'}

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in numerical_fields:
                if field in row:
                    if field == 'id' or field == 'tempo_bpm':
                        row[field] = int(row[field])
                    else:
                        row[field] = float(row[field])
            songs.append(row)

    print(f"Loading songs from {csv_path}...")
    print(f"Loaded songs: {len(songs)}")
    print()
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return score with reasons."""
    score = 0.0
    reasons = []

    # Genre match: +2.0 points
    if song.get('genre', '').lower() == user_prefs.get('genre', '').lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match: +1.0 point
    # if song.get('mood', '').lower() == user_prefs.get('mood', '').lower():
    #     score += 1.0
    #     reasons.append("mood match (+1.0)")

    # Energy match: 0 to +1.0 points (linear distance)
    if 'energy' in user_prefs and 'energy' in song:
        energy_diff = abs(float(user_prefs['energy']) - float(song['energy']))
        energy_score = max(0, 1.0 * (1.0 - energy_diff))
        score += energy_score
        reasons.append(f"energy match (+{energy_score:.2f})")

    # Danceability match: 0 to +0.5 points (linear distance)
    if 'danceability' in user_prefs and 'danceability' in song:
        danceability_diff = abs(float(user_prefs['danceability']) - float(song['danceability']))
        danceability_score = max(0, 0.5 * (1.0 - danceability_diff))
        score += danceability_score
        reasons.append(f"danceability match (+{danceability_score:.2f})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k recommendations sorted by score."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
# I learned from the AI coding assistant that sorted() would be better here since it returns a new list. 
# The function called sort() changes the original list, but I would like to keep the original list intact. 