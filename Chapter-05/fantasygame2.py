dct={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
count=0
def displayInventory(inventory):
    item_total=0
    for i,j in inventory.items():
        print(j,i)
        item_total+=j
    print(item_total)
displayInventory(dct)

print('==========================================================================================')
        
def addToInventory(inventory, addedItems):
        for item in addedItems:
            inventory.setdefault(item, 0) 
            inventory[item] += 1 
        return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)