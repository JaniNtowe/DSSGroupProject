import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Plotting the data onto a graph
plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.boxplot(data=df, x = "val", color = "#66b3b3", linecolor="#008080", linewidth=.75)
plt.xlabel('Valence')
plt.title('Top 10s Valence Box Plot')
plt.savefig('Top10s Valence Box Plot')
plt.show()
