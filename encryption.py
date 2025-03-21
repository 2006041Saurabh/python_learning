def encrypt(text, shift,alphabet):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            place = alphabet.index(letter)
            new_place = (place + shift) % len(alphabet)  # Wrap around using modulo
            encrypted_text += alphabet[new_place]
        else:
            encrypted_text += letter  # Keep non-alphabet characters as they are
    return encrypted_text

def decrypt(text, shift, alphabet):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            place = alphabet.index(letter)
            new_place = (place - shift) % len(alphabet)  # Wrap around using modulo
            decrypted_text += alphabet[new_place]
        else:
            decrypted_text += letter  # Keep non-alphabet characters as they are
    return decrypted_text


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Enter encode to encrypt or decode to decrypt\n").lower()
text = input("Enter your message\n").lower()
shift = int(input("Enter the shift number"))



if direction == "encode":
    result = encrypt(text, shift, alphabet)
    print(f"Encrypted message: {result}")
elif direction == "decode":
    result = decrypt(text, shift, alphabet)
    print(f"Decrypted message: {result}")
else:
    print("Invalid direction. Please enter 'encode' or 'decode'.")