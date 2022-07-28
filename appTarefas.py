"""
Um app de lista de tarefas, onde é possivel adicionar uma nova tarefa,
remover e alterar o status da mesma.
"""


def cria_nova_tarefa(tarefas, status='inconcluido'):
    titulo = input('Entre com o titulo da tarefa: ')
    adicionar_tarefa = input('Digite sua tarefa: ')
    tarefas.append({titulo: adicionar_tarefa, 'status': status})


def mostra_tarefa(tarefas):
    print('-' * 40)
    for linhas in tarefas:
        for status, trf in linhas.items():
            print(f'{status}: {trf}')
        print('-' * 40)


def alterar_status(tarefas):
    if not tarefas:
        print('Nenhuma tarefa adicionada')
    else:
        linha = int(input('Em qual linha você deseja alterar para concluido?: '))
        if tarefas[linha - 1]['status'] == 'inconcluido':
            tarefas[linha - 1]['status'] = 'concluido'
        else:
            tarefas[linha - 1]['status'] = 'inconcluido'


def remover_tarefa(tarefas, removidas):
    if not tarefas:
        print('Nenhuma tarefa adicionada')
    else:
        removido = tarefas.pop()
        removidas.append(removido)


def refaz_remocao(tarefas, removidas):
    if not removidas:
        print('Nenhuma tarefa foi removida')
    else:
        refazer = removidas.pop()
        tarefas.append(refazer)


def menu():
    lista_de_tarefas = []
    tarefa_removida = []
    while True:

        opcao = int(input("1 - Adicionar tarefas\n2 - Alterar status\n3 - Mostrar tarefas\n4 - Remover tarefa\n5 - "
                          "Refazer remoção\n6 - Sair\nEscolha uma opção: "))

        if opcao == 1:
            cria_nova_tarefa(lista_de_tarefas)
        elif opcao == 2:
            alterar_status(lista_de_tarefas)
        elif opcao == 3:
            mostra_tarefa(lista_de_tarefas)
        elif opcao == 4:
            remover_tarefa(lista_de_tarefas, tarefa_removida)
        elif opcao == 5:
            refaz_remocao(lista_de_tarefas, tarefa_removida)
        else:
            print('Ate mais!!')
            break


if __name__ == '__main__':
    menu()
