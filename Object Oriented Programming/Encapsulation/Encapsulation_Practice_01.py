class Account:
    def __init__(self,balance):
        self.__balance = balance

    def show_balance(self):
        print('Balance:',self.__balance)
    
    def deposit(self,balance):
        self.__balance += balance  

acc=Account(1000)
acc.show_balance()
acc.deposit(500)
acc.show_balance()

acc.__balance =99999
acc.show_balance()
print(acc.__dict__)

acc.deposit(50000)
acc.show_balance()