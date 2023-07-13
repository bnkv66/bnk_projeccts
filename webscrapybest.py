import csv
import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://statisticstimes.com/demographics/country/india-cities-population.php'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with a specific attribute or class name
table = soup.find('table', attrs={'class': 'Population of Cities in India (UN)'})

# Open a CSV file in write mode
csv_file = open('C:/Users/91994/OneDrive/data.csv', 'w', newline='')

# Create a CSV writer object
csv_writer = csv.writer(csv_file)

# Iterate over the table rows and extract the data
for row in table.find_all('tr'):
 # Get the cells in each row
 cells = row.find_all('td')

 # Extract the text from the cells
 data = [cell.text.strip() for cell in cells]

 # Write the data to the CSV file
 csv_writer.writerow(data)

# Close the CSV file
csv_file.close()

