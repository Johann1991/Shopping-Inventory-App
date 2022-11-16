# ====================== Description ======================

# This program reads a text file with grocery items listed
# Then it displays the prodcts in an easy to read manner

# ================== IMPORTANT DEV NOTES ==================

# Variables that can be changed - 'currency'
# Need to do all calculations in functions

# =========================================================

# Importing modules
from tabulate import tabulate

# Informs the user to what the programme is capable of and what is required
# of the user for the programme to work.
print('''\n----------------------------------------------------------------------
                    Program Description
\nThis program reads a text file with grocery items listed
Then it displays the prodcts in an easy to read manner
\n----------------------------------------------------------------------n''')

# Creating definition to calculate the total amount of products 
def calculate_total_products(quantities_list):

    # Declarin variabes and assigning default values
    total_products = 0
    quantity = 0

    # Using a nested for loop to get the lists from the list to 
    # fetch the value of each and sum it all together.
    for each in quantities_list:
        for index in each:
            total_products = round(total_products + float(index), None)
    
    # Calculating  and returning the total items on the list
    total_products = total_products + quantity
    return total_products

# This function is used to declare the currency
def declare_currency():

    # Declaring the currency and returning the value
    currency = "R "
    return currency

# This function styles the table footer
def style_tabulate(full_list, total_list_items, currency, total):
    # Creating placeholders for styling    
    placeholder = " "
    total_title = "TOTAL"
    total_items = "Total Items"

    # dding a blank line to seperate the total from the groceries
    blank_line = [placeholder, placeholder, placeholder , placeholder]
    full_list.append(blank_line)

    # Adding the total to the end of the slip
    sub_str = [total_title, total_list_items, placeholder , currency + str(total)]
    full_list.append(sub_str)

# Defining the function for counting the lines in the document
def main_method():

    # Declaring lists to store the read data
    prices_list = []
    quantities_list = []
    products_list = []
    full_list = []
    new_list = []
    str_new_list = []

    # Calling function storing the currency
    currency = declare_currency()
     
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

    # Declaring variable to store the total products from the result
    # of the function that is called
    # Calling the function to style the tabulated footer
    total_list_items = calculate_total_products(quantities_list)
    style_tabulate(full_list, total_list_items, currency, total)

    # Returning the total lines
    return(line_count, products_list, quantities_list, prices_list, sub_total, full_list, total_list_items)

# ====================== Main Program ======================

# Declaring the counter to iterate through each list accordingly
counter = 0

# Calling function to count the lines and assign the first value to variable "total_lines"
total_lines = main_method()[0]
products = main_method()[1]
quantities = main_method()[2]
pricing = main_method()[3]
sub_total = main_method()[4]
full_list = main_method()[5]

# Creating truncated headers for the  and printing the final list
headers_list = ["Product", "Quantity", "Price", "Sub-Total"]
print(tabulate(full_list, headers = headers_list, showindex='always', stralign='left', numalign='center', tablefmt='simple_grid'))
