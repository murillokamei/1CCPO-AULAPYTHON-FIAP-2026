cp = 0

while cp <= 3:
    print(f"Produto {cp}")
    cp += 1

#while decrescente de 4 até 1 (incluir)
i = 4
print()
while i > 0:
    print(i)
    i -= 1

# repetição com entrada de usuário
jogar = "SIM"

#".lower()" é pra quando for tudo minúsculo
while jogar.lower() == "sim":
    print()
    print("Repete ou inicia o jogo")
    jogar = input("Deseja ou jogar novamente? ")

#continue : é um "filtro"
i = 0
print()
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"Produto {i}")
