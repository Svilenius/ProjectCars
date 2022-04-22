print ('Automotive inventory')
from Functions import *
inventory = Inventory()
while True:
    print ("""
    #1 Add Vehicle to Inventory
    #2 Delete Vehicle from Inventory
    #3 View Current Inventory
    #4 Update Vehicle in Inventory
    #5 Export Current Inventory
    #6 Quit
    """)
    ans = input ('Please choose from one of the above options: ')
    if ans == "1":
        inventory.addvehicle()
    elif ans == "2":
        if len(inventory.vehicles) < 1:
            print ('There are no vehicles in the inventory currently')
            continue
        inventory.viewinventory()
        item = int(input('Please enter the inventory number of vehicle to be deleted: '))
        if item - 1 > len(inventory.vehicles):
            print ('There is not such vehile in the inventory')
        else:
            inventory.vehicles.remove(inventory.vehiles[item - 1])
            # Add a secondary confirmartion about deletion (Y/N)
            print()
            print('The selected vehicle has been deleted!')
    elif ans == "3":
        if len(inventory.vehicles) < 1:
            print ('There are no vehicles in the inventory currently')
            continue
        inventory.viewinventory()
    elif ans == "4":
        if len(inventory.vehicles) < 1:
            print ('There are no vehicles in the inventory currently')
            continue
        inventory.viewinventory()
        item = int(input('Please enter the inventory number of vehicle to be updated: '))
        if item - 1 > len(inventory.vehicles):
            print ('There is not such vehile in the inventory')
        else:
            automobile = Automobile()
            if automobile.addvehicle() == True:
                inventory.vehicles.remove (inventory.vehicles[item-1])
                inventory.vehicles.insert (item-1, automobile)
                print ()
                print ('The selected vehicle has been updated!')
    elif ans == "5":
        if len(inventory.vehicles) < 1:
            print ('There are no vehicles in the inventory currently')
            continue
        pass
    elif ans == "6":
        print ('Thanks you! Good bye and have a nice day!')
    else:
        print ("Invalid choose. Please try again!")