def add_products(products_list):
    keep_register = "yes"
    while keep_register == "yes":

        product_name = ""

        while product_name == "":
            print()
            product_name = input("Enter product name: ")

            if product_name == "":
                print ("Error, this field must be filled")
    #------------------------------------------------------------
        product_price = 0 

        while product_price <= 0:
            try:
                print()
                product_price = int(input("Enter the product price: "))

                if product_price <= 0:
                    print("Error, please enter a positive integer value: ")

            except ValueError:
                print("Error, please enter a numeric positive integer value: ")

    #-------------------------------------------------------------
        product_quantity = 0
        while product_quantity <= 0:
            try:
                print()
                product_quantity = int(input("Enter the product quantity: "))
                
                if product_quantity <= 0:
                    print("Error, please enter a positive integer value: ")

            except ValueError:
                print("Error, please enter a numeric positive integer value: ")
#---------------------------------------------------------------
        product_dictionary = {
            "name" : product_name,
            "price" : product_price,
            "quantity" : product_quantity
        }
        
        products_list.append(product_dictionary)

        keep_register = input ("Do you want to add another product yes/no: ?")