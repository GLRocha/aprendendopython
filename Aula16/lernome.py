nome = input("Digite seu nome para avançar: ")



nome_peq = len (nome)
nome_curto = len (nome)
nome_grande = len (nome)

if nome_peq == 4:
    print("Seu nome está muito curto!")
elif nome_curto == 5:
    print("Seu nome está normal.")
elif nome_grande == 6:
    print("Seu nome esta grande demais!")
else:
    print("Sáo válidos apenas nomes com 4, 5 ou 6 caracteres!")
    