alphabte=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrpyt , type 'decode' to decrypt:\n")
text=input("type your message:\n").lower()
shift=int(input("type the shift number:\n"))

def encrpyt(plain_text,shift_amount):
    for letter in plain_text:
        position=alphabte.index(letter)
        new_position=position+shift_amount
        cipher_text=""
        cipher_text+=alphabte[new_position]
    print(cipher_text) 

encrpyt(text,shift)


def decrypt(cipher_text,shift_amount):
    for letter in cipher_text:
        position=alphabte.index(letter)
        new_position=position-shift_amount
        normal=""
        normal+=alphabte[new_position]
    print(normal) 


if direction=="encode":
   encrpyt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("please enter correct")