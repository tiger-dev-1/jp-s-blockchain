blockchain = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transacion(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [1]
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

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            # print(block)
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid

        
while True:
    print("\nPlease, choose:\n")
    print("1 - Add a New Transaction ")
    print("2 - Output the Blockchain Blocks")
    print("3 - Quit\n")

    user_choice = get_user_choice()

    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transacion(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "3":
        break
    else:
        print("\nINVALID INPUT!!! Please, pick a value from the list.")
    if not verify_chain():
        print("\nINVALID BLOCKCHAIN!!!")
        break

print("\nDone!")