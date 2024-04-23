import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Reading the CSV file into the program
df = pd.read_csv("unpopular_songs.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='tempo')
bpms = organized_data["tempo"]

# Plotting the data onto a graph
plt.figure(figsize=(10, 6))
# Plotting the data on, using the BPM column as the x value
sns.boxplot(data=organized_data, x = bpms, color = "#66b3b3", linecolor="#008080", linewidth=.75)
plt.xlabel('BPM')
plt.title('Unpopular BPM Box Plot')
plt.savefig('Unpopular BPM Box Plot')
plt.show()
