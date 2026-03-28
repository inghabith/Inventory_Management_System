def add_products(products_list):      
    """
    Adds one or more products to the inventory.
    Parameters:
        products_list (list): list of product dictionaries.
    Returns:
        None
    """
    keep_register = "yes"
    while keep_register == "yes":

        # Name can't be empty
        product_name = ""
        while product_name == "":
            print()
            product_name = input("Enter product name: ")
            if product_name == "":
                print ("Error, this field must be filled")

        # Price must be a positive number
        product_price = 0 
        while product_price <= 0:
            try:
                print()
                product_price = int(input("Enter the product price: $ "))
                if product_price <= 0:
                    print("Error, please enter a positive integer value: ")
            except ValueError:
                print("Error, please enter a numeric positive integer value: ")

        # Quantity must be a positive number
        product_quantity = 0
        while product_quantity <= 0:
            try:
                print()
                product_quantity = int(input("Enter the product quantity: units "))
                if product_quantity <= 0:
                    print("Error, please enter a positive integer value: ")
            except ValueError:
                print("Error, please enter a numeric positive integer value: ")

        # Build the product and add it to the list
        product_dictionary = {
            "name" : product_name,
            "price" : product_price,
            "quantity" : product_quantity
        }
        
        products_list.append(product_dictionary)
        keep_register = input ("Do you want to add another product yes/no?: ")
        print()
        print("-"*60)