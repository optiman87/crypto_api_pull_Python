# Import the required libraries
import pandas as pd

# Import the extract cvs file into a dataframe
df= pd.read_csv('/Users/ek/Desktop/PythonPortfolio/api_extract.csv')

# Rename the required columns
df= df.rename(columns={'name': 'Cryptocurrency', 'quote.CAD.price':'CAD Price','quote.CAD.percent_change_1h':'1 hour','quote.CAD.percent_change_24h':'24 hours','quote.CAD.percent_change_7d': '7 days','quote.CAD.percent_change_30d':'30 days','quote.CAD.percent_change_60d':'60 days','quote.CAD.percent_change_90d':'90 days'})

# Create a new dataframe to store the required columns
df2= df[['Cryptocurrency', 'CAD Price', '1 hour', '24 hours', '7 days', '30 days', '60 days', '90 days']]

# Group the dataframe by Cryptocurrency and display the mean CAD Price, 1 hour, 24 hours, 7 days, 30 days, 60 days, 90 days values
df2= df2.groupby('Cryptocurrency')[['CAD Price', '1 hour', '24 hours', '7 days', '30 days', '60 days', '90 days']].mean()

Save the dataframe to a csv file
df2.to_csv('/Users/ek/Desktop/PythonPortfolio/clean_data.csv')



