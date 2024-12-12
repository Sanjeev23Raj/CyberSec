from PIL import Image
import random

def encrypt_image(image_path, key):
    """Encrypts an image by modifying pixel values."""
    image = Image.open(image_path)
    pixels = list(image.getdata())  # Get image pixels as a list
    random.seed(key)  # Seed random number generator with the key

    encrypted_pixels = [
        (pixel[0] ^ random.randint(0, 255),  # XOR each channel with a random number
         pixel[1] ^ random.randint(0, 255),
         pixel[2] ^ random.randint(0, 255))
        for pixel in pixels
    ]

    # Create a new encrypted image
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    """Decrypts an image encrypted using the encrypt_image function."""
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_pixels = list(encrypted_image.getdata())
    random.seed(key)  # Use the same key to decrypt

    decrypted_pixels = [
        (pixel[0] ^ random.randint(0, 255),  # XOR each channel with the same sequence
         pixel[1] ^ random.randint(0, 255),
         pixel[2] ^ random.randint(0, 255))
        for pixel in encrypted_pixels
    ]

    # Create a new decrypted image
    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

# Example usage
if __name__ == "__main__":
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = int(input("Choose an option (1/2): "))

    if choice == 1:
        image_path = input("Enter the path to the image to encrypt: ")
        key = input("Enter a key for encryption: ")
        encrypt_image(image_path, key)
    elif choice == 2:
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        key = input("Enter the key used for encryption: ")
        decrypt_image(encrypted_image_path, key)
    else:
        print("Invalid choice!")
