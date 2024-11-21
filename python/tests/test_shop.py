from shop import Shop
from user_builder import UserBuilder


def test_happy_path():
    user = UserBuilder().build()

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    user = UserBuilder().set_as_minor().build()

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified():
    user = UserBuilder().set_as_non_verified().build()

    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee():
    user = UserBuilder().set_as_foreign_user().build()

    assert Shop.must_pay_foreign_fee(user)
