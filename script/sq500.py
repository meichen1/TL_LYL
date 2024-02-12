import requests
from bs4 import BeautifulSoup
import pandas as pd


# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Fetch the page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with S&P 500 companies
table = soup.find('table', {'id': 'constituents'})

# List to hold all rows
rows = []

# Iterate over table rows and extract data
for row in table.find_all('tr'):
    cols = row.find_all(['td', 'th'])
    cols = [ele.text.strip() for ele in cols]
    rows.append(cols)
    
# Create a DataFrame
df = pd.DataFrame(rows[1:], columns=rows[0])
df.to_csv('../data/sq500.csv', index=False)