# 📖 Description
A modular command-line application built in Python that automates the management of a product inventory. The system allows adding, viewing, searching, updating and deleting products, calculating business statistics, and saving or loading data through CSV files — all from the terminal, without external dependencies.

## ⚙️ System Architecture
The application follows a modular architecture where each feature lives in its own independent file. The main.py file acts as the entry point and orchestrator: it imports all feature functions, maintains the shared inventory state (a list of dictionaries), and routes user input from the main menu to the correct module.

## 🔁 Flow Diagram

<img width="6521" height="3580" alt="H3 - CRUD + persistencia" src="https://github.com/user-attachments/assets/086dc1dd-0623-4aac-997b-66d12f54e486" />

## 🚀 How to Run the Program

1. Clone or download the repository so all .py files are in the same folder.
2. Open a terminal in that folder and run python main.py.
3. Follow the on-screen menu to manage your inventory.
4. Use options 7 and 8 to save or load your data as a CSV file at any time.

## 💡 Data Structure and Module Descriptions
The code is based on a list of dictionaries where each dictionary represents one product with three fields: name (str), price (float), and quantity (int). The program is divided into six independent modules, each responsible for a specific part of the system:

1. Add Product - FEATURE_ADD_PRODUCT - add_product(): The user is asked to enter a product name, price, and quantity. The system validates that the values are non-negative and that the product does not already exist. The new product is stored as a dictionary and added to the inventory list.

2. Show Inventory - FEATURE_CHECK_INVENTORY - show_inventory(): Displays all products currently in the inventory in a formatted table, showing name, price, and quantity for each one. If the inventory is empty, it shows a clear message.

3. Search Product - FEATURE_CHECK_PRODUCT - search_product(): The user enters a product name and the system looks for it in the inventory (case-insensitive). If found, it displays the product details. If not, it informs the user without crashing.

4. Update Product - FEATURE_UPDATE_PRODUCT - update_product(): The user selects a product by name and can modify its price, its quantity, or both. Fields left blank are not changed. The system validates that new values are non-negative before applying any update.

5. Remove Product - FEATURE_REMOVE_PRODUCT - remove_product(): The user enters the name of the product to delete. The system confirms it exists before removing it from the inventory list. If the product is not found, it shows a message and returns to the menu.

6. Statistics Report - FEATURE_STADISTIC_REPORT - calculate_statistics(): This module goes through the entire inventory and calculates: total units in stock, total inventory value (price × quantity per product), the most expensive product, and the product with the highest stock. Results are displayed in a readable format using a lambda for per-product subtotals.

7. Save CSV - FEATURE_SAVE_CSV - save_csv(): Saves the current inventory to a CSV file (products.csv) in the same folder as the project. The file includes a header row with the column names. If the inventory is empty, the system shows a message and skips the save. Errors such as permission issues are caught and reported without closing the program.

8. Load CSV - FEATURE_LOAD_CSV - load_csv(): Loads products from an existing CSV file into the inventory. The system validates the file header, checks that each row has exactly three columns, and converts price to float and quantity to int. Invalid rows are skipped and counted. After loading, the user is asked whether to overwrite the current inventory or merge by name if merging, quantities are summed and prices updated to the new value. A summary is shown at the end.

9. Exit: - Ends the program.
