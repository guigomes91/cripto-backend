amigos = ['Marcos', 'Pedro', 'Adriana', 'Karina', 'Julia']
numeros = [3, 5, 12, 2, 15, 6]

amigos.sort()
numeros.sort()
print(amigos)
print(numeros)

acordei_antes_9 = False
fome = True

if acordei_antes_9 and fome:
    print('Hora de fazer o café da manhã')
elif acordei_antes_9 and not(fome):
    print('Hora de fazer uma corrida')
else:
    print('Hora de fazer o almoço')