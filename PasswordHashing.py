import bcrypt

def hash_password(password):
    # 비밀번호를 바이트로 인코딩
    password_bytes = password.encode('utf-8')
    
    # salt 생성 및 해싱
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    return hashed_password

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

# 사용 예:
password = "mysecurepassword123"
hashed = hash_password(password)
print(f"Hashed password: {hashed}")

# 검증
is_correct = verify_password(password, hashed)
print(f"Password is correct: {is_correct}")