class Car(object):
    def __init__(self,color,model,speed,company):
        self.color=color
        self.model=model
        self.speed=speed
        self.company=company
    def start(self):
        print('started')
    def stop(self):
        print('stoped')
    def accelarate(self):
        print('accelarating')

oudi = Car('red','A6',100,'oudi')
print(oudi.color)
print(oudi.start())

bmw = Car('white','M63',20,'bmw')
print(bmw.model)
