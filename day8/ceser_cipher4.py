alphabte=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceser(start_text,shift_amount,cipher_direction):
    end_text=""
    for letter in start_text:
        position=alphabte.index(letter)
        if cipher_direction=="decode":
            shift_amount*=-1
        new_position=position+shift_amount
        end_text+=alphabte[new_position]
    print(f"the {cipher_direction}d text is {end_text}")

continue_is=True
while continue_is:

    direction=input("Type 'encode' to encrpyt , type 'decode' to decrypt:\n")
    text=input("type your message:\n").lower()
    shift=int(input("type the shift number:\n"))
    shift=shift%25
    con=input("do you want to continue yes or no").lower()
    ceser(text,shift,direction)
    if con=="no":
        continue_is=False
        print("GoodBye")

    