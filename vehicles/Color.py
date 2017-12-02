class Color:
    def __init__(self):
        self.members = ['Red', 'White', 'Black', 'Gray']

    def printColors(self):
        print('Available Colors')
        for color in self.members:
            print('\t%s ' % color)