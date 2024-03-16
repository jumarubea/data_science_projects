import pandas as pd
import matplotlib.pyplot as plt

#reading the file and storing it in netflix_df
netflix_df = pd.read_csv('netflix_data.csv')

#removing "TV Show" in type column
is_tv_show = netflix_df['type'] == 'TV Show'
netflix_subset = netflix_df.drop(netflix_df[is_tv_show].index)
print(netflix_subset.head(5))   # 5 rows of netflix_subset

#removing unwanted columns
columns_to_keep = ["title", "country", "genre", "release_year", "duration"]
netflix_movies = netflix_subset[columns_to_keep]
print(netflix_movies.head(5))   # 5 rows of netflix_movies  

is_shorter_than_60 = netflix_movies['duration'] < 60
short_movies = netflix_movies[is_shorter_than_60]
print(short_movies.head(30))   # 30 rows of short_movies   

# investigation says, documentaries, children, standup,are most shorter netflix movies and assigning colors to them
colors = []
for color, gen in netflix_movies.iterrows(): # iterrows() returns the index and the row data as a Series of dataframes
    if gen['genre'] == 'Children':
        colors.append('yellow')
    elif gen['genre'] == 'Documentaries':
        colors.append('hotpink')
    elif gen['genre'] == 'Stand-Up':
        colors.append('blue')
    else:
        colors.append('green')
# print(colors[0:10])

# defining the figure size, x-axis, y-axis,       
plt.figure(num=1, label = 'fig', figsize= (8, 12))
x_axis = netflix_movies['release_year']
y_axis = netflix_movies['duration']

# adding title, x-axis label, y-axis label in the plot
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')

# plotting the scatter plot
plt.scatter(x_axis, y_axis, color = colors)

# adding legend to the plot
handles = []
labels = ['Children', 'Documentaries', 'Stand-Up', 'Others']
colors = ['yellow', 'hotpink', 'blue', 'green']

# create a plot instance for each category you want to display in the legend
for label, color in zip(labels, colors):
    handles.append(plt.scatter([], [], c=color, label=label))

plt.legend(handles, labels)
plt.show()
