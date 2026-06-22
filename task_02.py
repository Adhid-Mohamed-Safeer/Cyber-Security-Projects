from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)

    img.save("encrypted_image.png")
    print("Encrypted image saved as encrypted_image.png")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)

    img.save("decrypted_image.png")
    print("Decrypted image saved as decrypted_image.png")


choice = input("Encrypt or Decrypt (E/D): ").upper()
path = input("Enter image path: ")
key = int(input("Enter key: "))

if choice == "E":
    encrypt_image(path, key)
elif choice == "D":
    decrypt_image(path, key)