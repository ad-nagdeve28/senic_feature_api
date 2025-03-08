import request_mang
from fetch_products import SenicProducts


def product_fetch():
    senic = SenicProducts()
    product = senic.get_products()
    return product


if __name__ == "__main__":
    call = request_mang()
    senic = SenicProducts()
    product = senic.get_products()
    product_fetch()
