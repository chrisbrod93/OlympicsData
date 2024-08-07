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


total_pop = pd.merge(df,df1, on='Country')

pop_gdp = pd.merge(total_pop,df2, on='Country')


