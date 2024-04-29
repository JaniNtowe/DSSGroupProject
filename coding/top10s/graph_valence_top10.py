import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("output.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='valence')

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(organized_data['id'], organized_data['valence'])
plt.xlabel('')  # Replace 'Column Names' with a suitable label
plt.ylabel('Valence')  # Replace 'Value' with a suitable label
plt.title('Top10s Valence')
plt.xticks([])
plt.show()