from use_cases.adicionar import adicionarProduto
from use_cases.listar import listarProdutos
from use_cases.editar import editarProduto
from use_cases.deletar import deletarProduto

def menu():
    while True:
        print('------ Menu de produtos ------')
        print('1 - Cadastrar produto')
        print('2 - Editar produto')
        print('3 - Deletar produto')
        print('4 - Listar todos os produtos')
        print('5 - Sair')
        opcao = input('Digite o número da opção desejada: ')
        if opcao == '1':
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite o nome da categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            adicionarProduto(nome, categoria, preco)
        elif opcao == '2':
            listarProdutos()
            codigo = int(input('Digite o código do produto que deseja editar: '))
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            editarProduto(codigo,nome, categoria, preco)
        elif opcao == '3':
            listarProdutos()
            codigo = int(input('Digite o código do produto que deseja deletar: '))
            deletarProduto(codigo)
        elif opcao == '4':
            listarProdutos()
        elif opcao == '5':
            print('Você saiu do sistema, até logo!')
            break
        else:
            print('Opção inválida!')

menu()


