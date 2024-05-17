class Bank:
    def __init__(self,accno,accname,balance):
        self.accno = accno
        self.accname = accname
        self.balance = balance

    def balc(self,updateamt):
          self.updateamt=updateamt
          self.balance+=updateamt
          print(self.balance)
    def withdraw(self,drawamt):
          self.drawamt=drawamt
          amt=self.balance-drawamt
          if amt>1000:
              print(amt)
          else:
              print("No Adequate balance")
n=int(input(""))
a=input("")
c=int(input(""))
d=int(input(""))
e=int(input(""))
b=Bank(n,a,c)
b.balc(d)
b.withdraw(e)