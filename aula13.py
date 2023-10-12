nome = 'Beatriz'
altura = 1.61
peso = 90
imc = peso / (altura*altura) 


linha_1 = f'{nome} tem {altura:.2f} de altura'

linha_2 = f'pesa {peso} quilos e seu imc é'

linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


print(nome,'tem',altura,'de altura, pesa',peso,'kilos e seu IMC é de:',imc)
print(f'{nome} tem {altura} de  altura, pesa {peso} quilos e seu imc é de {imc:.2f}')