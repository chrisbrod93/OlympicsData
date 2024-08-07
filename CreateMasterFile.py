import pandas as pd

df = pd.read_csv('GlobalPop1960_2022.csv')


# Formating Columns to end with 'Population' for clarity after merging
#df.rename(columns=lamda x: x + 'Population' , inplace=True)
df1 = pd.read_csv('World Population by country 2024.csv')
df2 = pd.read_csv('Per Capita GDP of All Countries 1970 to 2022.csv')
df.columns = ('Population ' + col for col in df.columns)
df.rename(columns={'Population Country Name': 'Country'}, inplace=True)

###Renaming Key in GDP File

df2.columns = ('GDP ' + col for col in df2.columns)
df2.rename(columns={'GDP Country': 'Country'}, inplace=True)

## Total population Data frame
total_pop = pd.merge(df,df1, on='Country')


## Pop and GDP Dataframe
pop_gdp = pd.merge(total_pop,df2, on='Country')



### Creating a % Change in Population DataFrame for Reference 

only_population_df = total_pop[['Country'] + total_pop.filter(like='Population',axis=1).columns.tolist()]
only_population_df.set_index('Country', inplace=True)

total_pop_pct_change = only_population_df.pct_change(axis=1) * 100
total_pop_pct_change.columns = [f'{year}% Change' for year in total_pop_pct_change.columns]
total_pop_pct_change.reset_index(inplace=True)
total_pop_pct_change.filter(like='Population 1960% Change',axis=1)
total_pop_pct_change

