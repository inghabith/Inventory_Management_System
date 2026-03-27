from FEATURE_ADD_PRODUCT import add_products
from FEATURE_CHECK_INVENTORY import inventory_list
from FEATURE_CHECK_PRODUCT import check_product
from FEATURE_UPDATE_PRODUCT import update_product
from FEATURE_REMOVE_PRODUCT import remove_product
from FEATURE_STADISTIC_REPORT import stadistic_calculator
products_list = []




print(f"""
    ╔═══════════════════════════════════════════════════════════╗
                    🛒 Pricesmart Riwi 🛒
    🌷 Welcome to the Customer Order Management System! 🌷
    ╚═══════════════════════════════════════════════════════════╝""")

Menu = "yes"

while Menu == "yes":    

    try:
        Option = int(input(f"""{"-"*24} MAIN MENU {"-"*25} 
1) 🤵  Enter product 
2) 🥦  Check inventory 
3) 🧾  Check product
4) 🔍  Update products
5) 📋  Remove products
6) 📋   Stadistic report
{"="*60}
~ Please select an option:
➤  """))

        if Option < 1 or Option > 9:
            print(f"\n{'❌ ERROR: Please enter a valid number ❌':^60}\n")
            continue  

    except ValueError:
        print(f"\n{'❌ ERROR: Please enter a valid integer ❌':^60}\n")
        continue 



    if Option == 1:
        add_products(products_list)

    if Option == 2:
        inventory_list(products_list)

    if Option == 3:
        check_product(products_list)

    if Option == 4:
        update_product(products_list)

    if Option == 5:
        remove_product(products_list)

    if Option == 6:
        stadistic_calculator(products_list)

    



    Menu = input("Do you want to return to the main menu? yes/no: ")