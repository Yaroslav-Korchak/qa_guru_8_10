"""
Протестируйте классы из модуля homework/models.py
"""
import pytest


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        equal_quantity = product.quantity
        product.buy(equal_quantity)
        assert product.quantity == 0, 'failed with equal quantity'

        less_quantity = product.quantity - 1
        product.buy(less_quantity)
        assert product.quantity == 1


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        bigger_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            assert product.buy(bigger_quantity) is ValueError, 'failed when quantity is bigger'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_to_cart(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1

    def test_add_to_not_empty_cart_successful(self, not_empty_cart, product):
        not_empty_cart.add_product(product, 1)
        assert not_empty_cart.products[product] == 11

    @pytest.mark.parametrize('quantity', [11, 12, ""])
    def test_remove_product_successful(self, quantity, product, cart):
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_product_not_in_cart_with_assertion_error(self, product, cart):
        with pytest.raises(ValueError):
            cart.remove_product(product)
            assert cart.remove_product(product) is ValueError

    def test_clear(self,cart, product):
        cart.add_product(product, 500)
        cart.add_product('шляпы', 20)
        cart.clear()
        assert cart.products == {}, 'cart is not empty'

    def test_get_total_price(self, product, not_empty_cart):
        assert not_empty_cart.get_total_price() == 1010

    def test_buy_product_in_cart(self, product, not_empty_cart):
        not_empty_cart.buy()
        assert product.quantity == 990

    def test_buy_more_than_exist(self,product, cart):
        cart.add_product(product, product.quantity +1)
        with pytest.raises(ValueError):
            assert cart.buy() is ValueError ,'You are trying to buy more than we have'