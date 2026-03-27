def inventory_list(product_list):
    print("="*60)
    print("                INVENTORY LIST")
    
    for iterant in product_list:
        print("Product:".ljust(30), iterant["name"])
        print("Price:".ljust(30), iterant["price"])
        print("Quantity:".ljust(30), iterant["quantity"])
        print("-"*60)
        print()