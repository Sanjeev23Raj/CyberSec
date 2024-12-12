def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift within the bounds of A-Z or a-z
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
    shift_value = int(input("Enter the shift value: "))

    encrypted_text = caesar_cipher_encrypt(plaintext, shift_value)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)
    print("Decrypted Text:", decrypted_text)
