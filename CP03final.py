import numpy as np

salas = ["Sala 1","Sala 2","Sala 3","Sala 4"]
temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]
sala_risco = -1
critico = 0
for i,v in enumerate (temperaturas):
    contador = 0
    registro = 0
    for temperatura in v:
        contador += temperatura
        if temperatura >= 33:
            registro += 1
    media = contador / len(v)
    if registro > critico:
        critico = i +1
    print(f"Sala {i+1}")
    print(f"Média {media}")
    print(f'Registro {registro}')
    print()

print(f"Sala com maior risco {critico}")

