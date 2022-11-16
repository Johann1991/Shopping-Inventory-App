# ====================== Description ======================

# This program reads a text file with grocery items listed
# Then it displays the prodcts in an easy to read manner

# ================== IMPORTANT DEV NOTES ==================

# Variables that can be changed - 'currency'
# Need to do all calculations in functions
# Set up on git repository

# =========================================================

# Importing modules
from tabulate import tabulate

# Informs the user to what the programme is capable of and what is required
# of the user for the programme to work.
print('''\n--------------------------------------------------------
                    Program Description
\nThis program reads a text file with grocery items listed
Then it displays the prodcts in an easy to read manner
\n--------------------------------------------------------''')

# Defining the function for counting the lines in the document
def line_counter():

    # Declaring lists to store the read data
    prices_list = []
    quantities_list = []
    products_list = []
    full_list = []
    new_list = []
    str_new_list = []

    # Declaring currancy
    currency = "R "
    
    # Declaring variable to store the integer values of all the products on the slip
    total = 0
    sub_total = 0
    qty = 0
    price = 0
    all_items = 0

    # Declaring the variable to store the line count
    line_count = 0

    # Open and read the file to store the list in a string
    f = open("Shopping_list.txt", "r")

    # Using a conditional statement to iterate through the 
    # Splitting the original string into a list
    for each_item in f:
        shopping_list = each_item.split(',')

        # Adding quantity and price in a single list to calculate the sub totals
        temp_sub_total_string = shopping_list[1] + ' ' + shopping_list[2]
        sub_total_list = temp_sub_total_string.split(' ')
        sub_total_list = [eval(i) for i in sub_total_list]
        qty = sub_total_list[0]
        price = sub_total_list[1]
        sub_total = round(qty * price, 2)
        total = total + sub_total

        # Converting the subtotal to a nice display format
        str_subtotal = currency + str(sub_total)

        # Stripping leading and tailing whitespaces to prevent the sub-total from 
        # Creating a new grocery list
        new_price_string = (currency + str(shopping_list[2]).strip())
        str_new_list = [shopping_list[0], shopping_list[1] , new_price_string, str_subtotal]

        # Creating the products with complete details
        full_list.append(str_new_list)

        # Adding total items
        individual_items = float(shopping_list[1])

        # Using a conditional statement to check if the unit of measure is a float
        # if it is the unit of measure should be set to 1 as 
        # it would be scanned individually
        if individual_items != float:
            individual_items = 1
        all_items = all_items + individual_items

        # Assigning values to the relevant lists
        product = shopping_list[0]
        quantity = shopping_list[1]
        price = shopping_list[2]

        # Appending each element from the index to the relevant list.
        products_list.append([product])
        quantities_list.append([quantity])
        prices_list.append([price])

        # Adding count to line_count variable to increase total lines
        line_count += 1

    # Creating placeholders for styling    
    placeholder = " "
    total_title = "TOTAL"
    total_items = "Total Items"

    # dding a blank line to seperate the total from the groceries
    blank_line = [placeholder, placeholder, placeholder , placeholder]
    full_list.append(blank_line)

    # Adding the total to the end of the slip
    sub_str = [total_title, all_items, placeholder , currency + str(total)]
    full_list.append(sub_str)

    # Returning the total lines
    return(line_count, products_list, quantities_list, prices_list, sub_total, full_list)

# ====================== Main Program ======================

# Declaring the counter to iterate through each list accordingly
counter = 0

# Calling function to count the lines and assign the first value to variable "total_lines"
total_lines = line_counter()[0]
products = line_counter()[1]
quantities = line_counter()[2]
pricing = line_counter()[3]
sub_total = line_counter()[4]
full_list = line_counter()[5]

# Creating truncated headers for the  and printing the final list
headers_list = ["Product", "Quantity", "Price", "Sub-Total"]
print(tabulate(full_list, headers = headers_list, showindex='always', stralign='left', numalign='center', tablefmt='simple_grid'))
