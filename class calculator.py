class cal():
    def __init__(self,satu,dua): #to innitiate the needed variable
        self.a=satu
        self.b=dua
    #to set the calculating proccess in the class
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
#to input number that going to be proccess
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Choose choice to make:\n","1) add\n","2) substract\n","3) multiply\n","4) divide\n")
choice=(input("enter choice:"))#to input choice of what to do with the number
obj=cal(a,b) #to set the class as obj
#to determine which choices to make
if choice == "1":
    print(obj.add())
elif choice == "2":
    print(obj.sub())
elif choice == "3":
    print(obj.mul())
elif choice == "4":
    print(obj.div())
else:
    print("error")

print()
