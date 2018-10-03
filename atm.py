#Ricky Anderson
#Class ATM
print ("Welcome to Ayam Bank, a World Class Bank\n")
restart=('Y')
class Account(): #name the class as account
    def __init__(self,balanceParam):
        self.balance = balanceParam #element balance

    def get_balance(self):
        return self.balance #to get the current balance

    def deposit(self, moneyParam):
        self.balance += moneyParam #to put money in
        return print(self.balance)

    def pull_money(self, moneyParam):
        self.balance -= moneyParam #to take money
        return print(self.balance)

chances=3 #to limit the tries of pin into 3
while chances>=0: #if tries exceded 3 trimes the program continue to line 69
    pin= int(input("Enter your pin:")) #to detect the pin
    if pin == 1234: #if the pin is 1234 same as the set pin then continue the program
        a=float(input("How many money do you want to start with:")) #to determine the start of mone
        e = Account(a) #to use the class and set it to e
        while restart not in ('n'): #to do a looping until n is choosen
            print('Please Press 1 For Checking Your Balance')
            print('Please Press 2 To Put In')
            print('Please Press 3 To Withdrawl')
            print('Please Press 4 To Return Card\n')
            menuIn = int(input('What Would you like to do?:\n')) #to pick what do you want to do
            if menuIn == 1: #to determine the choosen menuIn
                print(e.get_balance()) #to print the current balance
                restart = input('Would You you like to do another transaction?(n for NO, y for YES): \n') #to determine what to do next if wanted to continue or not
                if restart in ('n'): #if the answer is n then do this
                    print("Please wait while your card is Returned...\n")
                    print("Thank you")
                    break #to end the looping
            elif menuIn == 2:
                moneyPut= float(input("Money to Put:\n")) #money to be put
                print("Please wait while your transaction is processing\n")
                e.deposit(moneyPut) #to add the nominal to current balance
                restart = input('Would You you like to do another transaction?(n for NO, y for YES): \n')
                if restart in ('n'):
                    print("Please wait while your card is Returned...\n")
                    print("Thank you")
                    break
            elif menuIn == 3:
                withdraw=float(input("Money to Take:\n")) #money to be take
                print("Please wait while your transaction is processing\n")
                if withdraw > int(e.get_balance()): #so the money doesn't go minus
                    print("Not enough money")
                else:
                    e.pull_money(withdraw) #to minus the nominal to current balance
                restart = input('Would You you like to do another transaction?(n for NO, y for YES): \n')
                if restart in ('n'):
                    print("Please wait while your card is Returned...\n")
                    print("Thank you")
                    break
            elif menuIn == 4:
                print("Please wait while your card is Returned...\n")
                print("Thank you")
                break
            else:
                print("error, returning card")
                break
    elif pin != ('1234'): #if the input of pin isn't 1234 then do the below
        print('Incorrect Password')
        chances = chances - 1 #to decrease the current chance by 1
        if chances == 0: #if the chance is 0 then print below
            print('\nNo more tries')
            break
#the end
