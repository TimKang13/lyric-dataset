import pandas as pd


#csv1_path = 'augmented_lyrics.csv' 
#csv2_path = 'augmented_lyrics_style.csv'
csv1_path = 'thematic_analysis.csv' 
csv2_path = 'moods_style.csv'  

df1 = pd.read_csv(csv1_path)
print(df1.head)
df2 = pd.read_csv(csv2_path)
print(df2.head)

df1.set_index('index', inplace=True)
df2.set_index('index', inplace=True)

#df1['styles'] = df2['styles']
df1['moods'] = df2['moods']
df1['styles'] = df2['styles']

# combined_df.fillna('', inplace=True)

#combined_csv_path = 'moods_style.csv'  
combined_csv_path = 'lyrics_annotated.csv' 
df1.to_csv(combined_csv_path)


