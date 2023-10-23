alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from cipher_art import logo
print(logo)



def caeser(start_text , shift_by , direction_given):
    end_text = ''
    if shift_by > 26:
        shift_by = shift_by%26
    if direction_given == 'decode':
        shift_by *= -1 
    
    for ch in start_text:
        current_letter = ch
        
        if current_letter in alphabet:
    
            current_idx_in_aplhbet = alphabet.index(current_letter)
            new_idx = current_idx_in_aplhbet + shift_by

            if new_idx > 25 :
                new_idx-=26
            elif new_idx <0 :
                new_idx = 26 + new_idx

            new_letter = alphabet[new_idx]
        
        else:
            new_letter = current_letter;

        end_text += new_letter

    print(end_text)
    


should_continue = True;
while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(start_text=text ,shift_by=shift , direction_given=direction)

    continue_or_not = input("Do you want to continue : 'Y' for Yes | 'N' for No ")
    if continue_or_not =='Y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caeser(start_text=text ,shift_by=shift , direction_given=direction)

    else:
        print('Good Bye!')
        should_continue = False
      
    





