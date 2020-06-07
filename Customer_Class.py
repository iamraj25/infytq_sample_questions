# Create a class Customer having data members as cid , name ,balance ,
# Initialize the customer account with custemer id ,name and opening amount . Opening amount must be >=500
# Create setter for name
# Create getter for all data members

# Create a method deposit() which takes some amount as argument and add into balance.
# If amount passed is lesser than or equal to 0 then throw an error message

# Create a method withdraw() which takes some amount as argument and deduct the amount from balance.
# If amount asked to withdraw is more than balance then throw an error msg.
# Sorry ! Not enough Balance . Unable to withdraw

# Create a customer with the data taken from user as cid , name and opening amount.
# Show the account information of the Customer as -
# Customer ID:<cid> , Name:<name>, Balance:<balance>

# Take some amount to be withdrawn from user and called withdraw() Function

# Show the account info of customer
# Customer ID:<cid> , Name:<name>, Balance:<balance>


class Customer:
    def __init__(self):
        self.cid = 1
        self.name = "Raj"
        self.balance = 500

    def set_name(self, name):
        self.name = name

    def get_data(self):
        print("Customer ID:" + str(self.cid) + " , Name:" + self.name + " , Balance:" + str(self.balance))

    def deposit(self, amount):
        if amount <= 0:
            print("Error In Amount Entered ")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry ! Not enough Balance . Unable to withdraw")
        else:
            self.balance -= amount

    def new_customer(self, id, name, amount):
        self.cid = id
        self.name = name
        self.balance = amount
        print("Customer ID:" + str(self.cid) + " , Name:" + self.name + " , Balance:" + str(self.balance))


C = Customer()
_id = int(input("Enter ID"))
_name = input("Enter Name")
_amount = int(input("Enter Opening Balance"))
C.new_customer(_id, _name, _amount)
amount = int(input("Amount to be withdrawn"))
C.withdraw(amount)
C.get_data()
