from mysql.connector import connect

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