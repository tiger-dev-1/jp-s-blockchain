blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input("Please, enter your Transaction Amount: "))
    return user_input


def get_user_choice():
    user_input = input("Enter the Number of your Choice: ")
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print("Outputting Block")
        print(block)

tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print("Please, choose:")
    print("1 - Add a New Transaction ")
    print("2 - Output the Blockchain Blocks")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()

print("Done!")