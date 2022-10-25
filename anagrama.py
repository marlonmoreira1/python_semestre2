def repetidas(palavra):

	repetida = {}

	for letra in palavra:
		repetida.setdefault(letra,0)
		repetida[letra] += 1

	return repetida

def fatorial(n):
	
	if n == 0:
		return 1
	else:
		return n * fatorial(n - 1)

def total_p(lista):
	total = 1

	for p in lista:
		total *= fatorial(p)

	return total

def anagrama(n, palavra):

	p_dicio = repetidas(palavra)
	p = list(p_dicio.values())
	total_do_p = total_p(p)  

	return fatorial(n)/total_do_p

palavra = input('Digite a palavra com letras repetidas: ')

n = len(palavra)

mat_anam = anagrama(n,palavra)
print(mat_anam)








