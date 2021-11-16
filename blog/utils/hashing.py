from passlib.context import CryptContext

pswd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hashing():
    def get_hashed_password(password: str):
        return pswd_cxt.hash(password)

    def verify(plain_password: str, hashed_password: str):
        return pswd_cxt.verify(plain_password, hashed_password)