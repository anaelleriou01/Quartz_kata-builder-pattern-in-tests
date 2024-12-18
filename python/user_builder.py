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

    def build(self):
        return User(
            name=self._name,
            email=self._email,
            age=self._age,
            address=self._address,
            verified=self._verified,
        )

    def set_as_minor(self):
        self._age = 16
        return self

    def set_as_non_verified(self):
        self._verified = False
        return self

    def set_as_foreign_user(self):
        self._address = Address("33 quai d'Orsay", "", "Paris", "75007", "France")
        return self
