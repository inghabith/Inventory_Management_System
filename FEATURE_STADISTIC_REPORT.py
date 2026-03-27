def stadistic_calculator(products_list):
    if len(products_list) == 0:
        print("The list is empty.")
        return

    total_units = 0
    total_value = 0

    for product in products_list:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]

    producto_mas_caro = max(products_list, key=lambda p: p["price"])
    producto_mayor_stock = max(products_list, key=lambda p: p["quantity"])

    subtotal = lambda p: p["price"] * p["quantity"]

    print("Total units:", total_units)
    print("Total value:", total_value)
    print("Most expensive product:", producto_mas_caro["name"], "-", producto_mas_caro["price"])
    print("Product with most stock:", producto_mayor_stock["name"], "-", producto_mayor_stock["quantity"])