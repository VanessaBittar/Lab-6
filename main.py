

def main():

    print('Menu')

    print('-------------')
    table = ('1. Encode\n2. Decode\n3. Quit')
    print(table)
    menu_option = int(input('\nPlease enter an option:'))
    return menu_option


def encode(password):
    new_password=''
    for i in str(password):
        new_password += str((int(i)+3))
    return new_password


#def decode(password):
    #int(input('\nPlease enter an option:'))
    #new_password = ''
    #for i in password :
        #new_password -= (int(i)-3) % 10
    #return new_password

if __name__ == '__main__':

    password = None

    while True:
        menu_option = main()

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")

        if menu_option == 3:
            break












