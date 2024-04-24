import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Reading the CSV file into the program
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# Plotting the data onto a graph
plt.figure(figsize=(10, 6))
# Plotting the data on, using the danceability column as the x value
sns.boxplot(data=df, x = "danceability", color = "#C1D5F0", linecolor="#A8B5E0", linewidth=.75)
plt.xlabel('Danceability')
plt.title('Unpopular Danceability Box Plot')
plt.savefig('Unpopular Danceability Box Plot')
plt.show()
