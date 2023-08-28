from ecommerce_scraper.core.base_scraper import BaseScraper
import requests
from tqdm import tqdm

class ShopifyScraper(BaseScraper):
    def get_product_data(self):
        product_data = []
        page = 1
        items_scraped = 0 # Keep track of the number of items scraped

        # Initial fetch to get the first set of products and estimate total products
        products = self._get_page(page)
        if not products:
            return product_data

        with tqdm(desc="Fetching products") as pbar:
            while products:
                for product in products:
                    name = product['title']
                    product_url = self.url + '/products/' + product['handle']
                    category = product['product_type']

                    # Fetching product description
                    description = product.get('body_html', '').strip()

                    # Fetching product images (using the first image as the primary image)
                    images = product.get('images', [])
                    primary_image_url = images[0]['src'] if images else None

                    for variant in product['variants']:
                        variant_names = []
                        for i in range(1, 4):
                            k = 'option{}'.format(i)
                            if variant.get(k) and variant.get(k) != 'Default Title':
                                variant_names.append(variant[k])
                        variant_name = ' '.join(variant_names)
                        price = variant['price']
                        row = [name, category, variant_name, price, product_url, primary_image_url, description]
                        product_data.append(row)
                    
                    # Update the count of items scraped
                    items_scraped += len(product['variants'])

                    # If the limit is reached, break out of the inner loop
                    if items_scraped >= BaseScraper.MAX_ITEMS:
                        break
                    
                # If the limit is reached, break out of the outer loop
                if items_scraped >= BaseScraper.MAX_ITEMS:
                    break

                page += 1
                products = self._get_page(page)
                pbar.update(len(products))  # Update the progress bar based on the number of products fetched

        return product_data

    def _get_page(self, page):
        response = requests.get(f"{self.url}/products.json?page={page}")
        if response.status_code != 200:
            return None
        return response.json().get('products')
