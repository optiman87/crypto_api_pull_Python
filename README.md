Crypto API Pull Python Project

This project will perform an API pull from https://coinmarketcap.com/ and retrieve the USD rate for multiple cryptocurrencies. The API pull script is scheduled to run every minute (60s) but it can be changed to every hour or day.

The dataframe is then cleaned and transformed to show the mean USD percentage change for 1 hour, 24 hours, 7 days, 30 days, 60 days and 90 days.

The API pull script (crypto_api_pull.py), data cleaning script (data_cleaning.py) and the clean data csv file (clean_data.csv) are attached.
