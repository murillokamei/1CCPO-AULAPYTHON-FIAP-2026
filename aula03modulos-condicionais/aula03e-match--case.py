#0 --> sair do programa
#1 --> entrar no programa
# ----> erro!!
escolha_usuario = 0

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _: #o _ é pra qualquer coisa que não seja os termos acima (nesse caso 0 e 1)
        print("Erro!!")