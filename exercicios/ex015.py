d = int(input("Quantos dias alugado? "))
k = float(input("Quantos Km usado? "))
p = (d * 60) + (k * 0.15)
print("O total a ser pago é R${:.2f} ".format(p))