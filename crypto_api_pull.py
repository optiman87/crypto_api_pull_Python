# Import the required libraries
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

# Define a function that will pull the CAD rate from top 20 cryptocurrencies using the coinmarketcap API.
def api_runner():
    # Define url and parameters
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'20',
      'convert':'CAD'
        }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'd7a29977-ef6e-4665-8fe5-d3ed677158e8',
        }

    session = Session()
    session.headers.update(headers)
  
    # Retrieve API response in json format
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

    # Store the JSON response in a dataframe
    df= pd.json_normalize(data['data'])

    # Add timestamp to the dataframe
    df['timestamp']= pd.to_datetime('now')

    # Store the dataframa as a csv file, if the csv file exists, the dataframe will be appended to the existing csv file.
    if not os.path.isfile('/Users/ek/Desktop/PythonPortfolio/api_extract.csv'):
        df.to_csv('/Users/ek/Desktop/PythonPortfolio/api_extract.csv', header='column_names',index=None)
    else:
        df.to_csv('/Users/ek/Desktop/PythonPortfolio/api_extract.csv', mode='a',header=None, index=None)
