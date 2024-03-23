product = {
    "price": 36,
    "fixedCost": 0.15,
    "comission": 0.05,
    "taxes": 0.12,
    "profit": 0.20
}

def getSalePrice(product):
    return product["price"] / (1 - (product["fixedCost"] + product["comission"] + product["taxes"] + product["profit"]))

print('preço de venda', getSalePrice(product))