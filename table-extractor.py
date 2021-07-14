from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('url of the page that contains table').text

soup = BeautifulSoup(source,'lxml')

table_rows = soup.findAll('tr')

with open('your_csv_file.csv','w') as csv_file:

    csv_writer = csv.writer(csv_file)

    for index, table_row in enumerate(table_rows):

        table_row_text = []
    
        for data in table_row:
            table_row_text.append(data.get_text())

        csv_writer.writerow(table_row_text)