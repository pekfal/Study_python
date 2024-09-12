def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
        
    return result

plaintext = input("암호화할 텍스트를 입력하세요: ")

while True:
    try:
        shift = int(input("시프트할 정수를 입력하세요 (-26 ~ 25): "))
        if -26 <= shift <= 25:
            break
        else:
            print("시프트할 정수는 -26 ~ 25 사이여야 합니다.")
    except ValueError:
        print("시프트할 수는 정수로 입력하세요.")

encrypted_text = caesar_cipher(plaintext, shift)
print(f"\n암호화된 텍스트: {encrypted_text}")

decrypt_option = input("\n복호화하시겠습니까? (y/n): ").lower()
if decrypt_option == 'y':
    decrypted_text = caesar_cipher(encrypted_text, -shift)
    print(f"복호화된 텍스트: {decrypted_text}")