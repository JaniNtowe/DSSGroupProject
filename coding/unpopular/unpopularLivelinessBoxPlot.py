import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading the csv file into the code
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# plotting the data onto the graph
plt.figure(figsize=(10, 6))
# plotting the data using the BPM data as the x axis
sns.boxplot(data=df, x = "liveness", color = "#C2B4E2", linecolor="#996FD6", linewidth=.75)
plt.xlabel('Liveliness')
plt.title('Unpopular Liveliness Box Plot')
plt.savefig('Unpopular Liveliness Box Plot')
plt.show()
