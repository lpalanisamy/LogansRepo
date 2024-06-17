import requests
from bs4 import BeautifulSoup
import csv
import re

# Function to process a single URL and write data to CSV
def process_url(url, writer):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the state and constituency info from the h2 tag
    h2 = soup.find('div', class_='page-title').find('h2').text.strip()
    state = re.sub(r"Parliamentary  Constituency .* \((.*)\)", r"\1", h2)
    constituency = re.sub(r"Parliamentary  Constituency .* - (.*) \(.*", r"\1", h2)

    # Extract the table data
    table = soup.find('table', {'class': 'table table-striped table-bordered'})
    rows = table.find_all('tr')

    # Write the data to the CSV
    for row in rows[1:-1]:  # Skip header and footer rows
        columns = row.find_all('td')
        candidate = columns[1].text.strip()
        party = columns[2].text.strip()
        votes = columns[5].text.strip()
        percentage = columns[6].text.strip()
        writer.writerow([state, constituency, candidate, party, votes, percentage])

# Read URLs from the urls.txt file
with open('urls.txt', 'r') as url_file:
    urls = url_file.read().splitlines()

# Open the CSV file for writing
with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['State', 'Constituency', 'Candidate', 'Party', 'Votes', 'Percentage'])

    # Process each URL
    for url in urls:
        process_url(url, writer)
