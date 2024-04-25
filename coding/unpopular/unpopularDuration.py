import pandas as pd
import matplotlib.pyplot as plt
#import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='dur')

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(organized_data['title'], organized_data['dur'])
plt.xlabel('Duration (seconds)')
plt.ylabel('Unpopular Duration')
plt.title('Unpopular Duration graph')
plt.show()