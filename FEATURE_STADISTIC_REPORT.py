def stadistic_calculator(products_list):
    """
    Calculates and displays inventory statistics.

    Parameters:
        products_list (list): list of product dictionaries.

    Returns:
        dict: dictionary with total_units, total_value, most_expensive and most_stock.
    """

    if len(products_list) == 0:
        print("The list is empty.")
        return

    # Add up units and total value across all products
    total_units = 0
    total_value = 0
    for product in products_list:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]

    # Find the most expensive and highest stock products
    producto_mas_caro = max(products_list, key=lambda p: p["price"])
    producto_mayor_stock = max(products_list, key=lambda p: p["quantity"])

    # Lambda to calculate subtotal per product
    subtotal = lambda p: p["price"] * p["quantity"]

    print("Statistics".center(60, "-"))
    print("Total units:".ljust(50), total_units)
    print("Total value:".ljust(50), total_value)
    print("Most expensive product:".ljust(50), producto_mas_caro["name"], "-", "$", producto_mas_caro["price"])
    print("Product with most stock:".ljust(50), producto_mayor_stock["name"], "-", producto_mayor_stock["quantity"], "units")
    print("Subtotals per product:")
    for product in products_list:
        print(" " + product["name"] + ": $", str(subtotal(product)))

    return {
        "total_units"    : total_units,
        "total_value"    : total_value,
        "most_expensive" : producto_mas_caro,
        "most_stock"     : producto_mayor_stock
    }