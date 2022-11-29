import pytest


class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def create_user_in_db(self):
        print(f"--------User {self.name} in DB created------")
        return True

    def remove_user_in_db(self):
        print(f"\nUser {self.name} in DB removed")
        return True
