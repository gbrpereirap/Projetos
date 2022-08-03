from eCommerce import Projeto_eCommerce
import re


def valida_valores(valor):
    if re.search(r'^-?[0-9]+\.[0-9]+$', valor):
        return True
    elif re.search(r'^-?[0-9]+$', valor):
        return True
    return False


def valida_nomes(nomes):
    if nomes not in '':
        return True
    return False


def lendo_nome():
    while True:
        nome = str(input('Entre com o nome do produto: ')).strip().title()
        if valida_nomes(nome):
            return nome


def lendo_valor():
    while True:
        valor = input('Entre com o valor do produto: ')
        if valida_valores(valor):
            return float(valor)
        else:
            print('\033[0;31mERRO! Digite um numero.\033[m')


def registration_menu(products_includes):
    while True:
        opcao = input("1 - Adicionar Produtos\n2 - Remover Produtos\n3 - Mostar produtos Cadastrados"
                      "\n4 - Sair\nEscolha uma opção: ")
        if valida_valores(opcao):
            opcao = int(opcao)
            if opcao == 1:
                products_includes.get_product(lendo_nome(), lendo_valor())
            elif opcao == 2:
                products_includes.delete_product(lendo_nome())
            elif opcao == 3:
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
        if valida_valores(option):
            option = int(option)
            if option == 1:
                get_cart = lendo_nome()
                try:
                    shopping_cart.insert_cart_product(get_cart, products_includes.product['products'][get_cart])
                except KeyError:
                    print('\033[0;31mOpção invalida. Produto não cadastrado\033[m')
            elif option == 2:
                get_cart = lendo_nome()
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
        if valida_valores(option):
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
