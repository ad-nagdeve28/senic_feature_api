import requests
from bs4 import BeautifulSoup
import json

class SenicProducts:
    def __init__(self):
        self.base_url = "https://senic.ro/wp-content/uploads/2021/10/"
        self.products = self.get_products()

    def get_products(self):
        try:
            resp = requests.get(self.base_url)
            if resp.status_code != 200:
                print(f"Error: Unable to fetch data (Status Code: {resp.status_code})")
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
            print(f"Error: {e}")
            return {}
    
    def search_product(self, product_name):
        """Search for a product by name and return its URLs."""
        result = {key: value for key, value in self.products.items() if product_name.lower() in key.lower()}
        return result if result else f"No products found for '{product_name}'"



if __name__ == "__main__":
    senic = SenicProducts()
    product = senic.get_products()
    

