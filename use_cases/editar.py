from use_cases.buscar_por_cod import buscarPorCodigo
from use_cases.adicionar import adicionarProduto
from repositorio import banco
def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
        print('Dados alterados com sucesso!')

    else:
        print('Produto não encontrado!')


if __name__ == '__main__':
    adicionarProduto('mouse', 'Perifericos', 50.00)
    adicionarProduto('monitor philco', 'Monitores', 750.00)
    print(banco)
    editarProduto(1, 'Mouse logitech', 'Perifericos', 60.00)
    print(banco)