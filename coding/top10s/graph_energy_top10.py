import pandas as pd
import matplotlib.pyplot as plt
#import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("output.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='energy')

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(organized_data['id'], organized_data['energy'])
plt.xlabel('')  # Replace 'Column Names' with a suitable label
plt.ylabel('Energy')  # Replace 'Value' with a suitable label
plt.title('Top10s Energy')
plt.xticks([])
plt.show()