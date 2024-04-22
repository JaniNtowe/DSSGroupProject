#
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
#
# # Read the CSV file into a DataFrame
# df = pd.read_csv("top10s.csv", encoding="latin1")
# plt.close("all")
#
# # Organize the data based on a specific column
# organized_data = df.sort_values(by='bpm')
# titles = organized_data["title"].astype(str)
# bpms = organized_data["bpm"]
# titles = [title.replace('\x92', '’') for title in titles]
# titles = [title.replace('\x93', '"') for title in titles]
# titles = [title.replace('\x94', '"') for title in titles]
# # titles = pd.Categorical(titles)
# print(titles)
#
# # Plot the data
# plt.rcParams['font.family'] = 'Arial'
# plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# sns.scatterplot(data = df, x = titles, y = "bpm")
# sns.regplot(data=df, x=titles, y="bpm", scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'color': 'red'})
# plt.xlabel('Title')
# plt.ylabel('BPM')  # Replace 'Value' with a suitable label
# plt.title('BPM graph')
# plt.xticks(rotation=90)
# plt.show()

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

# Plot the data
plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

# Scatterplot with regression line
sns.regplot(x=list(range(len(titles))), y=bpms, scatter_kws={'s': 10, 'alpha': 0.5}, line_kws={'color': 'red'})

# Set tick labels
plt.xticks(range(len(titles)), titles, rotation=90)

plt.xlabel('Title')
plt.ylabel('BPM')
plt.title('BPM graph')
plt.show()
