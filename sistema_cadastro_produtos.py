"""
Projeto sistema de um mercado

Um menu de opções ao usuario(a), onde é possível fazer 5 escolhas: Adicionar, Remover,
mostrar os produtos cadastrados(Tambem o produto mais caro e o mais barato), pesquisar e sair.
"""
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


def adiciona_produtos(produtos):  # Adiciona os produtos e valores digitados pelo usuario(a) no dict, retornado a adição
    escolha = ' '

    while escolha != 'N':
        nome = lendo_nome()
        valor = lendo_valor()
        produtos[nome] = valor
        escolha = ' '
        while escolha not in "SN":
            escolha = input('Deseja adicionar mais produtos [S/N]: ').strip().upper()

    return produtos


def remove_produtos(produtos):  # Função que remove a chave e o valor do produto escolhido, retornando o dict atualizado
    while True:
        remove = input('Digite o nome do produto que deseja remover?: ').strip().title()
        if valida_nomes(remove):
            if remove in produtos:
                del produtos[remove]
                return produtos
            else:
                print('\033[0;31mO produto não esta cadastrado.\033[m')
        else:
            print('\033[0;31mPor favor, digite algo. Pesquisa em branco invalida!\033[m')


def prod_cadastrados(produtos):
    mais_caro = max(produtos, key=produtos.get)  # Pega a chave do maior valor do dict e armazena na variavel
    mais_barato = min(produtos, key=produtos.get)  # Pega a chave do menor valor do dict e armazena na variavel

    print(40 * '-')
    for produto, valor in produtos.items():
        print(f'O Produto: {produto}, Valor: {valor:.2f}')
    print(f'O produto mais caro é: {mais_caro}, custando: {produtos[mais_caro]:.2f}')
    print(f'O produto mais barato é: {mais_barato}, custando: {produtos[mais_barato]:.2f}')
    print(40 * '-')


def pesquisa_produto(produtos):
    escolha = ' '

    while escolha != 'N':
        pesquisa = str(input('Qual produto deseja pesquisar?: ')).strip().title()
        if valida_nomes(pesquisa):
            if pesquisa in produtos:
                print(f'O produto pesquisado foi {pesquisa} e seu valor é {produtos[pesquisa]:.2f}')
                escolha = ' '
                while escolha not in "SN":
                    escolha = input('Deseja p esquisar mais produtos [S/N]: ').strip().upper()
            else:
                print('\033[0;31mO produto não esta cadastrado.\033[m')
        else:
            print('\033[0;31mPor favor, digite algo. Pesquisa em branco invalida!\033[m')


def menu():
    cadastro = {}

    print('Bem vindo ao sistema de cadastros de produtos.')
    print(40 * '-')

    while True:
        opcao = input('1 - Adicionar Produtos\n2 - Remover Produtos\n3 - Produtos Cadastrados\n4 - Pesquisa Produto'
                      '\n5 - Sair\nEscolha uma opção: ')
        if valida_valores(opcao):
            opcao = int(opcao)
            if opcao == 1:
                if not cadastro:  # Usado para executar uma condição False, ou seja, o dict vazio tera valores
                    # adicionados
                    cadastro = adiciona_produtos(cadastro)
                else:  # Caso não esteja vazia, ele adiciona os novos valores ao dict ja criado
                    cadastro.update(adiciona_produtos(cadastro))
            elif opcao == 2:
                if not cadastro:
                    print('\033[0;31mNenhum produto cadastrado.\033[m')
                else:
                    cadastro = remove_produtos(cadastro)
            elif opcao == 3:
                if not cadastro:
                    print('\033[0;31mNenhum produto cadastrado.\033[m')
                else:
                    prod_cadastrados(cadastro)
            elif opcao == 4:
                if not cadastro:
                    print('\033[0;31mNenhum produto cadastrado.\033[m')
                else:
                    pesquisa_produto(cadastro)
            else:
                print('\033[0;31mVocê escolheu sair, Ate mais !!\033[m')
                break
        else:
            print('\033[0;31mOpção invalida.\033[m')


if __name__ == '__main__':
    menu()
