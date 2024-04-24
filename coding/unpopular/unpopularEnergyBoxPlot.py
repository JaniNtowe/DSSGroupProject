import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading the CSV file into the program
df = pd.read_csv("unpopular_songsFixed.csv", encoding="latin1")
plt.close("all")

# plotting the data onto a graph
plt.figure(figsize=(10, 6))
# plotting the data on, using the BPM column as the x value
sns.boxplot(data=df, x = "energy", color = "#BFDAA4", linecolor="#7B8D6A", linewidth=.75)
plt.xlabel('Energy')
plt.title('Unpopular Energy Box Plot')
plt.savefig('Unpopular Energy Box Plot')
plt.show()
