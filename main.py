def show_balance(balance):
    print(f"Your balance is UGX{balance:.2f}")


def deposit():
    print("==========================")
    amount = float(input("ENTER DEPOSIT AMOUNT: "))
    print("==========================")

    if amount < 0:
        print("Invalid Amount!")
        return 0
    else:
        return amount


def withdraw(balance):
    print("==========================")
    amount = float(input("ENTER WITHDRAW AMOUNT: "))
    print("==========================")

    if amount > balance:
        print("Insuffient Funds!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0!")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("==========================")
        print("BANKING PROGRAM")
        print("==========================")
        print("1. Show Balance\n")
        print("2. Deposit\n")
        print("3. Withdraw\n")
        print("4. Exit\n")
        print("==========================")

        choice = input("SELECT CHOICE: ")
        print("==========================")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid Choice!")

    print("Alright, Have a nice day!")


if __name__ == "__main__":
    main()
