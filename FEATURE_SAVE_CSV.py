import csv

def save_csv(products_list, path, include_header= True):
 
    """
    Saves the inventory into a CSV file.

    Parameters:
        products_list (list): list of product dictionaries.
        path (str): file path to save the CSV.
        include_header (bool): if True, writes the header row. Default is True.

    Returns:
        None
    """

    if len(products_list) == 0:
        print("Inventory is empty, cannot save.")
        return
        
    try:
        file = open(path, "w", newline="", encoding="utf-8")
        writer = csv.writer(file)

        # Write header
        if include_header:
            writer.writerow(["name", "price", "quantity"])

        # Write product data
        for iterant in products_list:
            writer.writerow([iterant["name"], iterant["price"], iterant["quantity"]])

        file.close()
        print("File saved at:", path)

    except:
        print("Error while saving file.")
