class Product:
    product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1

    def display_info(self):
        info = f"Product Name: {self.name}, Price: {self.price}, Total Products Created: {Product.product_count}"
        return info


class ElectronicProduct(Product):
    def __init__(self, name, price, warrantyPeriod):
        super().__init__(name, price)
        self.warrantyPeriod = warrantyPeriod

    def display_info(self):
        info = super().display_info()
        info += f", Warranty Period: {self.warrantyPeriod} months"
        return info


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        info = super().display_info()
        info += f", Size: {self.size}"
        return info


# Тестування функціональності
if __name__ == "__main__":
    # Створення продуктів
    product1 = Product("Generic Product", 10.99)
    electronic1 = ElectronicProduct("Laptop", 999.99, 24)
    clothing1 = ClothingProduct("T-Shirt", 19.99, "L")

    # Виведення інформації про продукти
    print(product1.display_info())
    print(electronic1.display_info())
    print(clothing1.display_info())

    # Перевірка загальної кількості створених продуктів
    print(f"Total Products Created: {Product.product_count}")