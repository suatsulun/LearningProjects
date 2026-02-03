import random, string

def encrypt():
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {cipher_text}")
    return

def decrypt():
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Original message: {cipher_text}")
    print(f"Encrypted message: {plain_text}")
    return

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

is_running = True

while is_running:
    print("--Encryption - Decryption program--")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    pick = input("Please pick an option 1-3: ")

    match pick:
        case "1":
            encrypt()
        case "2":
            decrypt()
        case "3":
            is_running = False
        case _:
            print("Please enter a valid option!")