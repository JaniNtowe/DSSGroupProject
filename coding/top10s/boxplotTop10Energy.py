import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Plotting the data onto a graph
plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.boxplot(data=df, x = "nrgy", color = "#BFDAA4", linecolor="#7B8D6A", linewidth=.75)
plt.xlabel('Energy')
plt.title('Top 10s Energy Box Plot')
# Saving the graph into a separate file
plt.savefig('Top10s Energy Box Plot')
plt.show()
