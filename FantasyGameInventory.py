stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Function that displays the sum of items in a players inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item_type, item_quantity in inventory.items():
        print(str(item_quantity) + ' ' + item_type)
        item_total += item_quantity
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

#Function to add items from a list of loot to a player's inventory
def addToInventory(inventory, loot_crate):
  for loot in loot_crate:
    # add the key (item name) to the dictionary
    inventory.setdefault(loot, 0)
    # increment the value of that item by one
    inventory[loot] += 1
  return inventory

treasure_chest = {'gold coin': 42, 'rope': 1}
displayInventory(treasure_chest)
loot_box = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'saphire']
treasure_chest = addToInventory(treasure_chest, loot_box)
displayInventory(treasure_chest)
