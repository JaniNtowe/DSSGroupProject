import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Plotting the data onto a graph
plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.boxplot(data=df, x = "dnce", color = "#C1D5F0", linecolor="#B4CBF0", linewidth=.75)
plt.xlabel('Danceability')
plt.title('Top 10s Danceability Box Plot')
# Saves the figure into a separate file
plt.savefig('Top10s Danceability Box Plot')
plt.show()
