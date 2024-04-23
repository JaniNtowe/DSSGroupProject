import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("unpopular_songs.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='valence')

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(organized_data['valence'], organized_data['valence'])
plt.xlabel('Title')  # Replace 'Column Names' with a suitable label
plt.ylabel('valence')  # Replace 'Value' with a suitable label
plt.title('Valence graph')
plt.show()