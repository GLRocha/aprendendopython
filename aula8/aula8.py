nome ='gabriel'
idade = 24
altura = 1.76
peso = 96
ano_atual = 2020

ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print('O IMC de {} é {:.2f}'. format(nome, imc))
print('{} nasceu em {}'. format(nome, ano_nasc))

