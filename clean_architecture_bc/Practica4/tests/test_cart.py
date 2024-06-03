import pytest
from pytest_bdd import scenarios, given, when, then
import clean_architecture_bc.Practica4.src.entidades.cart as carrito


def test_adicionar_producto():
    cart = carrito.Cart()
    cart.adicionar_producto("Producto 1", 50)
    assert len(cart.products) == 1
    assert cart.calcular_total() == 50

def test_eliminar_producto():
    cart = carrito.Cart()
    cart.adicionar_producto("Producto 1", 50)
    cart.eleiminar_producto("Producto 1")
    assert len(cart.products) == 0

def test_adicionar_producto_negativo():
    cart = carrito.Cart()
    with pytest.raises(ValueError):
        cart.adicionar_producto("Producto 1", -50)

def test_adcionar_producto_descuento():
    cart = carrito.Cart()
    cart.adicionar_producto("Producto 1", 150)
    assert cart.calcular_total() == 135

scenarios('test_cart.feature')

@pytest.fixture
def cart():
    return carrito.Cart()

@given('an empty cart')
def step_impl(cart):
    cart.products = []

@when('I add a product with price 150')
def step_impl(cart):
    cart.add_product("Producto 1", 150)

@then('the total should be 135')
def step_impl(cart):
    assert cart.calculate_total() == 135
