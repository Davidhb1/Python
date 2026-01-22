real = float(input("Quanto você tem na sua carteira? R$: "))
dolar = real / 5.77
print("Você tem R${:.2f} em Real e convertido terá US{:.2f} ".format(real,dolar))