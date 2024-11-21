from shop import User, Address


class UserBuilder:
    def __init__(self):
        """Returns a default user named "bob" with address mail "bob@domain.tld". He's 18 and lives in Boston.
        He's verified.
        """
        self._name = "bob"
        self._email = "bob@domain.tld"
        self._age = 25
        self._address = Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")
        self._verified = True

    def result(self):
        return User(
            name=self._name,
            email=self._email,
            age=self._age,
            address=self._address,
            verified=self._verified,
        )

    def set_name(self, name: str):
        self._name = name
        return self

    def set_email(self, email: str):
        self._email = email
        return self

    def set_age(self, age: int):
        self._age = age
        return self

    def set_address(self, address: str):
        self._address = address
        return self

    def set_verified(self, verified: bool):
        self._verified = verified
        return self
