import product
import db 

print("Bem-vindo ao sistema de controle de estoque!\n")

prod = product.inputProduct()
product.showResults(prod)

connection = db.getMySQLConnection('localhost', 'newuser', 'Ti8T6hjxiv3c3N@murilo', 'projetointegrador1')
db.addProduct(connection, prod)

while True:
    try:
        code_id = int(input("Digite o código do produto que deseja obter dados: "))
        if (code_id < 1):
            print("Código inválido. Por favor, tente novamente com um número inteiro positivo!")
        else:
            break
    except ValueError:
        print("Código inválido. Por favor, tente novamente com um número inteiro positivo!")

prod = db.retrieveProduct(connection, code_id)
if prod != None:
    product.showResults(prod)

print("OBRIGADO POR USAR ESTE PROGRAMA!\n")

connection.close()