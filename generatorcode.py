import random

def generate_cipher():
    """Generate a random cipher mapping for letters."""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    cipher = {chr(97+i): alphabet[i] for i in range(26)}
    return cipher

def encode_message(message, cipher):
    """Encode the message using the provided cipher."""
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += cipher[char]
            else:
                encoded_message += cipher[char.lower()].upper()
        else:
            encoded_message += char
    return encoded_message

if __name__ == "__main__":
    input_text = input("Enter the text to encode: ")
    
    # Generate a cipher mapping
    cipher = generate_cipher()
    print("Cipher Mapping:")
    for key, value in cipher.items():
        print(f"{key} => {value}")
    
    # Encode the input text
    encoded_text = encode_message(input_text, cipher)
    print("\nEncoded Message:")
    print(encoded_text)
