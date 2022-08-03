from eCommerce import Projeto_eCommerce
import re


def value_validate(value):
    if re.search(r'^-?[0-9]+\.[0-9]+$', value):
        return True
    elif re.search(r'^-?[0-9]+$', value):
        return True
    return False


def names_validate(names):
    if names not in '':
        return True
    return False


def get_name():
    while True:
        name = str(input('Entre com o nome do produto: ')).strip().title()
        if names_validate(name):
            return name


def get_value():
    while True:
        value = input('Entre com o valor do produto: ')
        if value_validate(value):
            return float(value)
        else:
            print('\033[0;31mERRO! Digite um numero.\033[m')


def registration_menu(products_includes):
    while True:
        option = input("1 - Adicionar Produtos\n2 - Remover Produtos\n3 - Mostar produtos Cadastrados"
                       "\n4 - Sair\nEscolha uma opção: ")
        if value_validate(option):
            option = int(option)
            if option == 1:
                products_includes.get_product(get_name(), get_value())
            elif option == 2:
                products_includes.delete_product(get_name())
            elif option == 3:
                products_includes.display_register_products()
            else:
                break
        else:
            print('\033[0;31mOpção invalida.\033[m')


def purchase_menu(products_includes):
    shopping_cart = Projeto_eCommerce.Cart()
    while True:
        print("Produtos cadastrados: ")
        products_includes.display_register_products()
        option = input(
            "1 - Adicionar Produtos ao carrinho\n2 - Remover Produtos do carrinho\n3 - Mostar produtos do carrinho"
            "\n4 - Sair\nEscolha uma opção: ")
        if value_validate(option):
            option = int(option)
            if option == 1:
                get_cart = get_name()
                try:
                    shopping_cart.insert_cart_product(get_cart, products_includes.product['products'][get_cart])
                except KeyError:
                    print('\033[0;31mOpção invalida. Produto não cadastrado\033[m')
            elif option == 2:
                get_cart = get_name()
                shopping_cart.delete_cart_produtos(get_cart)
            elif option == 3:
                shopping_cart.show_cart_products()
                print(shopping_cart.sum_cart_total())
            else:
                break


def main_menu():
    registration_products = Projeto_eCommerce.Product()
    while True:
        option = input("1 - Menu de cadastro de produtos\n2 - Menu de compras\n3 - Sair\nEscolha "
                       "uma opção: ")
        if value_validate(option):
            option = int(option)
            if option == 1:
                registration_menu(registration_products)
            elif option == 2:
                if registration_products.product:
                    purchase_menu(registration_products)
                else:
                    print('\033[0;31mNenhum produto cadatrados.\033[m')
            else:
                break


if __name__ == '__main__':
    main_menu()
