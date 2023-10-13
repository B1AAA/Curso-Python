#Strings são iteraveis(acessar item por item de uma lista)

# nome = 'Beatriz'
# print(nome [2])
# print(nome [-5])
# print('a' in nome)
# print('Bea' in nome)            
# print('z' in nome)
# print('zero' in nome)
# print('Bea'  not in nome)
# print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')
