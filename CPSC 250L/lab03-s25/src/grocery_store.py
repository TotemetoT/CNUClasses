"""
Practice with lists, tuples, dictionary, and strings


@author Ryan Schatzberg
@version 1/30/2025

"""
# pylint: disable-msg=C0103

# import os

def stock():
    """
    Returns the dictionary reference with key:value pairs
    described in README
    :return: reference to a dictionary object
    """

    shopping = {
        'pink lady apple': 2.99,
        'honeycrisp apple': 3.99,
        'eggs':1.29,
        'bananas':3.99,
        'milk':4.59,
        'ground beef':8.99,
        'cheerios':3.69
    }

    return shopping

def shop(stock_dict, shopping_list):
    """
    Calculate total cost of shopping trip

    See the README for description of the output

    :param stock_dict:  dictionary containing grocery stock with item_name:price_per_quantity pairs
    :param shopping_list:  list of tuples of [(item_name1, quantity1), (item_name2, quantity2),... ]
    :return: tuple with (total, receipt, out_of_stock_list)
    """
    buying_list = []
    no_stock = []
    total_price = 0
    rec = ""
    for item in shopping_list:
        if item[0] in stock_dict.keys():
            buying_list.append(item)
        else:
            no_stock.append(item[0])
    for item in buying_list:
        temp = stock_dict.get(item[0]) * item[1]
        rec += f'{item[0]:21}${temp:6.2f}\n'
        total_price += temp
    rec += '                      ------\n'
    rec += f'total                ${total_price:6.2f}'
    return total_price,rec,no_stock




if __name__ == '__main__':


    print(" Example usage of stock() and shop() :")

    # Get the stock dictionary as defined in README
    store_stock = stock()
    print(" Stock : ", store_stock)

    # Define a grocery list
    grocery_list = [("honeycrisp apple", 2), ("milk", 1), ("delci food", 1)]
    print("Shopping list: ", grocery_list)

    # Do the shopping
    total, receipt, out_of_stock = shop(store_stock, grocery_list)
    print(" Total=", total)
    print(receipt)
    print(" Out of stock: ", out_of_stock)
