import hashlib


def hash_passwd(raw_password: str) -> str:
    password = hashlib.sha256(raw_password.encode(encoding='utf-8')).hexdigest()
    return password


def verify_password(password: str, hashed_password: str) -> bool:
    return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest() == hashed_password
