alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text , shift_by):


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
   
        cipher_text =''
        for i in range(len(plain_text)): 
            current_letter = plain_text[i] 

            idx_of_current_letter_in_26letters = alphabet.index(current_letter)
            new_idx = idx_of_current_letter_in_26letters + shift_by

            if new_idx>25:
                new_idx = new_idx-26
            new_letter = alphabet[new_idx]
            
            # print(f"new letter is {new_letter}")

            cipher_text += new_letter;
        print(f"The encoded text is {cipher_text}")
    

def decrypt(cipher_text, shift_by):
    
    decode_text =''
    for i in range(len(cipher_text)): 
        current_letter = cipher_text[i] 

        idx_of_current_letter_in_26letters = alphabet.index(current_letter)
        new_idx = idx_of_current_letter_in_26letters - shift_by

        if new_idx<0:
            new_idx = 26 + new_idx
        new_letter = alphabet[new_idx]
        
        decode_text += new_letter;
    print(f"The decoded text is {decode_text}")

    

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

if direction == 'encode':
    encrypt(plain_text=text,shift_by=shift)
elif direction == 'decode':
    decrypt(cipher_text=text , shift_by=shift)