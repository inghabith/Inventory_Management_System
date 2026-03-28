def check_product(products_list):
    """
    Searches for a product in the inventory by name.

    Parameters:
        products_list (list): list of product dictionaries.

    Returns:
        None
    """

    if len(products_list) == 0:
        print("The list is empty, please add new products.")
        return

    search_product = input("Please enter the product name: ")
    print()
    print("-"*50)

    # Look for the product by name
    found = False
    for iterant in products_list:
        if iterant["name"] == search_product:
            print("Product: ".ljust(30), iterant["name"])
            print("Price: ".ljust(30), iterant["price"])
            print("Quantity".ljust(30), iterant["quantity"])
            found = True
        print("-"*50)

    if found == False:
        print("The product doesn't exist")