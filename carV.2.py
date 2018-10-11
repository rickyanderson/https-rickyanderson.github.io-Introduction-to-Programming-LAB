class Toll(): #to declare Toll as a class
    def __init__(self):
        self.type1 = []  #so I can put the vehicle ini each of the array for each of the vehicle
        self.type2 = []
        self.type3 = []

    def getTotalVehicle(self):
        return "Car:", len(self.type1), " Bus: ", len(self.type2), " Truck: ", len(self.type3) #to show for each of the vehicle list

    def print_price_List(self):
        print ("Price List for Toll Ayam\nCar: Rp.6000\nBus: Rp.8000\nTruck: Rp.10000\n") #to tell the price list

    def getPriceCar(self):
        return int(6000)

    def carPrice(self):
        return "Fee :RP. 6000"

    def getPriceBus(self):
        return int(8000)

    def busPrice(self):
        return "Fee :RP. 8000"

    def getPriceTruck(self):
        return int(10000)

    def truckPrice(self):
        return "Fee :RP. 10000"

    def calculate_total_total(self):
        print("Rp."+str((self.getPriceCar() * len(self.type1))+(self.getPriceBus() * len(self.type2))+(self.getPriceTruck() * len(self.type3)))) #to get the total of the revenue

toll = Toll() #to delcare class Toll as toll
restart=0 #to set restart as 0
while restart == 0: #to do a looping if the restart is in 0
    toll.print_price_List() #to print the price list
    m=input("Next Vehicle?y/n:") #to do the looping
    if m == "y":
        n=input("Vehicle:")
        print()
        if n == "Car":
            toll.type1.append("ayam") #to put the car in the array
            print(toll.carPrice(),"\n") #to show the price of the vehicle

        elif n == "Bus":
            toll.type2.append("goreng")
            print(toll.busPrice(),"\n")
        elif n == "Truck":
            toll.type3.append("tepung")
            print(toll.truckPrice(),"\n")
        else:
            print("ERROR")
        restart = 0
    else:
        print (toll.getTotalVehicle()) #to show the current vehicle
        toll.calculate_total_total() #to calculate the total price
        print(len(toll.type1) + len(toll.type2) + len(toll.type3)) #to get the total vehicle
        print()
        print("END")
        restart += 1
        break #to stop the looping
