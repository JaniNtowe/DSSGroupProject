import pandas as pd
import matplotlib.pyplot as plt
#import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='dur')

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(organized_data['title'], organized_data['dur'])
plt.xlabel('Title')
plt.ylabel('Duration')
plt.title('Duration graph')
plt.xticks([])
plt.show()