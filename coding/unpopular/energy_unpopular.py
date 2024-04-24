import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
#Here we go through the file 'unpopular_songs.csv' and we interpret it.
#'latin1' represents the alphabets of western european languages which
#means we are reading 'unpopular_songs.csv' in english.
df = pd.read_csv("unpopular_songs.csv", encoding="latin1")
#this closes all other open figures, in our case, the other plots
plt.close("all")

# Sorts 'df' by the values in the column 'energy'
organized_data = df.sort_values(by='energy')

# Plot the data
#Set the parameters of the plot as (width, height)
plt.figure(figsize=(10, 6))
#this creates a bar graph
#the first 'organized_data['energy']' is the data for the x axis of the bar chart
#the second 'organized_data['energy']' is the data for the height of the bar chart
plt.bar(organized_data['energy'], organized_data['energy'])
#this names the x-axis
plt.xlabel('Title')
#this names the y-axis
plt.ylabel('energy')
#this names the top of the graph
plt.title('Energy graph')
#this makes the graph appear
plt.show()
