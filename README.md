# Genius API & Web Scraping to get Lyrics

Process:
1. Get artist IDs
2. Get song URLs
3. Scrape lyrics

## Annotating Theme, Mood, Style, Tone, and Narrative

Use Mistral API with Langchain for annotation. Example prompt for getting style:

```plaintext
Question: {question}

Lyrics: 
{lyric}

Answer in ONLY 3 words, separated by comma.
Never explain. No need to provide an explanation. 
```

## LLM API Cost
Around 300 input tokens per lyric annotation request.
14000*350*3  = 14,700,000

-> around $4 spent with Mistral 7B

## Usage 

Fine tuning llm models for
Song classification
Based on theme, mood, style
Lyrics Generation
With parameters on these theme, mood, style, etc.
Recommendation system

