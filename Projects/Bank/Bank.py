accounts = {}

while True:
    print("\n1- Create Account")
    print("2- Deposit")
    print("3- Withdraw")
    print("4- Check Balance")
    print("5- Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Account name: ")
        if name in accounts:
            print("Account already exists!")
        else:
            accounts[name] = 0
            print("Account created!")

    elif choice == "2":
        name = input("Account name: ")
        if name in accounts:
            amount = float(input("Deposit amount: "))
            accounts[name] += amount
            print("Deposited successfully!")
        else:
            print("Account not found!")

    elif choice == "3":
        name = input("Account name: ")
        if name in accounts:
            amount = float(input("Withdraw amount: "))
            if amount <= accounts[name]:
                accounts[name] -= amount
                print("Withdraw successful!")
            else:
                print("Not enough balance!")
        else:
            print("Account not found!")

    elif choice == "4":
        name = input("Account name: ")
        if name in accounts:
            print("Balance:", accounts[name])
        else:
            print("Account not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
