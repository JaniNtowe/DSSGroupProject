import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading the csv file into the code
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# plotting the data onto the graph
plt.figure(figsize=(10, 6))
# plotting the data using the BPM data as the x-axis
sns.boxplot(data=df, x = "valence", color = "#66b3b3", linecolor="#008080", linewidth=.75)
plt.xlabel('Valence')
plt.title('Unpopular Valence Box Plot')
plt.savefig('Unpopular Valence Box Plot')
plt.show()
