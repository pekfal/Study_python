def vigenere_encrypt(plain_text, key):
    encrypted_text = []
    plain_text= plain_text.upper()
    key = key.upper()

    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plain_text_as_int = [ord(i) for i in plain_text]
    
    for i in range(len(plain_text)):
        shifted_char = (plain_text_as_int[i] + key_as_int[i % key_length]) % 26 + 65
        encrypted_text.append(chr(shifted_char))
    
    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    encrypted_text_as_int = [ord(i) for i in encrypted_text]
    
    for i in range(len(encrypted_text)):
        shifted_char = (encrypted_text_as_int[i] - key_as_int[i % key_length]) % 26 + 65
        decrypted_text.append(chr(shifted_char))
    
    return ''.join(decrypted_text)
    

def main():
    while True:
        mode = input("Choose Encrypt, Decrypt or Quit. E, D, Q :").upper()

        if  mode == 'E':
            plain_text = input("Enter the plain text: ")
            key = input("Enter the key: ")
            encrypted_text = vigenere_encrypt(plain_text, key)
            print(f"Encrypted Text: {encrypted_text}")

        elif mode == 'D':
            encrypted_text = input("Enter the encrypted text: ")
            key = input("Enter the key: ")
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            print(f"Decrypted Text: {decrypted_text}")

        elif mode == 'Q':
            break

        else:
            print("Invalid mode. Please enter E for encryption or D for decryption.")

if __name__ == "__main__":
    main()

