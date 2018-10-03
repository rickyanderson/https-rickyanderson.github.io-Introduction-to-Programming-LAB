class cal():
    def __init__(self,satu,dua):
        self.a=satu
        self.b=dua
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
choice=(input("enter choice:"))
obj=cal(a,b)
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
