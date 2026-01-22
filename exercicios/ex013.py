sal = float(input("Qual o seu salario? R$"))
novo = sal + (sal * 15 / 100)
print("Seu salario era {:.2f} e teve o aumento de 15% e você ira receber {:.2f} ".format(sal,novo))