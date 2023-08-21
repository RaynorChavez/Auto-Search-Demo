import discriminator

# Maybe use Decathlon (they have a wide range of products)
url = "https://example-shopify-store.com"
scraper = discriminator.get_scraper_for_url(url)
data = scraper.get_product_data()
scraper.save_to_db(data)
