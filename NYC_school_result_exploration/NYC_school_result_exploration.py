import pandas as pd
import numpy as np

# creating dataframe from school csv
schools = pd.read_csv('schools.csv')

# best math school in NYC with more than 80% of maximum score 800
math_sorted = schools[['school_name', 'average_math']].sort_values('average_math', ascending=False)


is_atleast_80_percent = math_sorted['average_math'] >= 0.8*800
best_math_schools = math_sorted[is_atleast_80_percent].reset_index(drop=True)

# sorting schools based on total SATs
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name', 'total_SAT']].sort_values('total_SAT', ascending=False).reset_index(drop=True).head(10)

schools= schools.groupby('borough').agg(['count', 'mean', 'std']).round(2)
schools['std'] = schools.std(axis=1)
largest_std_dev = schools[schools['std'] == schools['std'].max()]


largest_std_dev = largest_std_dev.rename(columns= {'count': "num_schools", 'mean': "average_SAT", 'std':"std_SAT"})
largest_std_dev = largest_std_dev.iloc[1:]
print(largest_std_dev)


