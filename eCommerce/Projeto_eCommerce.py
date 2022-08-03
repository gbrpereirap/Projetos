class Product:
    def __init__(self):
        self.product = {}
        self.name = ""
        self.valor = 0

    def get_product(self, name, valor):
        self.name = name
        self.valor = valor
        if "products" not in self.product:
            self.product["products"] = {self.name: self.valor}
        else:
            self.product["products"].update({self.name: self.valor})

    def display_register_products(self):
        try:
            print("-" * 40)
            for name, valor in self.product["products"].items():
                print(f"\033[0;31mNome: {name}    Valor: {valor:.2f}\033[m")
                print("-" * 40)
        except KeyError:
            print('\033[0;31mProduto não cadastrado.\033[m')

    def delete_product(self, name):
        try:
            del self.product["products"][name]
        except KeyError:
            print('\033[0;31mProduto não cadastrado.\033[m')


class Cart:
    def __init__(self):
        self.cart_products = {}

    def insert_cart_product(self, itens_name, itens_valor):
        if "products" not in self.cart_products:
            self.cart_products["products"] = {itens_name: itens_valor}
        else:
            self.cart_products["products"].update({itens_name: itens_valor})

    def show_cart_products(self):
        try:
            print("-" * 40)
            for name, valor in self.cart_products["products"].items():
                print(f"\033[0;31mNome: {name}    Valor: {valor:.2f}\033[m")
                print("-" * 40)
        except KeyError:
            print('\033[0;31mProduto não cadastrado.\033[m\n')

    def delete_cart_produtos(self, name):
        try:
            if self.cart_products:
                del self.cart_products["products"][name]
            else:
                print('\033[0;31mO carrinho está vazio.\033[m\n')
        except KeyError:
            print('\033[0;31mProduto não cadastrado.\033[m\n')

    def sum_cart_total(self):
        if not self.cart_products:
            return
        total = 0
        for name, valor in self.cart_products["products"].items():
            total += valor
        return f"\033[0;31mValor total do carrinho: {total:.2f}\033[m\n"


