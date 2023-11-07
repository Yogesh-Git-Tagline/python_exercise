"""Create the following class with given fuctionality"""

#class Creation
class BankAccount:
    def __init__(self,name,acc_num,balance,pin):  #constructor assign the values comes by parameter
        self.account_holder_name=name
        self.account_number=acc_num
        self.balance=balance
        self.pin=pin
        #values are assigned with parameter which will send while object creation

    def check_pin(self):                        #this method checks user enterd pin with defined pin
        user_pin=int(input("Enter Pin:"))       #it takes the pin from user as int
        if(user_pin==self.pin):                 #checking user pin with defined pin
            return True                         #user enterd correct pin then it return true
        return False                       
        
    def deposit(self,amount):                   #this method is for deposit the amount in bank
        if(self.check_pin()):                   #first it will check the pin of user is correct or not 
                self.balance=self.balance+amount #then it will add the deposit amount in balance
                print(amount,"rupees added to account successfully")
        else:
            print("You Entered Wrong Pin...")   #when user enterd wrong pin

    def withdraw(self,amount):                  #this method is for withdraw the amount in bank
        if(self.check_pin()):                    #first it will check the pin of user is correct or not 
            if(amount>self.balance):            #then it checkes amount is grater than balance
                print("Your account don't have sufficient balance")   #when user have not that much balance
            else:
                self.balance=self.balance-amount    #amount will be substract from remaining balance
                print(amount,"rupees has been withdrawn successfully")
        else:
            print("You Entered Wrong Pin...")          #when user enterd wrong pin

    def __str__(self):  #this just disaply the information which we pass while object initialization
        return f"Account Holder Name:{self.account_holder_name} \nAccount Number:{self.account_number} \nTotal Balance:{self.balance}"


#object creation and passing the user information as an arguments
b1=BankAccount(name="Ram",acc_num="12345", balance=1000, pin=3456)
print(b1)            #displaying the information before deposit and withdraw money
b1.deposit(100)      #calling the deposit method to add 100Rs in bank
b1.withdraw(200)     #calling the withdraw method to withdraw 200Rs
print(b1)            #displaying the information after deposit and withdraw money
