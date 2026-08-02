# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
SongRecs
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

The recommender is designed to take in the user's preferences and give back 5 songs that best match what you like. 

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model takes into account the genre, mood, energy, and danceability features of a song. The model then scores each feature individually. To give a song a score, the model compares it to what the user likes and finds out how far apart the difference for each feature's score is. If the difference is minimal, a certain number of points are added. If the difference is large, less or no points are added. One of the limits is that the genre is the most heavily emphasized feature here. 

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

There are 18 songs in the dataset. There were originally 10 songs, but 8 songs were added as well. Some of the represented genres are pop, rock, lofi, jazz, hip-hop, country, and classical. One limit is that there is no feature that measures the amount of instrumentals in the song. Some users may want to listen to songs with only instrumentals, but then they get recommended lyrical pop songs instead due to their other preferences. 
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system gives reasonable results for lofi and chill music. It takes into account the mood and low-energy features. The recommendations matched my intuition for the chill categories. I think the scoring captures the mood well. 

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I discovered during my experiements is that the system heavily values genre over any other feature. According to the AI coding assistant, almost 60% of the score is based on genre alone. This will lead to users getting recommended songs that are in their preferred genre, so the user will not be exposed to that much new music. 
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

There were four user profiles tested, excluding the "Original Profile" that was already there. The profiles were happy dancing pop, chill and low-energy, energetic rock, and an edge case with high energy but sad mood. In the recommendations, I mainly looked at what songs kept appearing as this would give me a clue as to what was being emphasized in the system. I was surprised by how the same song "Gym Hero" appeared in 3 out of the 4 profiles. However, this does go along with how the system significantly prioritizes genre over anything else. 

High Energy Pop profile likes pop music with energy, while Acoustic Chill prefers low energy. 
Acoustic Chill prefers lofi music, while Energetic Rock likes rock and metal genres. 
Both High Energy Pop and Energetic Rock like listening to energetic music, but High Energy Pop profile likes pop music, while Energetic Rock would rather listen to rock and metal.  
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

A feature that I would want to add is giving negative scores if a feature does not match. For example, if the user wants lofi genre music, then rock genre songs will get -2.0 for their genre score. A way to improve diversity among the top results would be to change the weight of the features. I would also like to add more features into consideration. 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment was coming up with the "Algorithm Recipe" and trying to come up with how I wanted the program to recommend songs. AI tools helped me a lot with coming up with math formulas to calculate the amount of points a song should get. I did need to double-check AI when it would try to add in a more complicated step than what I needed. It surprised me that the formula I decided to go with was just a linear equation. I thought it would be much more complicated, but it made me realize how important the fundamentals are. If I were to extend the project, I would want to include more features in the calculations and cut back on how much the system emphasized genre. 