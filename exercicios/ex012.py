preço = float(input("Qual é o preço do produto: R$ "))
novo = preço - (preço * 5 / 100)
print("o protudo é {:.2f} e com 5% de desconto ele vai custar {:.2f} ".format(preço,novo))