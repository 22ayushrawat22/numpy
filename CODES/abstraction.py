class Account():
    def __init__(self , balance , acc_no):
        self.balance = balance 
        self.acc_no = acc_no

    def debit(self , amount):
        self.balance-= amount
        print("Rs" , amount , "has been debited")
        print("final balance is : ",self.getbalance())

    def credit(self , amount):
        self.balance+= amount
        print("Rs" , amount , "has been credited")
        print("final balance is : ",self.balance())

    def getbalance(self):
        return self.balance
    
acc1 = Account(10000 , 12345)
acc1.debit(1000)