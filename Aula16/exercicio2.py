hora = input ("Que horas são na sua localidade? ")
nome = input ("Informe seu nome: ")

hora = int (hora)

if hora >= 0 and hora <= 11:
    print (f"Bom dia {nome}")
elif hora >= 12 and hora <= 18:
    print (f"Boa tarde {nome}")
elif hora >= 18 and hora <= 23:
    print (f"Boa noite {nome}")
else:
    print("Você informou um horário incorreto.")

