import pandas as pd
import matplotlib.pyplot as plt
#import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='live')

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(organized_data['title'], organized_data['live'])
plt.xlabel('Title')  # Replace 'Column Names' with a suitable label
plt.ylabel('liveliness')  # Replace 'Value' with a suitable label
plt.title('Liveliness Graph')
plt.xticks([])
plt.show()