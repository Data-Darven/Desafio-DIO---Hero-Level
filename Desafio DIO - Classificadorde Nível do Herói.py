def classificar_heroi(nome, xp):
    if xp < 1000:
        nivel = "Ferro"
    elif 1000 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 6001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    
    print(f"O Herói de nome {nome} está no nível de {nivel}.")

while True:
    nome = input("Digite o nome do herói ou 'sair' para encerrar: ")
    if nome.lower() == "sair":
        break
    xp = int(input("Digite a quantidade de experiência do herói: "))
    classificar_heroi(nome, xp)
