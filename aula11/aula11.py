"""
Operadores Relacionais - Aula 11

== - Igualdade
> - Maior que
>= Maior ou Igual que
< - Menor que 
<= - Menor ou igual que
!= - Diferente 
"""
nome = input ("Qual o seu nome? ")
idade = int (input ("Qual a sua idade? "))
jovem = 20
velho = 30

if (idade >= jovem and idade <= velho):
    print("Você consegue um novo emprestimo.")
else:
    print ("Você não está autorizado a retirar um novo emprestimo")
