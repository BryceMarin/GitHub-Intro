import pandas as pd
import matplotlib.pyplot as plt

### Data Manipulation
# read in the data - already deleted extraneous rows
file_path = "BadViz/SIPRI-Milex-data-1992-2021-notutf8.csv"
df = pd.read_csv(file_path)
# remove extraneous columns
df.pop("Unnamed: 1")
df.pop("Notes")
# transpose the dataset so the years are the row index
df = df.transpose()
# make the countries the column names and drop that extra row
country_col = df.iloc[0].tolist()
df.columns = country_col
df = df.drop("Country")
# turn index into datetime strings for graph
df.index = pd.to_datetime(df.index)
# scale the data
df_scaled = (df/1000)

### Setting Up Two Dataframes for Graphing
# Dataframe without United States
dfwo_US = df_scaled.loc[:, df_scaled.columns != "United States of America"]
# Dataframe with only the United States
df_US = df_scaled.loc[:, df_scaled.columns == "United States of America"]

### Graphing
# (called) "normal" color palette taken from: https://tsitsul.in/blog/coloropt/
normal_colors_US = "#b51d14"
normal_colors = ["#4053d3", "#ddb310", "#00beff", "#fb49b0", "#00b25d"]
fig, (ax1, ax2) = plt.subplots(2, sharex = True, constrained_layout = False)
# fig.sup____ is for the entire figure not just the subplots
# x and y allows for little adjustments in position
fig.suptitle("Military Expenditures by Country", y = 0.92)
fig.supxlabel("Year", y = 0.04)
fig.supylabel("Constant 2023 USD in Billions ($)", x = 0.07)
# puts US in one subplot (the one on top)
df_US.plot(ax = ax1, color=normal_colors_US).legend(loc = "upper left")
# puts the other countries in the second subplot
dfwo_US.plot(ax = ax2, color=normal_colors)

plt.subplots_adjust(hspace = 0.074)
# ha = horizontal alignment for when you don't need to be so precise
plt.figtext(0.02, 0.02, "Source: SIPRI Military Expenditure Database", fontsize = 8, 
            ha = "left")
plt.figtext(0.02, 0.05, "*The countries selected had the highest defense spending (in constant 2020 U.S. dollars) from 2017 to 2021", fontsize = 8, ha = "left")
plt.show()
