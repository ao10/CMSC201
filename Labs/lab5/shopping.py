#File: shopping.py
#Author: Ati Ok
#Date: March 7th, 2016
#Section: 15
#Email: ao10@umbc.edu

def main():
    shoppingList = []
    item = input("Add item to list ('done' when finished): ")
    if (item != 'done'):
        shoppingList.append(item)
    while (item != 'done'):
        item = input("Add item to list ('done' when finished): ")
        if (item != 'done'):
            shoppingList.append(item)
    print(shoppingList)

    itemCost = []
    
    for x in range(len(shoppingList)):
        itemCost.append(float(input("How much did " + shoppingList[0] + " cost? ")))
        shoppingList.remove(shoppingList[0])

    total = 0
    for y in itemCost:
        total += y
    print("Your shopping trip cost: $", total)
    print("Your shopping list at end of trip: ", shoppingList)    
main()
 
