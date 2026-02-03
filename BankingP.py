
def show_balance(balance):
    print(f"Your balance is : ${balance:.2f}")

def deposit():
    amount = input("Enter an amount to deposit: ")
    if amount.isdigit():
        amount = float(amount)
        if amount < 0:
            print("That's not a valid amount")
            return 0
        else:
            return amount
    else:
        return 0

def withdraw(x):
    amount = input("Enter an amount to withdraw: ")
    if amount.isdigit():
        amount = float(amount)
        if amount < 0:
            print("That's not a valid amount")
            return 0
        elif amount > x:
            print("Inffuicient Funds!")
            return 0
        else:
            return amount
    else:
        return 0
def main():
    balance = 0
    is_running = True

    while is_running:
        print("***************************")
        print("------BANKING PROGRAM------")
        print("***************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***************************")
        choice = input("Please enter the number of your choice(1-4): ")
        print("***************************")
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("***************************")
                print("Please enter a valid number!")
        print("***************************")

    print("Thank you! Have a nice day!")
    print("***************************")

if __name__ == '__main__':
    main()