from use_cases.gerar_produto import criarProduto
from repositorio import banco
from use_cases.listar import listarProdutos
# codigo - nome - categoria - preço
def adicionarProduto(nome, categoria, preco):
    produto = criarProduto(nome, categoria, preco)
    banco.append(produto)
    print('Produto adicionado com sucesso!')

if __name__ == '__main__':
    adicionarProduto('mouse', 'Perifericos', 50.00)
    adicionarProduto('monitor philco', 'Monitores', 750.00)
    print(banco)
    listarProdutos()