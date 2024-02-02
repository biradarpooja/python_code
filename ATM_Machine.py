 #1)Withdraw 2)diposite only 10000,3)check balance 4)change pin old passwor=new password
class WrongPwd(Exception):
    pass
class LimitDe(Exception):
    pass
amount=50000
print("Welcome to DCC bank")
print("your amount is:",amount)
pin=123
while True:
    upin=int(input("Enter your pin:"))
    try:
        if upin!=pin:
            raise WrongPwd("INvalid password error")
    except WrongPwd as k:
         print(k)
    else:
        print("Correct Password")
        choice=input("Enter your choice:-")
        if choice=='a':
            a=int(input("Enter amount withdraw:-"))
            try:
                if a>amount:
                    raise Invalid("Out of amount")
            except Invalid as i:
                print(i)
            else:
                amount=amount-a
            finally:
                print("Current balence is:",amount)
        elif choice=='b':

            b=int(input("Enter amount you want to diposite"))
            try:
                if b>10000:
                    raise LimitDe("Cannot deposite more than 10000")
            except LimitDe as k:
                print(k)
            else:
                b=b+amount
                print("your total amount is:",amount)
            finally:
                print("after adding deposite Current balance is:",b)
        elif choice=='c':
            print("Total Amount is:",amount)
        elif choice=='d':
            print("change pin")
            newpin=int(input("Enter new pin:"))
            confirmpin=int(input("Enter your confirm pin:"))
            if newpin==confirmpin:
                print("your pin is succesfully Updated")
            else:
                print("your pin is not confirm")
        else:
            print("Invalid input")
            break
        ch=input("Do You want to continue")
        if ch=="yes":
            continue
        else:
            print("Thank you for visiting atm machine")
            break
        if ch=="no":
            break




        
