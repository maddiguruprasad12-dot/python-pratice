#Mini-project for Bank-Statement
balance=0
def deposite():
    amount=int(input("enter a amount:"))
    if amount>0:
        print("amount"+str(amount)+'/-credited sucessfully')
        return amount
    else:
        print("invalid amount")
        return 0
def with_draw():
    amount=int(input("enter a withdraw amount:"))
    if amount<=balance:
        print("amount"+str(amount)+'/- debited sucessfully!')
        return amount
    else:
        print("insufficient amount!")
def check_balance():
    print("your balance"+str(balance)+'/-')

def check_credentials():
    db_pin=1234
    chances=3
    for i in range(1,chances+1):
        input_pin=int(input("enter a your pin:"))
        if db_pin==input_pin:
            return True
        else:
            if chances-i!=0:
                print("wrong pin,yiu have only" +str(chances-i) +'chances left!')
            else:
                return False
print('<-----WELCOME TO BANK MANAGEMENT SYSTEM----->')
if check_credentials()==True:
    while True:
        print('\n1) Deposite')
        print('2) Withdraw')
        print('3) Check Balance')
        print('4) Exit')
        choice=int(input("enter your choice:"))
        match choice:
            case 1:
                balance+=deposite()
            case 2:
                balance-=with_draw()
            case 3:
                check_balance()
            case 4:
                print("THANK YOU FOR VISITING AGAIN...!")
                break
            case _:
                print("Invalid choice,try again...!")
else:
    print("your account got blocked! Try after 24hrs...!")


