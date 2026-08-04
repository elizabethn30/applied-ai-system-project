# [Project Title]

## Original Project

**Original Project Name:** Music Recommender Simulation

The original goals of the music recommender simulation project were to learn from a dataset and give you recommendations based on what the model learned. The original music recommender simulation was able to give you recommendations and provide pre-generated reasoning for why they selected a song. 

---

## Title and Summary

This project takes the original music recommender and extends it to provide specific feedback from Gemini. This project matters because the recommender can now tell you why a song was chosen and what exactly made the recommender score the song higher. 

---

## Architecture Overview

The system starts with taking in the user's music preference and goes to the data/songs.csv dataset. After searching and getting songs that the user may like, the songs are then passed to Gemini. Gemini gives back a recommendation and explains exactly why they chose the song. The recommendation and explanation are finally outputted to the user. Each step is logged to show where an error may have occured and allows for verification. 

---

## Setup Instructions

# 1. Create your virtual environment
```
python -m venv .venv
.\venv\Scripts\activate # For Windows
```

# 2. Install Python dependencies
```
pip install -r requirements.txt
```

# 3. Configure environment variables
```
cp .env.example .env
```

# 4. Add your Gemini key
Replace the line saying "your_key_here" with your API key:
```
GEMINI_API_KEY=your_key_here
```

# 5. Run the Music Recommender Simulation
```
python src/main.py
```

---

## Sample Interactions

### Example 1
**Input:** 
I want chill acoustic music
**Output:** 
Retrieved Songs:
  • Sunrise City by Neon Echo (pop, happy)
  • Midnight Coding by LoRoom (lofi, chill)
  • Storm Runner by Voltline (rock, intense)
  • Library Rain by Paper Lanterns (lofi, chill)
  • Gym Hero by Max Pulse (pop, intense)

LLM Recommendation:
Based on the user's request for **"chill acoustic music,"** the best match is:

**Library Rain by Paper Lanterns**

### Analysis and Explanation:
To determine the best match, we evaluate the available songs against the two key terms in the user's request: **"chill"** and **"acoustic."**

1. **Acousticness:** The user specifically asked for acoustic music. 
   - *Library Rain* has the highest **Acousticness score of 0.86** (86%), making it by far the most acoustic track on the list. (For comparison, *Midnight Coding* is the next closest at 0.71, while the pop and rock tracks are all below 0.20).
2. **Mood & Energy:** The user requested "chill" music, which aligns with low energy and a relaxed mood.
   - *Library Rain* features a **"chill" mood** and the lowest **Energy score of 0.35** among all the options. This ensures the song will be calm and unobtrusive, perfectly fitting a relaxed vibe. 

While *Midnight Coding* is also a chill lofi track, *Library Rain* edges it out by having both a slightly more relaxed energy level (0.35 vs. 0.42) and a higher acousticness rating (0.86 vs. 0.71).

### Example 2
**Input:** 
I'm looking for upbeat pop songs
**Output:** 
Retrieved Songs:
  • Sunrise City by Neon Echo (pop, happy)
  • Midnight Coding by LoRoom (lofi, chill)
  • Storm Runner by Voltline (rock, intense)
  • Library Rain by Paper Lanterns (lofi, chill)
  • Gym Hero by Max Pulse (pop, intense)

LLM Recommendation:
Based on the user's request for **"upbeat pop songs,"** the best match is **"Sunrise City" by Neon Echo**.

### Analysis & Explanation:

1. **Genre Match:** The user specifically asked for "pop" songs. Out of the five options, only two fit the pop genre: *Sunrise City* (Neon Echo) and *Gym Hero* (Max Pulse). 
2. **Energy and Mood Match:** While "upbeat" implies high energy, the context of "pop" usually leans toward a positive, happy, or vibrant mood rather than an "intense" workout vibe. 
   - **Sunrise City** has a genre of **pop**, a **happy** mood, and a high **energy** level of **0.82**, making it lively and uplifting without being overwhelmingly aggressive.
   - **Gym Hero**, while also pop, is classified with an **intense** mood and an extreme energy level of **0.93**, which is better suited for working out than a standard upbeat listening session.
   - The other options (*Midnight Coding*, *Storm Runner*, and *Library Rain*) are either the wrong genre (lofi/rock) or have much lower energy levels unsuited for an upbeat request.

Therefore, **Sunrise City** hits the sweet spot of being a true pop song with a high, happy energy level that matches the user's request.

### Example 3
**Input:** 
Recommend something melancholic
**Output:** 
Retrieved Songs:
  • Sunrise City by Neon Echo (pop, happy)
  • Midnight Coding by LoRoom (lofi, chill)
  • Storm Runner by Voltline (rock, intense)
  • Library Rain by Paper Lanterns (lofi, chill)
  • Gym Hero by Max Pulse (pop, intense)

LLM Recommendation:
Based on the user's request for something **melancholic**, the best match from the available songs is **Library Rain by Paper Lanterns**. 

Here is the analysis of why this song fits best:

1. **Mood Match:** The user is looking for a melancholic (sad, reflective, sorrowful) vibe. While none of the songs are explicitly labeled "sad," *Library Rain* has a **"chill"** mood, which often overlaps with low-energy, introspective music. None of the other moods (happy, intense) align with melancholia at all.
2. **Energy Level:** Melancholic music is typically subdued and slow-paced. *Library Rain* has the **lowest energy of all the available songs (0.35)**, making it calm and gentle, which fits the reflective nature of melancholic music.
3. **Acousticness:** Melancholic tracks often rely on organic, warm, and intimate sounds rather than heavy electronic production. *Library Rain* has the **highest acousticness by far (0.86)**, meaning it features natural, acoustic elements that enhance an emotional, moody atmosphere. 

While *Midnight Coding* is also a chill lofi track, its energy is slightly higher (0.42) and its acousticness is lower (0.71), making **Library Rain** the superior choice for a quiet, moody, and melancholic listening experience.

---

## Design Decisions

I built the system this way because I wanted users to get a more personalized reasoning for why a song was recommended to them. I personally really like knowing "why" something happens, so having the LLM explaining their why was a big part as to why I decided on RAG. One tradeoff is that the dataset being used is small, so the model will not be able to recommend a song that the user will 100% love. 

---

## Testing Summary



---

## Reflection
This project taught me that you have to constantly review what the AI suggests to you because you may read the first couple of lines and assume that you have everything you need. However, in those last lines that you miss, you might be including information that is wrong or not what you intended. 