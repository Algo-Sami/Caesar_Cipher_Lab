# Caesar Cipher Program
# Course: Information Security
# Task: Encryption and Decryption using Caesar Cipher

# Function to encrypt the text
def caesar_encrypt(text, shift):
    encrypted_text = ""  # Empty string to store result
    
    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            # Convert letter to ASCII, shift it, and convert back
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        
        # Check if character is lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        
        # If not a letter (space, number, symbol), keep it same
        else:
            encrypted_text += char

    return encrypted_text


# Function to decrypt the text
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isupper():
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        
        elif char.islower():
            decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        
        else:
            decrypted_text += char

    return decrypted_text


# Main Program
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift_value)
    print("Encrypted Message:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift_value)
    print("Decrypted Message:", decrypted)