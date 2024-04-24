import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading the csv file into the code
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# plotting the data onto the graph
plt.figure(figsize=(10, 6))
# plotting the data using the BPM data as the x axis
sns.boxplot(data=df, x = "duration_ms", color = "#FF9997", linecolor="#FF7974", linewidth=.75)
plt.xlabel('Duration (seconds)')
plt.title('Unpopular Duration Box Plot')
plt.savefig('Unpopular Duration Box Plot')
plt.show()
