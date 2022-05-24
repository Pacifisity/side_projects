class ProductOne():
    pass
class ProductTwo():
    pass
class ProductThree():
    pass

def create_product():
    products = [ProductOne(), ProductTwo(), ProductThree()]
    types = ProductTwo()
    for i in products:
        if types == i:
            return types
print(create_product())