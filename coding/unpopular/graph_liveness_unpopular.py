import pandas as pd
import matplotlib.pyplot as plt
#import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='liveness')

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(organized_data['track_name'], organized_data['liveness'])
plt.xlabel('')  # Replace 'Column Names' with a suitable label
plt.ylabel('liveliness')  # Replace 'Value' with a suitable label
plt.title('Unpopular Liveliness')
plt.xticks([])
plt.show()