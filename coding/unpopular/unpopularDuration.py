'''import pandas as pd
import matplotlib.pyplot as plt
#import subprocess

# Read the CSV file into a DataFrame
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='duration_ms')

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(organized_data['track_name'], organized_data['duration_ms'])
plt.xlabel('Title')
plt.ylabel('Unpopular Duration')
plt.title('Unpopular Duration graph')
plt.show()'''

#NOT CURRENTLY WORKING
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")

# Assuming there are too many tracks to display all labels, let's limit the number of tracks shown on the x-axis
num_tracks_to_display = 50  # You can adjust this number based on your preference

# Sort the data based on a specific column
organized_data = df.sort_values(by='duration_ms')

# Trim the data to display only a subset of tracks
organized_data = organized_data[:num_tracks_to_display]

# Plot the data
plt.figure(figsize=(15, 8))  # Adjust the figure size as needed
plt.bar(organized_data['track_name'], organized_data['duration_ms'])
plt.xlabel('Title')
plt.ylabel('Unpopular Duration (ms)')
plt.title('Unpopular Duration of Top {} Tracks'.format(num_tracks_to_display))
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
