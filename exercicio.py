#Boletim
nota1 = float(input("Primeira nota do Aluno"))
nota2 = float(input("Segunda nota do Aluno"))

soma = (nota1 + nota2)/2
media = soma
if media >= 5:
    print("A sua média foi ", media, " Você foi Aprovado!!!")
else:
    print("A sua média foi ", media, " Você foi Reprovado - Precisa Estudar") 