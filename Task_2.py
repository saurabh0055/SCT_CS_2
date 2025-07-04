from PIL import Image
import random

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR each channel with key
            pixels[x, y] = (
                r ^ key,
                g ^ key,
                b ^ key
            )
    img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Same function, XOR again to decrypt
    encrypt_image(input_path, output_path, key)

def shuffle_pixels(input_path, output_path):
    img = Image.open(input_path)
    pixels = list(img.getdata())
    random.shuffle(pixels)
    img.putdata(pixels)
    img.save(output_path)
    print(f"Shuffled image saved as {output_path}")

# Example usage:
# Encrypt:
encrypt_image("input_image.png", "encrypted_image.png", key=123)

# Decrypt:
decrypt_image("encrypted_image.png", "decrypted_image.png", key=123)

# Shuffle:
shuffle_pixels("input_image.png", "shuffled_image.png")