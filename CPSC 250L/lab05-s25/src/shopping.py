"""
This program takes information regarding items that are at two different stores
and turns the information from the .txt files into dictionaries for easier viewing.

Once dictionaries are made the shopping list .txt file is turned into a dictionary

Finally, once all the dictionaries are made they're sorted through to see what place had the
best price and whichever has the bast price is where the user will buy the item from.
"""
# Start by writing your initial concept design in comments here!
# commit this design document before starting to code

# Next create your function stubs, and required main method in this script

# Make functions to find if item is at each grocery store
# If the same item is in both stores then save the store and price for the lower store
# If the item is only in one of the stores use that store
# If the item isn't anywhere then append to 'no_stock' list
# Use f-strings to make everything print correctly

import os

def sort_shopping(shopping):
    """
    This turns the List.txt file into a dictionary
    @param shopping: shopping file path
    @return: Dictionary containing what is planned to be bought
    """
    buying = []
    sorted_buying = []
    with open(shopping,'rt',encoding='utf-8') as shoppe:
        lines = shoppe.readlines()
    for line in lines:
        buying.append([line[:len(line)-1]])
    for item_set in buying:
        item = item_set[0]
        temp = []
        temp_string = ""
        while item != "":
            if item[0] == ',':
                if temp_string[0].isdigit():
                    temp.append(item[2:])
                    temp.append(temp_string)
                    sorted_buying.append(temp)
                    temp = ""
                else:
                    temp.append(temp_string)
                    temp.append(item[2:])
                    sorted_buying.append(temp)
                    item = ""
            if item != "":
                if item[0].isdigit():
                    temp_string += item[0]
                    item = item[1:]
                else:
                    temp_string += item[0]
                    item = item[1:]
    buying_dict = {}
    for item in sorted_buying:
        buying_dict[item[0]] = item[1]

    return buying_dict

def store_to_dict(store_path):
    """
    This function turns the given .txt file into a dictionary
    @param store_path: file path to the stores .txt file
    @return: Dictionary containing item names and their given prices
    """
    store_dict = {}
    with open(store_path,'rt',encoding='utf-8') as store:
        line = store.readlines()
    for item in line:
        item = item[:len(item)-1]
        temp = ""
        while item[0] != '$':
            temp += item[0]
            item = item[1:]
        store_dict[temp[:len(temp)-1]] = item
    return store_dict

def prices(wfood,food,harris_teeter):
    """
    This function finds the best deals for the user by looking through different
    dictionaries and finding which store has the lowest price
    @param wfood: Dictionary of what is being bought
    @param food: Dictionary of what store one has in stock and the items given prices
    @param harris_teeter: Dictionary of what store one has in stock and the items given prices
    @return: String formatted as a receipt containing what was bought and other details
    """
    buying_list = []
    total = 0
    no_stock = []
    dash = '--------------------------------------------------------------'
    string = f'{"Store":20}{"Item":19}{"Quantity":11}{"Total Price"}'
    for key in wfood:
        count = 0
        temp_list = []
        if key in food:
            count = 1
            if key in harris_teeter:
                count = 3
        if key in harris_teeter:
            count = 2
        if count == 0:
            no_stock.append(key)
        elif count == 1:
            temp_list.append("Food Lion")
            temp_list.append(key)
            temp_list.append(wfood.get(key))
            temp_list.append(f'{float(wfood.get(key)) * float(food.get(key)[1:]):.2f}')
            buying_list.append(temp_list.copy())
            total += float(wfood.get(key)) * float(food.get(key)[1:])
        elif count == 2:
            temp_list.append("Harris Teeter")
            temp_list.append(key)
            temp_list.append(wfood.get(key))
            temp_list.append(f'{float(wfood.get(key)) * float(harris_teeter.get(key)[1:]):.2f}')
            buying_list.append(temp_list.copy())
            total += float(wfood.get(key)) * float(harris_teeter.get(key)[1:])
        elif count == 3:
            if food.get(key)[1:] >= harris_teeter.get(key)[1:]:
                temp_list.append("Food Lion")
                temp_list.append(key)
                temp_list.append(wfood.get(key))
                temp_list.append(f'{float(wfood.get(key)) * float(food.get(key)[1:]):.2f}')
                buying_list.append(temp_list.copy())
                total += float(wfood.get(key)) * float(food.get(key)[1:])
            else:
                temp_list.append("Harris Teeter")
                temp_list.append(key)
                temp_list.append(wfood.get(key))
                temp_list.append(float(wfood.get(key)) * float(harris_teeter.get(key)[1:]))
                buying_list.append(temp_list.copy())
                total += float(wfood.get(key)) * float(harris_teeter.get(key)[1:])
    for item in buying_list:
        string += f'\n{item[0]:20}{item[1]:19}{item[2]:16}{float(item[3]):6.2f}'
    string += f'\n{dash}\n                                                       {total:6.2f}'
    string += f'\n{dash}\nUnfound Items:'
    for item in no_stock:
        string += f'\n{item}'
    return string


if __name__ == '__main__':
    shopping_list = os.path.join("data", "List.txt")
    FoodLion = os.path.join("data","FoodLion.txt")
    Harris = os.path.join("data","HarrisTeeter.txt")

    bought = sort_shopping(shopping_list)
    LionFood = store_to_dict(FoodLion)
    Harris_Teeter = store_to_dict(Harris)

    print(prices(bought,LionFood,Harris_Teeter))
