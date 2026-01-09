class Car:
         
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(Car):
    def __init__(self , name):
        self.name = name

car1 = toyotacar("fortuner")
print(car1.name)
car1.start()
car1.stop()