import csv
import pandas as pd
import os

csv_list = []
dir = '.'
column_names = ['index', 'artist', 'lyrics']


for csv_file in os.listdir(dir):
    print(csv_file)
    if csv_file.endswith('.csv'):
        print(csv_file)
        file_path = os.path.join(dir, csv_file)
        csv_list.append(pd.read_csv(file_path))

combined = pd.concat(csv_list, ignore_index = True)

combined.to_csv('lyrics_popular.csv', index=False)


