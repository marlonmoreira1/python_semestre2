def transforme(numero):
	
	resultado = 0
	binario = []

	while resultado != 1:
		resultado = numero//2
		
		if numero/2==0:
			binario.append(str(numero/2))
		else:
			binario.append(str(numero%2))
			
		numero = resultado

	binario.append(str(numero))

	return binario


def junta(lista):

	new_list = lista[::-1]
	junta = ''

	binario = junta.join(new_list)

	return binario
	


numero = int(input('Digite um numero: '))

lista = transforme(numero)

binario = junta(lista)

print(binario)



