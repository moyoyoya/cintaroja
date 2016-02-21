def bajada(lista):
	if len(lista) > 1:
		izq = lista[(round(len(lista)/2)):]
		der = lista[:(round(len(lista)/2))]
		izq = bajada(izq)
		der = bajada(der)
		return subida(izq, der)
	return lista

def subida(izq, der):
	con = 0
	lista = []
	while izq and der:
		if izq[con]<= der[con]:
			lista.append(izq[con])
			izq.remove(izq[con])
		else:
			lista.append(der[con])
			der.remove(der[con])
	while izq:
		lista.append(izq[con])
		izq.remove(izq[con])
	while der:
		lista.append(der[con])
		der.remove(der[con])
	return lista


lista = [1,2,1,2,4,6,5,6,78,7,8,9,7,9,3,4,6,7,8,0]
print(lista)
print(bajada(lista))


