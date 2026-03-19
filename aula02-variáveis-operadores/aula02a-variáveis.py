print("ola mundo")

print(7 + 4)
print("7 + 4")
print("7" + "4") #CONCATENAÇÃO DE STRINGS

#Comentários de 1 linha
'''
     Comentários de 
     múltiplas linhas
     ambos os comentários são ignorados pelo programa
'''

#VARIÁVEIS
nome = "Murillo"
print(nome)
print("nome")
idade = 18 #inteiro
peso = 92.2 #float

print(nome, idade, peso)
print(f"ola, {nome}!!")

#IMPUTS - SIMULAÇÃO DE FORMS NO CMD
nome = input("Digite o seu nome: ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o seu peso: "))

print(nome, idade, peso)
print(idade+1)

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade}")
