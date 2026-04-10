#FUNCAO SEM RETORNO E SEM PARAMETRO
def print_lyrics() :
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()
print()
print_lyrics()
print_lyrics()#exibir a funcao 2 vezes
print()

#FUNCAO SEM RETORNO E COM PARAMETRO
def boas_vindas(nome):
    print(f"Olá, {nome}!!! Seja bem-vindo!!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)
print()

#FUNCAO COM RETORNO E COM PARAMETRO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(17,22)
print(resultado_soma)
#print(soma(13, 30)) <- pode ser feito assim tbm

