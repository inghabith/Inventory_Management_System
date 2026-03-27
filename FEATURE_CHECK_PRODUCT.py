def check_product (products_list):
    
    if len(products_list) == 0:
        print("The list is empty, please add new products.")
        return
    search_product = input("Please enter the product name: ")

    found = False
    for iterant in products_list:
        
        if iterant["name"] == search_product:
            print("Product: ".ljust(30), iterant["name"])
            print("Price: ".ljust(30), iterant["price"])
            print("Quantity".ljust(30), iterant["quantity"])
            found = True

    if found == False: 
        print("The product doesn't exist")
    