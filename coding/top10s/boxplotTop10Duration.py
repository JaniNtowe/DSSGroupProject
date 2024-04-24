import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Plotting the data onto a graph
plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.boxplot(data=df, x = "dur", color = "#FF9997", linecolor="#FF7974", linewidth=.75)
plt.xlabel('Duration (seconds)')
plt.title('Top 10s Duration Box Plot')
# Saves the figure into a separate file
plt.savefig('Top10s Duration Box Plot')
plt.show()
