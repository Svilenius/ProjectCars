def addvehicle(self):
    vehicle = Automobile()
    if vehicle.addvehicle() == True:
        self.vehicle.append(vehicle)
        print ()
        print ('New vehicle has been added. Thank you!')
