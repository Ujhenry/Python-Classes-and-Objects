
class budget:

    def __init__(self, name, Deposite, Withdraw, Transfer,Check_balance, ):
     self.name = name
     self.deposite = Deposite
     self.withdraw = Withdraw
     self.transfer = Transfer
     self.check_balance = Check_balance

    def food(self):
        print('******* Food ********')
        print(f'Amount Deposited is {self.deposite}\nAmount withdraw is {self.withdraw} \nAmount transfered for the purchase of Food{self.transfer} \nAvailable balance after transacton {self.check_balance} ')

    def clothing(self):
        print('******** Clothing ********')
        print(f'Amount Deposited is {self.deposite}\nAmount withdraw is {self.withdraw} \nAmount transfered for the purchase Cloths {self.transfer} \nAvailable balance after transaction {self.check_balance} ')

    def entertainment(self):
        print('******** Entertainment ********')
        print(f'Amount Deposited is {self.deposite}\nAmount withdraw is {self.withdraw} \nAmount transfered for the purchase Cloths {self.transfer} \nAvailable balance after transaction {self.check_balance} ')

Category_1 = budget('Food',6000, 5000, 1000, 5000 )
Category_2 = budget('clothing', 10000, 5000, 3000, 2000)
Category_3 = budget('Entertainment', 5000, 2000, 1000, 1000)

Category_1.food()
Category_2.clothing()
Category_3.entertainment()
