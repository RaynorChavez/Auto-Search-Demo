from ecommerce_scraper.core.base_scraper import BaseScraper
from ecommerce_scraper.platforms.shopify_scraper import ShopifyScraper

scraper = ShopifyScraper("http://decathlon.com")
product_data = scraper.get_product_data()
scraper.save_to_csv(product_data, "decathlon_products.csv")
