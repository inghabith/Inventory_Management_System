import csv

def load_csv(products_list, path):

    """
    Loads products from a CSV file into the inventory.

    Parameters:
        products_list (list): list of product dictionaries.
        path (str): file path to load the CSV from.

    Returns:
        None
    """


    try:
        # Tries to open the file in read mode
        file = open(path, "r", encoding="utf-8")

    except FileNotFoundError:
        # File does not exist at the given path
        print("Error: File not found.")
        return

    except UnicodeDecodeError:
        # File has characters Python cannot read
        print("Error: File encoding not supported.")
        return

    except Exception:
        # Any other unexpected error while opening the file
        print("Error while opening file.")
        return

    # Reads the file as CSV
    reader = csv.reader(file)

    # Reads the first row which must be the header
    header = next(reader)

    # Validates that the header is correct
    if header != ["name", "price", "quantity"]:
        print("Error: Invalid header.")
        file.close()
        return

    # Temporary list where loaded products are stored
    loaded_products = []

    # Counter for invalid rows
    error_count = 0

    # Loops through each row in the file
    for row in reader:

        # Validates that the row has exactly 3 columns
        if len(row) != 3:
            error_count += 1
            continue

        try:
            name     = row[0]
            price    = float(row[1])  # converts to decimal
            quantity = int(row[2])    # converts to integer

            # Validates that values are not negative
            if price < 0 or quantity < 0:
                error_count += 1
                continue

            # Adds the product to the temporary list
            loaded_products.append({
                "name"    : name,
                "price"   : price,
                "quantity": quantity
            })

        except ValueError:
            # Row has data that cannot be converted
            error_count += 1
            continue

    file.close()

    # Asks the user what to do with the loaded data
    decision = input("Overwrite current inventory? (Y/N): ")

    if decision == "Y":
        # Clears the current list and adds the loaded products
        products_list.clear()
        for product in loaded_products:
            products_list.append(product)

    else:
        # Merges by name
        for loaded in loaded_products:

            # Checks if the product already exists in the list
            found = False
            for existing in products_list:

                if existing["name"] == loaded["name"]:
                    # If it exists, adds quantity and updates price
                    existing["quantity"] += loaded["quantity"]
                    existing["price"] = loaded["price"]
                    found = True

            # If it does not exist, adds it
            if found == False:
                products_list.append(loaded)

    # Shows the summary at the end
    print("Products loaded: " + str(len(loaded_products)))
    print("Invalid rows skipped: " + str(error_count))

    if decision == "Y":
        print("Action: Inventory replaced.")
    else:
        print("Action: Inventory merged.")