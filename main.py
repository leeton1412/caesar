alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# take the parameters into caesar
def caesar(function, plain_text, shift_amount):
    # set empty variable
    cipher_text = ""
    #for each letter in the text
    for letter in plain_text:
        #get the index of the letter in the alphabet list
        posistion = alphabet.index(letter)
        # if its encode, + the posistion else - and append to cipher_text
        if function == "encode":
            new_index = posistion + shift_amount
            cipher_text += alphabet[new_index]
        else:
            new_index = posistion - shift_amount
            cipher_text += alphabet[new_index]
    #Print results
    print(f"Your text is {cipher_text}")


caesar(direction, text, shift)
