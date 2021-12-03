from argon2 import PasswordHasher


class Argon2PasswordHasher:

    def __init__(self) -> None:
        self.ph = PasswordHasher()

    def hash(self, raw_password: str) -> str:
        return self.ph.hash(raw_password)

    def validate_password(self, raw_password: str, hashed_password: str) -> bool:
        return self.ph.verify(hashed_password, raw_password)
