import pandas as pd

activity = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-31/cats_uk.csv')
cat_info = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-31/cats_uk_reference.csv')

# print(cat_info.info())
# print(cat_info.columns)
# print(cat_info['animal_id'])

# How many male/female cats?
selector = cat_info['animal_sex'] == 'm'
print(cat_info.loc[selector, 'animal_id'])

# Average age of the cats by sex (m/f)
# print(cat_info['age_years'].mean())
print(f'Male cats: {cat_info.loc[selector, "age_years"].mean():.1f}')
print(f'Female cats: {cat_info.loc[~selector, "age_years"].mean():.1f}')
# ~selector
# print(cat_info.info())

# print(selector)
# cat_info.loc[['animal_sex']]

# Plot the trajectory (using lat/long readings) of the oldest
# female cat
oldest_f_cats = cat_info.loc[~selector, ['animal_id', 'age_years']].sort_values(by='age_years', ascending=False)
cat_of_interest = oldest_f_cats.iloc[0]['animal_id']
print(cat_of_interest)

# Look up this cat and extract the rows in 'activity'
# and plot their geographical location

print(activity.head())