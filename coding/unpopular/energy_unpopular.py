import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
#Here we go through the file 'unpopular_songs.csv' and we interpret it. 'latin1' represents the alphabets of western european languages which means we are reading 'unpopular_songs.csv' in english.
df = pd.read_csv("unpopular_songs.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='energy')

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(organized_data['energy'], organized_data['energy'])
plt.xlabel('Title')  # Replace 'Column Names' with a suitable label
plt.ylabel('energy')  # Replace 'Value' with a suitable label
plt.title('Energy graph')
plt.show()
