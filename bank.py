def show_balance(balance):
    print("*"*40)
    print(f"Your balance is ${balance :.2f}")
    print("*"*40)

def deposit():
    print("*"*40)
    amount= float(input("Enter an amount to be deposited :$ "))
    print("*"*40)
    if amount <0:
        print("Invalid Amount")
        return 0

    else :
        return amount    

def withdraw(balance):
    print("*"*40)
    amount= float(input("Enter an amount to be withdrawn :$ "))
    print("*"*40)

    if amount > balance:
        print("Insufficient finds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount    

def main():    

  balance =0
  is_running =True

  while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*"*40)

    choice=input('Enter your choice (1-4)  :')
    #print("*"*40)

    if choice =='1':
        show_balance(balance)
    elif choice=='2':
        balance += deposit()
    elif choice =='3':
        balance -= withdraw(balance)
    elif choice=='4' :
        print("*****Thank You !! Have a nice day !! *****")
        is_running=False
    else:
        print("*"*40)
        print('====Invalid choice====')    
        print("*"*40)
  

if __name__=='__main__':
 main()      


    