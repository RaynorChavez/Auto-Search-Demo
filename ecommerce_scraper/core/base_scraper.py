import csv 
import os

class BaseScraper:
    MAX_ITEMS = 100000 # Maximum number of items to scrape

    def __init__(self, url):
        self.url = url

    def get_product_data(self):
        raise NotImplementedError("Subclasses should implement this method")

    def save_to_csv(self, data, filename=None):
        if filename is None:
            filename = self.generate_filename()

        # Ensure 'data' directory exists
        if not os.path.exists('./data'):
            os.makedirs('./data')

        with open(f'./data/{filename}', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Category', 'Variant Name', 'Price', 'URL', 'Image URL', 'Description'])
            for row in data:
                writer.writerow(row)

    def generate_filename(self, suffix="_products.csv"):
        """Generate a filename based on the URL."""
        # Extract domain from the URL
        domain_name = self.url.split('//')[-1].split('/')[0]
        # Strip 'www.' if present
        domain_name = domain_name.replace("www.", "")
        # Use only the main part of the domain for filename
        filename_base = domain_name.split('.')[0]
        return f"{filename_base}{suffix}"

    def save_to_db(self, data):
        # Code to save data to the database
        pass

    def enter_to_indexing_queue(self, data):
        # Code to enter data to the indexing queue
        pass

    # ... common methods
