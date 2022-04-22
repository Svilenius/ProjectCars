def viewinventory(self):
    print ('\t'.join(['', 'Producer', 'Model', 'Year', 'Colour', 'Kilometer']))
    for idx, vehicle in enumerate(self):
        print (idx + 1, end = '\t')
        print(vehicle)