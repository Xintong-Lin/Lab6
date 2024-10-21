# Course: COP3502C
# Name: Xintong Lin
# Date: 19 October 2024
# Description: This program includes an encoder and decoder
#              for an 8-digit password.

def encode(password):
    encoded_password = ''
    for digit in password:
        new_digit = int(digit) + 3
        if new_digit >= 10:
            new_digit -= 10
        encoded_password += str(new_digit)
    return encoded_password

def decode(password):
    pass

if __name__ == '__main__':
    while True:

        # Display a menu and prompts user for option
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = int(input('Please enter an option: '))

        # Selection structure to determine message
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, '
                  f'and the original password is {password}.\n')
        elif option == 3:
            break