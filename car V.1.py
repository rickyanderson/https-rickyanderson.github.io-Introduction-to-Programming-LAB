class Toll(): #to declare Toll as a class
    def print_price_List(self):
        print ("Price List for Toll Ayam\nCar: Rp.6000\nBus: Rp.8000\nTruck: Rp.10000\n") #to tell the price list

    def carPrice(self):
        return "Fee :RP. 6000"

    def busPrice(self):
        return "Fee :RP. 8000"

    def truckPrice(self):
        return "Fee :RP. 10000"

toll = Toll() #to delcare class Toll as toll
restart=0 #to set restart as 0
while restart == 0: #to do a looping if the restart is in 0
    toll.print_price_List() #to print the price list
    m=input("Next Vehicle?y/n:") #to do the looping
    if m == "y":
        n=input("Vehicle:")
        print()
        if n == "Car":
            print(toll.carPrice(),"\n") #to show the price of the vehicle
        elif n == "Bus":
            print(toll.busPrice(),"\n")
        elif n == "Truck":
            print(toll.truckPrice(),"\n")
        else:
            print("ERROR")
        restart = 0
    else:
        print()
        print("END")
        restart += 1
        break #to stop the looping
