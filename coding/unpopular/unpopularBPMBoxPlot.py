import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading the csv file into the code
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# organizing the data
organized_data = df.sort_values(by='tempo')
bpms = organized_data["tempo"]

# plotting the data onto the graph
plt.figure(figsize=(10, 6))
# plotting the data using the BPM data as the x axis
sns.boxplot(data=organized_data, x = bpms, color = "#66b3b3", linecolor="#008080", linewidth=.75)
plt.xlabel('BPM')
plt.title('Unpopular BPM Box Plot')
plt.savefig('Unpopular BPM Box Plot')
plt.show()
