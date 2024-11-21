from shop import Shop
from user_builder import UserBuilder


def test_happy_path(fsf_address):
    user = UserBuilder().result()

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(fsf_address):
    user = UserBuilder().set_age(16).result()

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified(fsf_address):
    user = UserBuilder().set_verified(False).result()

    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee(paris_address):
    user = UserBuilder().set_address(paris_address).result()

    assert Shop.must_pay_foreign_fee(user)
