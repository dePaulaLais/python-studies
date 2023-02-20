#Entendendo variáveis
nome = input ("Nome: ")
ano_nascimento = input ("Ano de nascimento: ")
cidade = input ("Cidade: ")
estado_civil = input ("Estado civil: ")
idade = 2023 - int(ano_nascimento)

#print("Seu nome é " + nome + ", você tem "+ str(idade) + " anos e mora em "+ cidade +".")

#String Formatada
frase = f'   Seu nome é {nome}, você mora em {cidade} e tem {idade} anos.'
print (frase)

#Métodos para string

#substituir uma palavra por outra
print (frase.replace('nome', 'name'))
#remover os espaços no inicio
print (frase.strip())
#imprimir tudo em maiusculo
print (frase.upper())