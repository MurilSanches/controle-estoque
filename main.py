import product
import db 

print("Bem-vindo ao sistema de controle de estoque!\n")

prod = product.inputProduct()
product.showResults(prod)

connection = db.getMySQLConnection('localhost', 'newuser', 'Ti8T6hjxiv3c3N@murilo', 'projetointegrador1')
db.addProduct(connection, prod)