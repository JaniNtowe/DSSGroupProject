import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv("top10s.csv", encoding="latin1")
plt.close("all")

# Organize the data based on a specific column
organized_data = df.sort_values(by='bpm')
titles = organized_data["title"].astype(str)
bpms = organized_data["bpm"]
titles = [title.replace('\x92', '’') for title in titles]
titles = [title.replace('\x93', '"') for title in titles]
titles = [title.replace('\x94', '"') for title in titles]
# titles = pd.Categorical(titles)
print(titles)

# Plot the data
plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
sns.boxplot(data=organized_data, x = bpms)
plt.xlabel('Title')
plt.title('BPM Box Plot')
plt.savefig('Top10s BPM Box Plot')
plt.show()
