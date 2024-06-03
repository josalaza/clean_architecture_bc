class Cart:
    def __init__(self):
        self.products = []

    def adicionar_producto(self, product, price):
        if price < 0:
            raise ValueError("El precio no puede ser negativo")
        self.products.append((product, price))

    def eleiminar_producto(self, product):
        self.products = [p for p in self.products if p[0] != product]

    def calcular_total(self):
        total = sum(price for _, price in self.products)
        for _, price in self.products:
            if price > 100:
                total -= price * 0.10
        return total