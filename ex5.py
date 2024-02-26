name = input("Digite seu nome: ")
price = float(input("Digite o preço do produto: "))
quantity = int(input("Digite a quantidade de produtos: "))

def calcTotalPrice(price, quantity):
    if quantity > 10:
        return price * quantity * 0.10
    else:
        return price * quantity
    
print("O total a pagar é", calcTotalPrice(price, quantity))