balance = 0
def main():
    balance = 0 # local variable
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Blance:", balance)

def deposit(n):
    global balance
    balance += n



def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()