

def main():

    print('Menu')

    print('-------------')
    table = ('1. Encode\n2. Decode\n3. Quit')
    print(table)
    menu_option = int(input('\nPlease enter an option: '))
    return menu_option


def encode(password):
    new_password=''
    for i in str(password):
        new_password += str((int(i)+3))
    return new_password

def decode(new_password):
    password = ''
    for i in str(new_password):
        password += str((int(i) - 3))
    return password

if __name__ == '__main__':

    password = None

    while True:
        menu_option = main()

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            new_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        if menu_option == 2:
            original_password = decode(new_password)
            print(f"The encoded password is {new_password}, and the original password is {original_password}.")
            print()

        if menu_option == 3:
            break












