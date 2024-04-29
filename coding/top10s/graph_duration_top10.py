import pandas as pd
import matplotlib.pyplot as plt
# import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("output.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='duration_ms')


def milli_to_minutes(milliseconds):
    seconds = milliseconds / 1000
    minutes = seconds / 60
    return minutes


# Plot the data
organized_data['duration_minutes'] = organized_data['duration_ms'].apply(milli_to_minutes)
plt.figure(figsize=(10, 6))
plt.bar(organized_data['id'], organized_data['duration_minutes'])
plt.xlabel('')
plt.ylabel('Duration (min)')
plt.title('Top10s Duration')
plt.xticks([])
plt.show()
