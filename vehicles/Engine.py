class Engine:
    
    def __init__(self):
        pass
 
 
    def twoWheelerEngine(self):
        ccRange = ['110','150','200','250']
        print ("Available Engine in CC")
        for cc in ccRange:
            print('\t%s ' % cc)

    def fourWheelerEngine(self):
        power = ['1000','1200','1500','2200']
        print ("Available power in cars")
        for getpower in power:
            print('\t%s' % getpower)