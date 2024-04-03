from bs4 import BeautifulSoup
import os
from datetime import datetime

# Parser Class
class Parser:
    """
    Parses HTML files to extract and save document data to MongoDB.
    """
    def __init__(self, db_layer):
        """
        Initializes the Parser with a reference to the MongoDBDataLayer.
        :param db_layer: An instance of MongoDBDataLayer for database operations.
        """
        self.db_layer = db_layer

    def parse(self, folder_path):
        """
        Parses all HTML files in a specified folder and saves extracted data.
        :param folder_path: Path to the folder containing HTML files.
        """
        for filename in os.listdir(folder_path):
            if filename.endswith('.html'):
                with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                    soup = BeautifulSoup(file, 'html.parser')

                    table = soup.find('table')
                    if not table:
                        continue

                    caption = table.find('caption').get_text(strip=True) if table.find('caption') else 'No Title'
                    header = [th.get_text(strip=True) for th in table.find_all('th')]
                    body = [[td.get_text(strip=True) for td in tr.find_all('td')] for tr in
                            table.find('tbody').find_all('tr')]

                    # Find the `td` containing the text "Creation:" and extract date and country
                    creation_td = table.find('td', string=lambda text: text and "Creation:" in text)
                    if creation_td:
                        creation_text = creation_td.get_text(strip=True)
                        creation_parts = creation_text.split(' ')
                        try:
                            date_of_creation = datetime.strptime(creation_parts[1], '%d%b%Y').strftime('%d/%m/%Y')
                        except (IndexError, ValueError):
                            date_of_creation = 'Unknown'
                        country_of_creation = ' '.join(creation_parts[2:]) if len(creation_parts) >= 3 else 'Unknown'
                    else:
                        date_of_creation = 'Unknown'
                        country_of_creation = 'Unknown'

                    doc_data = {
                        'document_id': filename.split('.')[0],
                        'title': caption,
                        'header': header,
                        'body': body,
                        'footer': creation_td.get_text(strip=True) if creation_td else 'Unknown',
                        'country_of_creation': country_of_creation,
                        'date_of_creation': date_of_creation
                    }

                    self.db_layer.insert_document(doc_data)