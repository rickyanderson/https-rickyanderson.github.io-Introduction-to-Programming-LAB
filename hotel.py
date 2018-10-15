#Ricky Anderson Ricco
#Hotel quiz
class Hotel(object): # set a class as Hotel
    def __init__(self):
        #setting the number for the current situation
        self.single = 0
        self.double = 0
        self.deluxe = 0
        self.presidensuite = 0
        #setting the number from the first until the end
        self.single2 = 0
        self.double2 = 0
        self.deluxe2 = 0
        self.presidensuite2 = 0
    #to tell the price they need to pay if the check out
    def single(self):
        print("Price you need to pay: Rp. 580000\n")
    def double(self):
        print("Price you need to pay: Rp. 700000\n")
    def deluxe(self):
        print("Price you need to pay: Rp. 980000\n")
    def presidensuite(self):
        print("Price you need to pay: Rp. 1300000\n")
        #to get the total revenue of the day
    def revenue(self):
        print("Total Revanue of the Day: ",(self.single2*580000)+(self.double2*700000)+(self.deluxe2*980000)+(self.presidensuite2*1300000))
        #to get the current number of the room in used
    def total(self):
        print("Currently resserved room","(","Single:", self.single, "Double:", self.double, "Deluxe:", self.deluxe, "President Suite", self.presidensuite,")")

class Person(Hotel):
    def __init__(self, slotparams = 0, slotparamd = 0, slotparamde = 0, slotparamp = 0):
        Hotel.__init__(self)
        #to limit the room max number in used
        self.x = slotparams
        self.y = slotparamd
        self.z = slotparamde
        self.a = slotparamp
    #for the check in program
    def masuk(self):
        if kelas == "Single":
            if self.x < 5:
                self.single += 1
                self.single2 += 1
                self.x += 1
            else:
                print("Full")
        elif kelas == "Double":
            if self.y < 5:
                self.double += 1
                self.double2 += 1
                self.y += 1
            else:
                print("Full")
        elif kelas == "Deluxe":
            if self.z < 3:
                self.deluxe += 1
                self.deluxe2 += 1
                self.z += 1
            else:
                print("Full")
        elif kelas == "President Suite":
            if self.a < 2:
                self.presidensuite += 1
                self.presidensuite2 += 1
                self.a += 1
            else:
                print("Full")
        else:
            print("No Such Room")
    #for the check out program
    def keluar(self):
        if kelas == "Single":
            if self.x > 0:
                self.single -= 1
                Hotel.single(self)
                self.x -= 1
            else:
                print("Empty\n")
        elif kelas == "Double":
            if self.y > 0:
                self.double -= 1
                Hotel.double(self)
                self.y -= 1
            else:
                print("Empty\n")
        elif Kelas == "Deluxe":
            if self.z >0:
                self.deluxe -= 1
                Hotel.deluxe(self)
                self.z -= 1
            else:
                print("Empty\n")
        elif kelas == "President Suite":
            if self.a > 0:
                self.presidensuite -= 1
                Hotel.presidensuite(self)
                self.a -= 1
            else:
                print("Empty\n")
        else:
            print("No Such Room")
restart = 0
print("Welcome to Ayam Hotel")
print("Room list:\n","Single: Rp. 580000\n","Double: Rp. 700000\n","Deluxe: Rp. 980000\n","President Suite: Rp. 1300000\n")
hotel = Hotel() #to set class
person = Person() #to set class
while restart == 0: #to do the looping
    print()
    end =input("End Day?(y/n):\n") #to process if wanted to input checkin/checkout or wanthed the total revanue
    if end == "n":
        check = input("Checkin/Checkout:(in/out)") #to decide if cehckin/checkout
        if check == "in":
            kelas =input("Room choose:")
            print()
            person.masuk() #to use the masuk module
            person.total() #to get the total current from the module
            restart = 0
        elif check == "out":
            kelas =input("Room choose:")
            print()
            print("                         Billing")
            print("=========================================================")
            print()
            person.keluar() #to use the keluar module
            print()
            print("=========================================================")
            person.total() #to get the total current module
            restart = 0
        else:
            print("Your statement is not defined")
            restart = 0
    elif end == "y":
        print("                     Total Revenue")
        print("=========================================================")
        print()
        person.revenue() #to get the total revenue of the day
        print()
        print("=========================================================")
        restart += 1
        break #to end the looping
    else:
        print("your statement is not defined")
        restart = 0

