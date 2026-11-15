
import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():

         with open(database) as fs:
            data = json.loads(fs.read())
        else:
           print("No such files exists ")

    except Exception as err:
        print(f"an Exception occured as {err}")

    @staticmethod
    def update():
            with open(Bank.database, 'w') as fs:
              fs.write(json.dumps(Bank.data))


    @staticmethod
    def __Accountgenerate():
         alpha = random.choices(string.ascii_letters, k = 3)
         num = random.choices(string.digits, k = 3)
         spchar = random.choices("!@#$%^&*", k = 1)
         id = alpha + num + spchar
         random.shuffle(id)
         return "".join(id)



    def createaccount(self):
        info = {
            "Name": input("Tell me your name :"),
            "age": int(input("Tell your age :")),
            "email": input("Tell your email :"),
            "pin": int(input("Tell your pin :")),
            "accNo.": Bank.__Accountgenerate(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, You cannot create your account.")
        else:
                        print("Account has been created successfully.")

                        for i in info:
                            print(f"{i} : {info[i]}")
                        print("Please note down your account number")

                        Bank.data.append(info)

            

                        Bank.update()


    def depositemoney(self):
        accnumber = input("Tell your Account number :")
        pin = int(input("Tell your pin as well :"))

        userdata = [
            account for account in Bank.data
            if account['accNo.'] == accnumber and account['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")
        else:
            amount = int(input("How much you want to deposit? "))
            if amount > 10000 or amount <= 0:
                print("Sorry, you can deposit an amount above 0 and up to 10000")
            else:
                userdata[0]['balance'] += amount
                Bank.update()
                print("Amount deposited successfully")

    
    def withdrawmoney(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your PIN: "))

        userdata = [
        i for i in Bank.data
        if i.get('accNo.', i.get('accountNo.')) == accnumber
        and int(i['pin']) == pin
    ]

        if not userdata:
            print("Sorry, no account found.")

        else:
            try:
                amount = int(input("How much do you want to withdraw? "))
            except ValueError:
                print("Please enter a valid amount.")
                return

            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")

            elif userdata[0]['balance'] < amount:
                print("Sorry, you don't have enough money.")

            else:
                userdata[0]['balance'] -= amount
                Bank.update()
                print("Amount withdrawn successfully!")
                print("Remaining balance:", userdata[0]['balance'])



    
    def showdetails(self):
        accnumber = input("Please tell your account number: ")
        pin = input("Please tell your PIN: ")

        userdata = [
            i for i in Bank.data
            if i.get('accNo.', i.get('accountNo.')) == accnumber
            and str(i['pin']) == pin
        ]

        if not userdata:
            print("Sorry, no account found.")
            return

        print("\nYour account information:\n")

        for key, value in userdata[0].items():
            if key == "pin":
                print("PIN: ****")
            else:
                print(f"{key}: {value}")



        
    def updatedetails(self):
        accnumber = input("Please tell your account number: ").strip()
        pin = input("Please tell your PIN: ").strip()

        userdata = [
            i for i in Bank.data
            if i.get('accNo.', i.get('accountNo.')) == accnumber
            and str(i['pin']) == pin
        ]

        if not userdata:
            print("No such user found.")
            return

        account = userdata[0]

        print("You cannot change the age, account number, or balance.")
        print("Fill in the details to change, or press Enter to skip.")

        new_name = input("Enter new name or press Enter: ").strip()
        new_email = input("Enter new email or press Enter: ").strip()
        new_pin = input("Enter new PIN or press Enter: ").strip()

        if new_name:
            account['Name'] = new_name

       
        if new_email:
            account['email'] = new_email

        
        if new_pin:
            if not new_pin.isdigit() or len(new_pin) != 4:
                print("PIN must contain exactly 4 digits.")
                return
            account['pin'] = int(new_pin)

        Bank.update()
        print("Details updated successfully!")



        
    def Delete(self):
        accnumber = input("Please tell your account number: ").strip()
        pin = input("Please tell your PIN: ").strip()

        userdata = [
            i for i in Bank.data
            if i.get('accNo.', i.get('accountNo.')) == accnumber
            and str(i['pin']) == pin
        ]

        if not userdata:
            print("Sorry, no such account exists.")
            return

        check = input(
            "Are you sure you want to delete your account? "
            "Press Y to confirm or N to cancel: "
        ).strip().upper()

        if check == 'N':
            print("Account deletion cancelled.")
        elif check == 'Y':
            Bank.data.remove(userdata[0])
            Bank.update()
            print("Account deleted successfully!")
        else:
            print("Invalid choice. Account deletion cancelled.")


user = Bank()
print("Press 1 for creating an account")
print("Press 2 for Depositing the money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for  fetching the details ")
print("Press 5 for updating the details")
print("Press 6 for deactivate your account")

check = int(input("Tell your response :"))

if check == 1:
    user.createaccount()
    
if check == 2:
    user.depositemoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()



