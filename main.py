import product
import db

print("\nBEM-VINDO AO SISTEMA DE CONTROLE DE ESTOQUE!\n")

connection = db.getMySQLConnection( \
    'bd080324144.c7mu8ocussz1.us-east-1.rds.amazonaws.com', \
    'BD080324144', \
    'w8oVXn99zeyoxPN8M9heafzEM', \
    'bd080324144')

def opcao3():
    print("Você escolheu a opção 3")

def opcao_invalida():
    print("Opção inválida")
    print()
    
def addProduct():
    prod = product.inputProduct()
    product.showResults(prod)
    db.addProduct(connection, prod)

def listAllProducts():
    products = db.retrieveAllProducts(connection)
    product.listAllProducts(products)
        
def listProduct():
    code_id = product.getProductCode()
    print()
    prod = db.retrieveProduct(connection, code_id)
    if prod != None:
        product.showResults(prod)
        
def deleteProduct():
    code_id = product.getProductCode("Digite o código do produto que deseja excluir: ")
    print()
    prod = db.retrieveProduct(connection, code_id)
    if prod != None:
        db.deleteProduct(connection, code_id)

def sair():
    print("OBRIGADO POR USAR ESTE PROGRAMA!\n")

def showMenu():
    print(51*"-", "\n")
    print("MENU")
    print()
    print("1 - Adicionar um novo produto")
    print("2 - Listar todos os produtos")
    print("3 - Classificação de um produto")
    print("4 - Alterar um produto")
    print("5 - Excluir um produto")
    print("9 - Sair")
    print(51*"-", "\n")
    while True:
        try:
            opcao = int(input("Digite o opção que deseja: "))
            break
        except ValueError:
            opcao_invalida()            
    print()
    menu = {
        1: addProduct,
        2: listAllProducts,
        3: listProduct,
        4: opcao3,
        5: deleteProduct,
        9: sair
    }
    funcao = menu.get(opcao, opcao_invalida)
    funcao()
    return opcao

opcao = None
while opcao != 9:
    opcao = showMenu()

connection.close()