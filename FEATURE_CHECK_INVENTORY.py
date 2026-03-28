def inventory_list(product_list):
    """
    Displays all products in the inventory.

    Parameters:
        product_list (list): list of product dictionaries.

    Returns:
        None
    """
    
    # Nothing to show if the list is empty
    if len(product_list) == 0:
        print("Error, the list is empty")
        return

    print("="*60)
    print("INVENTORY LIST".center(60))
    
    # Print each product with its details
    for iterant in product_list:
        print("Product:".ljust(50), iterant["name"])
        print("Price:".ljust(50), iterant["price"])
        print("Quantity:".ljust(50), iterant["quantity"])
        print("-"*60)
        print()