import pandas as pd
import glob
import os

files = os.path.join("", "anime_data*.csv")
files = glob.glob(files)

print("Resultant CSV");
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
print(df)
df.to_csv("anime_data_combined.csv")
