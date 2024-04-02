import pandas as pd

csv_path = 'augmented_lyrics_theme.csv'
df = pd.read_csv(csv_path)

themes = []
narratives = []
tones = []

for row in df['analysis']:
    # Splitting by 'Theme:', 'Narrative:', and 'Tone:' and stripping leading/trailing spaces
    try:
        theme = row.split('Theme:')[1].split('Narrative:')[0].strip()
        narrative = row.split('Narrative:')[1].split('Tone:')[0].strip()
        tone = row.split('Tone:')[1].strip()
    
        themes.append(theme)
        narratives.append(narrative)
        tones.append(tone)
    except:
        themes.append(None)
        narratives.append(None)
        tones.append(None)
        

df['theme'] = themes
df['narrative'] = narratives
df['tones'] = tones
df = df.drop('analysis', axis=1)
new_csv_path = 'thematic_analysis.csv'
df.to_csv(new_csv_path, index=False)

