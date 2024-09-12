def vigenere_encrypt(plain_text, key):
    """
    비즈네르 암호화 함수
    """
    encrypted_text = []
    plain_text = plain_text.upper()
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plain_text_as_int = [ord(i) for i in plain_text]

    for i in range(len(plain_text)):
        if 65 <= plain_text_as_int[i] <= 90:  # 대문자 알파벳인 경우에만 처리
            shifted_char = (plain_text_as_int[i] + key_as_int[i % key_length] - 2 * 65) % 26 + 65
            encrypted_text.append(chr(shifted_char))
        else:
            encrypted_text.append(plain_text[i])  # 알파벳이 아닌 경우 그대로 추가

    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    """
    비즈네르 복호화 함수
    """
    decrypted_text = []
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    encrypted_text_as_int = [ord(i) for i in encrypted_text]

    for i in range(len(encrypted_text)):
        if 65 <= encrypted_text_as_int[i] <= 90:  # 대문자 알파벳인 경우에만 처리
            shifted_char = (encrypted_text_as_int[i] - key_as_int[i % key_length] + 26) % 26 + 65
            decrypted_text.append(chr(shifted_char))
        else:
            decrypted_text.append(encrypted_text[i])  # 알파벳이 아닌 경우 그대로 추가

    return ''.join(decrypted_text)

def find_whitespace(original_text):
    """
    공백 문자의 위치를 찾는 함수
    """
    whitespace_positions = []
    for i, char in enumerate(original_text):
        if char == ' ':
            whitespace_positions.append(i)
    return whitespace_positions

def restore_whitespace(text, whitespace_positions):
    """
    공백 문자의 위치를 복원하는 함수
    """
    text_with_spaces = list(text)
    for pos in whitespace_positions:
        text_with_spaces.insert(pos, ' ')
    return ''.join(text_with_spaces)

def main():
    while True:
        mode = input("Choose Encrypt, Decrypt or Quit (E, D, Q): ").upper()

        if mode == 'E':
            plain_text = input("Enter the plain text: ")
            key = input("Enter the key: ")
            whitespace_positions = find_whitespace(plain_text)
            plain_text_no_spaces = plain_text.replace(" ", "")
            encrypted_text = vigenere_encrypt(plain_text_no_spaces, key)
            encrypted_text_with_spaces = restore_whitespace(encrypted_text, whitespace_positions)
            print(f"Encrypted Text: {encrypted_text_with_spaces}")

        elif mode == 'D':
            encrypted_text = input("Enter the encrypted text: ")
            key = input("Enter the key: ")
            whitespace_positions = find_whitespace(encrypted_text)
            encrypted_text_no_spaces = encrypted_text.replace(" ", "")
            decrypted_text = vigenere_decrypt(encrypted_text_no_spaces, key)
            decrypted_text_with_spaces = restore_whitespace(decrypted_text, whitespace_positions)
            print(f"Decrypted Text: {decrypted_text_with_spaces}")

        elif mode == 'Q':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose 'E' for encrypt, 'D' for decrypt or 'Q' to quit.")

if __name__ == "__main__":
    main()
