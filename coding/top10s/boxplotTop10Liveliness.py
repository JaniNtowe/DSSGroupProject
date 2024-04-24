import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Plotting the data onto a graph
plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.boxplot(data=df, x = "live", color = "#C2B4E2", linecolor="#996FD6", linewidth=.75)
plt.xlabel('Liveliness')
plt.title('Top 10s Liveliness Box Plot')
# Saves the figure into a separate file
plt.savefig('Top10s Liveliness Box Plot')
plt.show()
