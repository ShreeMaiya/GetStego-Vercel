import os
import random
import zipfile
import tempfile
from datetime import datetime
from PIL import Image

def encode_lsb_image(image_path, message):
    # Open the image file
    image = Image.open(image_path).convert("RGB")

    # Check if the image is big enough to hide the message
    width, height = image.size
    message_length = len(message) * 8 + 5  # Include space for the key
    if message_length > (width * height * 3):
        raise ValueError("Text too long for chosen image.")

    # Generate a random key
    key = str(random.randint(10000, 99999))
    
    with tempfile.TemporaryDirectory() as temp_dir:
        key_file_path = os.path.join(temp_dir, 'key_image.txt')
        with open(key_file_path, 'w') as file:
            file.write(str(key))

        # Normalize the original image
        pixels = image.load()
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r - (r % 2), g - (g % 2), b - (b % 2))

        # Convert the message to a binary string
        binary_message = ""
        for char in message:
            binary_char = bin(ord(char))[2:].zfill(8)
            binary_message += binary_char

        # Add the key to the binary message
        binary_message = key + binary_message

        # Apply the binary string to the image
        counter = 0
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                if counter < len(binary_message):
                    r += int(binary_message[counter])
                    if counter + 1 < len(binary_message):
                        g += int(binary_message[counter + 1])
                    if counter + 2 < len(binary_message):
                        b += int(binary_message[counter + 2])
                    counter += 3
                    pixels[i, j] = (r, g, b)
                else:
                    break

        # Save the encoded image
        encoded_img_path = os.path.join(temp_dir, 'encoded_image.png')
        image.save(encoded_img_path)

        # Define the timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        zip_file_path = os.path.join(tempfile.gettempdir(), f'encoded_image_result_{timestamp}.zip')
        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            # Add the image file to the zip archive
            zip_file.write(encoded_img_path, os.path.basename(encoded_img_path))
            # Add the text file to the zip archive
            zip_file.write(key_file_path, os.path.basename(key_file_path))

    return zip_file_path

def decode_lsb_image(image_path, key):
    # Open the encoded image file
    image = Image.open(image_path).convert("RGB")

    # Extract the binary message from the image
    pixels = image.load()
    binary_message = ""
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            binary_message += str(r % 2)
            binary_message += str(g % 2)
            binary_message += str(b % 2)

    # Split the key and message
    key_length = 5
    key = binary_message[:key_length]
    binary_message = binary_message[key_length:]

    # Convert the binary message to ASCII
    output = ""
    for i in range(0, len(binary_message), 8):
        binary_char = binary_message[i:i + 8]
        char_code = int(binary_char, 2)
        output += chr(char_code)

    # Remove trailing whitespace or null characters
    output = output.rstrip("\0").rstrip()

    # Check if the decoded key matches the provided key
    if key != key:
        raise ValueError("Invalid key provided. Decoding unsuccessful.")

    return output

if __name__ == '__main__':
    zip_file_path = encode_lsb_image("cover_image_small.jpg", "This is a secret message.")
    print(f"Encoded image and key saved in: {zip_file_path}")
    print(decode_lsb_image("encoded_image.png", input("Key:")))
