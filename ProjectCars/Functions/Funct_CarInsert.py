def addvehicle(self):
    try:
        self._producer = input('Enter vehicle producer: ')
        self._model = input('Enter vehicle model: ')
        self._year = input('Enter vehicle year: ')
        self._colour = input('Enter vehicle colour: ')
        self._kilometers = input('Enter vehicle km: ')
        return True
    except ValueError:
        print ('Please enter a whole number for year and kilometers. Please try again!')
        return False