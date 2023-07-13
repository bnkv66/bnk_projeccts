import csv
import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://statisticstimes.com/demographics/country/india-cities-population.php'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table on the page
table = soup.find('table')


# Open a CSV file in write mode
csv_file = open('C:/Users/91994/OneDrive/Desktop/data1.csv','w', newline='')
# Create a CSV writer object
csv_writer = csv.writer(csv_file)

# Iterate over the table rows and extract the data
for row in table.find_all('tr'):

# Get the cells in each row
 cells = row.find_all('td')

# Extract the text from the cells
data1 = [cell.text.strip() for cell in cells]

# Write the data to the CSV file
csv_writer.writerow(data1)
# Close the csv file
csv_file.close()










