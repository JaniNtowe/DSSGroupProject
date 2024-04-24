import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading the CSV file into the program
# combining the two data plots onto one CSV file so that
# the data of the two could be compared depending on whether
# it came from the popular or the unpopular file
songData = pd.read_csv("fixedCombinedData.csv")

# plotting the data onto a graph
plt.figure(figsize=(10, 6))
sns.boxplot(data=songData, x="liveness", y="popularity", color = "#C2B4E2", linecolor="#996FD6", linewidth=.75)
plt.xlabel('Liveliness')
plt.title('Unpopular vs Popular Liveliness Box Plot')
plt.savefig('Liveliness Box Plot')
plt.show()
