alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(message, cypher):
#     # 'encrypt' function
#     # shifts each letter of the 'text' forwards in the alphabet

#     encrypted = ""
#     for char in message:
#         i = alphabet.index(char)
#         if i <= 25 - cypher:
#             encrypted += alphabet[i+cypher]            
#         else:
#             encrypted += alphabet[cypher - (26 - i)]

#     print(f"The encrypted text is:  {encrypted}")


# def decrypt(coded_message, cypher):
#     # 'decrypt' function
#     # shifts each letter of the 'text' backwards in the alphabet 

#     decrypted = ""
#     for char in coded_message:
#         i = alphabet.index(char)
#         if i >= cypher:
#             decrypted += alphabet[i-cypher]
#         else:
#             decrypted += alphabet[-(cypher - i)]

#     print(f"The decrypted text is:  {decrypted}")

# if direction == "encode":
#     encrypt(message=text, cypher=shift)
# elif direction == "decode":
#     decrypt(code=text, cypher=shift)

def caesar(message, cypher, direc):
    
    output = ""

    if direc == "decode":
        cypher *= -1

    for char in message:
        if char in alphabet:
            i = alphabet.index(char)
            n = i + cypher
            output += alphabet[n]
        else:
            output += char
    
    print(f"\nThe {direc}d result:  {output}")


from art import logo
print(logo)

endProgram = False

while not endProgram:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    shift = shift % 26

    caesar(message=text, cypher=shift, direc=direction)

    restart = input("\n\nType 'yes' to go again. Ohterwise type 'no':\n")
    if restart == 'no':
        endProgram = True
        print("Goodbye")