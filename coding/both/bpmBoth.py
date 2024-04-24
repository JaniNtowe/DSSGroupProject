import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# reading the CSV file into the program
# combining the two data plots onto one CSV file so that
# the data of the two could be compared depending on whether
# it came from the popular or the unpopular file
songData = pd.read_csv("combinedData.csv")

# plotting the data onto a graph
plt.figure(figsize=(10, 6))
sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True)
# plotting the data on, using the BPM column as the x value
# using whether it came from popular or unpopular file to split the two datas
sns.boxplot(data=songData, x="bpm", y="popularity", color = "#66b3b3", linecolor="#008080", linewidth=.75)
plt.xlabel('BPM')
plt.title('Unpopular vs Popular BPM Box Plot')
plt.savefig('BPM Box Plot')
plt.show()
