from argon2 import PasswordHasher


class Argon2PasswordHasher:

    def __init__(self) -> None:
        self.ph = PasswordHasher()

    def hash(self, raw_password: str) -> str:
        return self.ph.hash(raw_password)

    def validate_password(self, raw_password: str, hashed_password: str) -> bool:
        return self.ph.verify(hashed_password, raw_password)


if __name__ == "__main__":
    hasher = Argon2PasswordHasher()
    hashed = hasher.hash("123456aa")
    print(hashed)
    res = hasher.validate_password("123456aa", hashed)
    print(res)