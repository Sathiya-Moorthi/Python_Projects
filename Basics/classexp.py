class Bank:
    def __init__(self,accno,accname,balance):
        self.accno = accno
        print("Account No:", accno)
        self.accname = accname
        print("Account Holder Name:", accname)
        self.balance = balance
        print("Balance is:",balance)

    def balc(self,updateamt):
          self.updateamt=updateamt
          self.balance+=updateamt
          print("Updated Balance:",self.balance)
    def withdraw(self,drawamt):
          self.drawamt=drawamt
          print("withdraw amount is:",drawamt)
          amt=self.balance-drawamt
          print("after withdraw :", amt)
print("Enter the accno:")
n=int(input(""))
print("Enter the name:")
a=input("")
print("Enter the amount to be added:")
c=int(input(""))
print("Enter the amount to be added:")
d=int(input(""))
print("Enter the withdraw amount:")
e=int(input(""))
b=Bank(n,a,c)
b.balc(d)
b.withdraw(e)

