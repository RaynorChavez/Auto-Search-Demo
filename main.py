from ecommerce_scraper import discriminator

# Maybe use Decathlon (they have a wide range of products)
"""
url = "https://example-shopify-store.com"
scraper = discriminator.get_scraper_for_url(url)
data = scraper.get_product_data()
scraper.save_to_db(data)
"""

from ecommerce_scraper.core.base_scraper import BaseScraper
from ecommerce_scraper.platforms.shopify_scraper import ShopifyScraper

urls = ["https://www.taylorstitch.com", "https://www.decathlon.com", "https://www.bisoncoolers.com"]

for i in range(len(urls)):
    print(f"Scraping {urls[i]}")
    scraper = ShopifyScraper(urls[i])
    product_data = scraper.get_product_data()
    #scraper.save_to_csv(product_data, f"{urls[0].split('//')[1].split('.')[1]}_products.csv")
    scraper.save_to_csv(product_data) 