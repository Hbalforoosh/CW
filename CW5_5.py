
def price_invent(min_value):
    invent = {
        'apple': {'quantity': 50, 'price': 2},
        'banana': {'quantity': 30, 'price': 1},
        'orange': {'quantity': 20, 'price': 3}
    }

    finall_value = 0
    all_product = []

    for product in invent :
        quantity = invent[product]['quantity']
        price = invent[product]['price']
        first_value = quantity*price
        all_product.append((product, first_value))
        finall_value += first_value
    filtered_product = list(filter(lambda i: i[1] < min_value, all_product))
    return finall_value, filtered_product
total_value, list_Under = price_invent(50)
print(f"total: {total_value}\nUndervalue: {list_Under}\n")
