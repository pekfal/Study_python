from cryptography.fernet import Fernet
import base64

def generate_key():
    """암호화 랜덤 키 생성"""
    return Fernet.generate_key()


def encrypt_message(message, key):
    """메세지 암호화"""
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypt_message

def decrypt_message(encrypt_message, key):
    """암호화된 메세지 복호화"""
    f = Fernet(key)
    decrypt_message = f.decrypt(encrypt_message).decode()
    return decrypt_message

key = generate_key()  # 키 생성
message = "This is a secret message."  # 암호화할 메시지
encrypted = encrypt_message(message, key)  # 메시지 암호화
decrypted = decrypt_message(encrypted, key)  # 메시지 복호화

print(f"Original message: {message}")  # 원본 메시지 출력
print(f"Encrypted message: {encrypted}")  # 암호화된 메시지 출력
print(f"Decrypted message: {decrypted}")  # 복호화된 메시지 출력
