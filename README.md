# Synthetic Lyrics Dataset with Mistral 7B

## Genius API & Web Scraping to get Lyrics

Process:
1. Get artist IDs
2. Get song URLs
3. Scrape lyrics

## Annotating Theme, Mood, Style, Tone, and Narrative

Use Mistral API with Langchain for annotation. Example prompt for getting style:

```{python} 
template = 
"""
Question: {question}

Lyrics: 
{lyric}

Answer in ONLY 3 words, separated by comma.
Never explain. No need to provide an explanation. 
"""
question = 'What is the style and formality level of the whole text, in three words separated by comma?'
```
Ensure stable output format and quality with prompting

## LLM API Cost
Around 350 input tokens per lyric annotation request.
14000 lyrics x 350 Tok x 3 request groups = 14,700,000

-> around $4 spent with Mistral 7B

## Usage 

Fine tuning llm models for
* Song classification
* Lyrics Generation
* Recommendation system

