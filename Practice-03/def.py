#class product digital physical
#name price # get info # get total product class
#total products = 0
#dig file size
#phys weight
class Product:
    total_products = 0
    def __init__(self, name, price, get_total_products = 0):
        self.name = name
        self.price = price
        Product.total_products += 1
    def get_info(self):
        return f"{self.name} costs {self.price} $"
    def get_total_products(self):
        return f"Total products: {self.total_products}"
class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size
    def get_info(self):
        return f"{self.name} costs {self.price} $ and has a file size of {self.file_size} GB"
class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    def get_info(self):
        return f"{self.name} costs {self.price} $ and weights {self.weight} kg"
a = Product("Laptop", 1000)
b = DigitalProduct("Website", 50, 2.5)
c = PhysicalProduct("Food", 20, 1.2)

print(a.get_info())
print(b.get_info())
print(c.get_info())

print(a.get_total_products())
    





