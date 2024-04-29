import pandas as pd
import matplotlib.pyplot as plt
# import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='duration_ms')


def second_to_min(seconds):
    minutes = seconds / 60
    return minutes


# Plot the data
organized_data['duration_minutes'] = organized_data['duration_ms'].apply(second_to_min)
plt.figure(figsize=(10, 6))
plt.bar(organized_data['track_name'], organized_data['duration_minutes'])
plt.xlabel('')
plt.ylabel('Duration (min)')
plt.title('Unpopular Duration')
plt.xticks([])
plt.show()