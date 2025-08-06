class Product:
    product_favorite_counter = {}

    def __init__(self, product_id, name):
        self.name = name
        self.product_id = product_id


class Customer:
    def __init__(self, user_name):
        self.user_name = user_name
        self.fav_list = set()

    def add_fav(self, product):
        if isinstance(product, Product):
            if Product.product_favorite_counter.get(product.name):
                Product.product_favorite_counter[product.name] += 1
            else:
                Product.product_favorite_counter[product.name] = 1
            self.fav_list.add(product)
            return f"Added {product.name} to favorites."

    def show_fav(self):
        return f"List fav is: {self.fav_list}"

    def remove_product(self, product):
        if product in self.fav_list:
            return self.fav_list.discard(product)
        else:
            return f"We dont have: {product}"


class Manager:
    data_user = {}
    favorite_count = {}
    products = {}

    @staticmethod
    def most_popular_product():
        if not Product.product_favorite_counter:
            return "No products have been favorited yet."
        most_popular = max(
            Product.product_favorite_counter.items(), key=lambda x: x[1])
        return f"Most popular product is '{most_popular[0]}' with {most_popular[1]} favorites."
