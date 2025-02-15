import art
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
            ' ', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-']

def caesar(input_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in input_text:
        if letter not in characters:
            output_text += letter
        else:
            shifted_position = characters.index(letter) + shift_amount
            shifted_position %= len(characters)
            output_text += characters[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

print(art.logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    done = input("Do you want to Continue or Quit?\n").lower()
    if done.find('q') != -1:
        break
