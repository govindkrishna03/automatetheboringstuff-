dct={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
count=0
def displayInventory(inventory):
    item_total=0
    for i,j in inventory.items():
        print(j,i)
        item_total+=j
    print(item_total)
displayInventory(dct)

        