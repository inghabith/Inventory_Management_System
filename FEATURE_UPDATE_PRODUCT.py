def update_product (products_list):
    keep_updating = "yes"
    while keep_updating == "yes":
        if len(products_list) == 0:
            print("The list is empty, please add products.")
            return
        search_product = input("Please enter the product name: ")

        found = False
        for iterant in products_list:
            
            if iterant["name"] == search_product:
                new_price= int(input("Enter the new price:"))
                new_quantity= int(input("Enter the new quantity:"))

                iterant["price"] = new_price
                iterant["quantity"] = new_quantity

                found = True

        if found == False: 
            print("The product doesn't exist")

        if found == True:
            print ("The update is succesfully!")

        keep_updating = input("Do you want to update another product? yes/no: ")
    