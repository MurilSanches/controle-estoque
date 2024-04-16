def inputProduct():
    print("Por favor, insira os dados do produto conforme orientações:\n")
    
    while True:
        try:
            code_id = int(input("Código do produto: "))
            if (code_id < 1):       #Checar também se code_id já existe
                print("Código inválido. Por favor, tente novamente com um número inteiro positivo!")
            else:
                break
        except ValueError:
            print("Código inválido. Por favor, tente novamente com um número inteiro positivo!")
            
    name = input("Nome do produto: ")
    
    description = input("Descrição do produto: ")
    
    while True:
        try:
            cost = float(input("Custo do produto: "))
            if (cost <= 0):
                print("Custo inválido. Por favor, tente novamente com um número positivo!")
            else:
                break
        except ValueError:
            print("Custo inválido. Por favor, tente novamente com um número positivo!")
    
    costSum = 0
    while True:
        try:
            fixedAdmCost = float(input("Custo fixo/administrativo do produto: "))
            if (fixedAdmCost < 0 or fixedAdmCost >= 1):
                print("Custo fixo/administrativo inválido. Por favor, tente novamente com um número entre 0.00 e 1.00!")
            else:
                costSum += fixedAdmCost
                break
        except ValueError:
            print("Código fixo/administrativo inválido. Por favor, tente novamente com um número entre 0.00 e 1.00!")
    
    while True:
        try:
            commission = float(input("Comissão de vendas: "))
            if (commission < 0 or commission >= 1):
                print("Comissão de vendas inválida. Por favor, tente novamente com um número entre 0.00 e 1.00!")
            elif (costSum + commission >= 1):
                print("Comissão muito alta e pode gerar resultados incorretos. Por favor, insira um valor menor!")
            else:
                costSum += commission
                break
        except ValueError:
            print("Comissão de vendas inválida. Por favor, tente novamente com um número entre 0.00 e 1.00!")

    while True:
        try:
            taxes = float(input("Impostos: "))
            if (taxes < 0 or taxes >= 1):
                print("Impostos inválidos. Por favor, tente novamente com um número entre 0.00 e 1.00!")
            elif (costSum + taxes >= 1):
                print("Impostos muito altos e podem gerar resultados incorretos. Por favor, insira um valor menor!")
            else:
                costSum += taxes
                break
        except ValueError:
            print("Impostos inválidos. Por favor, tente novamente com um número entre 0.00 e 1.00!")

    while True:
        try:
            profit = float(input("Rentabilidade: "))
            if (profit < 0 or profit >= 1):
                print("Rentabilidade inválida. Por favor, tente novamente com um número entre 0.00 e 1.00!")
            elif (costSum + profit >= 1):
                print("Rentabilidade muito alta e pode gerar resultados incorretos. Por favor, insira um valor menor!")
            else:
                break
        except ValueError:
            print("Rentabilidade inválida. Por favor, tente novamente com um número entre 0.00 e 1.00!")
            
    return buildProduct(code_id, name, description, cost, fixedAdmCost, commission, taxes, profit)



def buildProduct(code_id, name, description, cost, fixedAdmCost, commission, taxes, profit):
    product = {
        "code_id": code_id,
        "name": name,
        "description": description,
        "cost": cost,
        "fixed_adm_cost": fixedAdmCost,
        "commission": commission,
        "taxes": taxes,
        "profit": profit,
        #"sale_price": None
    }
    getSalePrice(product)
    return product


def getSalePrice(product):
    product["sale_price"] = product["cost"] / \
            (1 - (product["fixed_adm_cost"] + product["commission"] + \
            product["taxes"] + product["profit"]))