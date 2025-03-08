import requests
from bs4 import BeautifulSoup
import logging

class SenicProducts:
    def __init__(self):
        self.base_url = "https://senic.ro/wp-content/uploads/2021/10/"
        self.products = self.get_products()

    def get_products(self):
        """Fetch and parse product images from the Senic website."""
        try:
            resp = requests.get(self.base_url)
            if resp.status_code != 200:
                logging.error(f"Failed to fetch data (Status Code: {resp.status_code})")
                return {}

            # Parse HTML content
            soup = BeautifulSoup(resp.text, 'html.parser')
            products = {}

            for link in soup.find_all('a'):
                file_name = link.get('href')
                if file_name and file_name.endswith('.png'):
                    product_name = " ".join(file_name.replace(".png", "").split("-")[:-1])
                    full_url = self.base_url + file_name

                    if product_name in products:
                        products[product_name].append(full_url)
                    else:
                        products[product_name] = [full_url]

            return products

        except Exception as e:
            logging.error(f"Error fetching products: {e}")
            return {}
    
    def search_product(self, product_name):
        """Search for a product by name and return its URLs."""
        result = {key: value for key, value in self.products.items() if product_name.lower() in key.lower()}
        return result if result else None
