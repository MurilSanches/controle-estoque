from mysql.connector import connect
import product

def getMySQLConnection (server, user, password, bd): 
    if getMySQLConnection.conexao==None:
        getMySQLConnection.conexao = connect(host=server, user=user, passwd=password, database=bd) 
    return getMySQLConnection.conexao
getMySQLConnection.conexao=None

def addProduct(connection, prod):
    cursor=connection.cursor()
    comando = "insert into Produto (codigo, nome, descricao, custo, custo_fixo, comissao, taxas, lucro) " + \
              "values (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (prod["code_id"], prod["name"], prod["description"], prod["cost"], prod["fixed_adm_cost"],
               prod["commission"], prod["taxes"], prod["profit"])
    try:
        cursor.execute(comando, valores)
        connection.commit()
        print("Produto adicionado com sucesso!")
    except Exception as e:
        if "Duplicate entry" in str(e):
            print("Chave primária duplicada")
        else:
            print("Erro de integridade:", e)

def retrieveProduct(connection, code_id):
    cursor=connection.cursor()
    comando = "select * from Produto where codigo = " + str(code_id)
    valores = (code_id)
    try:
        cursor.execute(comando)
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return product.buildProduct(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7])
        else:
            print("O código", code_id, "não representa o código de um produto cadastrado.")
    except Exception as e:
        print("Erro:", e)