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