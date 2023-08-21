class BaseScraper:
    def __init__(self, url):
        self.url = url

    def get_product_data(self):
        raise NotImplementedError("Subclasses should implement this method")

    def save_to_db(self, data):
        # Code to save data to the database
        pass

    def enter_to_indexing_queue(self, data):
        # Code to enter data to the indexing queue
        pass

    # ... common methods
