def remove_product(products_list):
    """
    Removes a product from the inventory by name.

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

        # Search and remove the product if it exists
        found = False
        for iterant in products_list:
            if iterant["name"] == search_product:
                products_list.remove(iterant)
                found = True

        if found == False:
            print("The product doesn't exist")
        if found == True:
            print("The product was removed successfully!")

        keep_updating = input("Do you want to remove another product? yes/no: ")