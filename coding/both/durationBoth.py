import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
songData = pd.read_csv("fixedCombinedData.csv")

# Plot the data
plt.figure(figsize=(10, 6))
sns.set_palette("Paired")
sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True)
sns.boxplot(data=songData, x="danceability", y="popularity", color = "#C1D5F0", linecolor="#B4CBF0", linewidth=.75)
plt.xlabel('Danceability')
plt.title('Unpopular vs Popular Danceability Box Plot')
plt.savefig('Danceability Box Plot')
plt.xticks(rotation=90)
plt.show()
