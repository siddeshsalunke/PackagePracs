class Wheels:
    def __init__(self):
        self.wheel = ['TWO', 'FOUR']
 
 
    def printwheel(self):
        print('Select Category')
        for wheel in self.wheel:
            print('\t%s ' % wheel)