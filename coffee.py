
# The program is a coffe shop with a menu, total stock and price.
# We will need to find out the total stock worth from the coffe shop.

# Tip: When you loop through the menu list, the ‘items’ can be set as keys
# to access the corresponding ‘stock’ and ‘price’ values. Each ‘item_value’ is
# calculated by multiplying stock value by the price value. For example:
# item_value = (stock[items] * price[items])

# Create a list called menu, which should contain at least 4 items in the cafe.
menu = ["coffe", "tea", "cappuccino", "chocolate"]

# Create a dictionary called stock, which should contain the stock value for each item on the menu.
stock = {"coffe": 200,
         "tea": 200,
         "cappuccino": 170,
         "chocolate": 170}

# Create another dictionary called price, which should contain the prices for each item on the menu.
price = {"coffe": 2,
         "tea": 1.5,
         "cappuccino": 1.7,
         "chocolate": 1.7}

# Calculate the total_stock worth in the cafe. 

total_stock_worth = 0  # Create a variable and set value 0
for item in menu:
    total_stock_worth += (stock[item] * price[item])  # Multiply the stock and price and add them togheter to find the total stock worth.

#  Print out the result of calculation.
print(f"Total stock worth in the coffe shop is £ {total_stock_worth}.")