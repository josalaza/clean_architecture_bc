Feature: Carrito de Compras

  Scenario: Add product with price greater than $100
    Given an empty cart
    When I add a product with price 150
    Then the total should be 135