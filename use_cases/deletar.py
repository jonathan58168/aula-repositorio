from use_cases.buscar_por_cod import buscarPorCodigo
from use_cases.adicionar import adicionarProduto
from repositorio import banco
from use_cases.editar import editarProduto

def deletarProduto(codigo: int) -> None:
    produto = buscarPorCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('Produto deletado com sucesso!')
    else:
        print('Produto não encontrado!')

if __name__ == '__main__':
    adicionarProduto('mouse', 'Perifericos', 50.00)
    adicionarProduto('monitor philco', 'Monitores', 750.00)
    print(banco)
    editarProduto(1, 'Mouse logitech', 'Perifericos', 60.00)
    print(banco)
    deletarProduto(1)
    print(banco)