# Human Evaluation Testing

| Test Input | Evaluation Criteria | Result |
|---|---|---|
| "I want chill acoustic music" | Retrieved songs have correct mood | Pass |
| "I'm looking for upbeat pop songs" | LLM explains using the correct attributes and cites each song specifically | Pass |
| Empty input | Should tell user to input preference; Returns songs from multiple genres but lets you know that you did not input a preference | Pass |
| "345" | LLM should ask for user input in words; Instead returns song recommendation based on whether the song has one of the digits in its individual feature scores | Fail |
| "Recommend something melancholic" | LLM gives correct comparison for each of the 5 retrieved songs | Pass |

4 of the 5 tests passed. Confidence score was around 0.8. The AI did not know what to properly do when given an input of integers. However, the AI still handled it well by returning an answer that made sense based on the context. 