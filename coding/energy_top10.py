import pandas as pd
import matplotlib.pyplot as plt
#import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='nrgy')

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(organized_data['title'], organized_data['nrgy'])
plt.xlabel('Title')  # Replace 'Column Names' with a suitable label
plt.ylabel('nrgy')  # Replace 'Value' with a suitable label
plt.title('NRGY graph')
plt.show()