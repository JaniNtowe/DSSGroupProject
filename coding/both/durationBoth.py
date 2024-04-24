import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
songData = pd.read_csv("fixedCombinedData.csv")

# Plot the data
plt.figure(figsize=(10, 6))
sns.set_palette("Paired")
sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True)
sns.boxplot(data=songData, x="duration", y="popularity", color = "#FF9997", linecolor="#FF7974", linewidth=.75)
plt.xlabel('Duration')
plt.title('Unpopular vs Popular Duration Box Plot')
plt.savefig('Duration Box Plot')
plt.xticks(rotation=90)
plt.show()
