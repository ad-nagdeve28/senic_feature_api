import request_mang
from fetch_products import SenicProducts

if __name__ == "__main__":
    request_mang
    senic = SenicProducts()
    product = senic.get_products()
