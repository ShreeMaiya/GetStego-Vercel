import wave
import numpy as np
import random
import zipfile
import os
import tempfile
from datetime import datetime

def generate_key():
    """
    Generates a random 5-digit key for encoding message.
    """
    return random.randint(10000, 99999)

def encode_lsb_video(video_file_path, message):
    key = generate_key()
    print("Key:", key)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        key_file_path = os.path.join(temp_dir, 'key_video.txt')
        with open(key_file_path, 'w') as file:
            file.write(str(key))

        video_array = np.fromfile(video_file_path, dtype=np.uint8)
        message_binary = ''.join(format(ord(c), '08b') for c in message)

        key_binary = format(key, '020b')  # Convert key to 20-bit binary representation

        message_binary = key_binary + message_binary  # Append key binary to message binary
        message_binary += '00000000'

        if len(message_binary) > len(video_array):
            raise ValueError('Message is too long to fit in the video file')

        video_array_copy = video_array.copy()

        for i in range(len(message_binary)):
            video_array_copy[i] = (video_array_copy[i] & ~1) | int(message_binary[i])  # Clear the least significant bit and set it to the message bit

        encoded_video_file_path = os.path.join(temp_dir, 'encoded_video.mp4')
        with open(encoded_video_file_path, 'wb') as file:
            file.write(video_array_copy.tobytes())

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_file_path = os.path.join(tempfile.gettempdir(), f'encoded_video_result_{timestamp}.zip')
        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            # Add the video file to the zip archive
            zip_file.write(encoded_video_file_path, os.path.basename(encoded_video_file_path))

            # Add the text file to the zip archive
            zip_file.write(key_file_path, os.path.basename(key_file_path))

    print('Message successfully encoded in video file.')
    return zip_file_path

def decode_lsb_video(encoded_video_file_path, key):
    with open(encoded_video_file_path, 'rb') as file:
        encoded_video_array = np.frombuffer(file.read(), dtype=np.uint8)

    key_binary = ''
    for byte in encoded_video_array[:20]:  # Extract first 20 bytes for key binary
        key_binary += str(byte & 1)

    extracted_key = int(key_binary, 2)  # Convert key binary to integer

    if str(key) != str(extracted_key):
        print("Key does not match. Decoding failed.")
        return None

    message_binary = ''
    for byte in encoded_video_array[20:]:  # Start from 21st byte for message binary
        message_binary += str(byte & 1)

    message = ''
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i + 8]
        if byte == '00000000':
            break
        char = chr(int(byte, 2))
        message += char

    return message.strip()

if __name__ == '__main__':
    encode_lsb_video("cover_video.mp4", input("Message: "))    
    print(decode_lsb_video("encoded_video.mp4", int(input("Key: "))))