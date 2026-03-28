def update_product(products_list):
    """
    Updates the price and quantity of an existing product.

    Parameters:
        products_list (list): list of product dictionaries.

    Returns:
        None
    """

    keep_updating = "yes"
    while keep_updating == "yes":

        if len(products_list) == 0:
            print("The list is empty, please add products.")
            return

        search_product = input("Please enter the product name: ")
        print()

        # Find the product and update its values
        found = False
        for iterant in products_list:
            if iterant["name"] == search_product:
                new_price = int(input("Enter the new price: "))
                new_quantity = int(input("Enter the new quantity: "))
                iterant["price"] = new_price
                iterant["quantity"] = new_quantity
                found = True

        if found == False:
            print("The product doesn't exist")
        if found == True:
            print()
            print("The update is successfully done!")
            print()

        keep_updating = input("Do you want to update another product? yes/no: ")