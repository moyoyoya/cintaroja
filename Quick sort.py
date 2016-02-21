def recursi(lista):
	lista1 = []
	lista2 = []
	if len(lista)>1:
	    pivote = lista[0]
	    lista.remove(pivote)
	    for numero in lista:
	        if numero >= pivote:
	            lista2.append(numero)
	        else:
	            lista1.append(numero)
	    lista1 = recursi(lista1)
	    lista2 = recursi(lista2)
	    lista1.append(pivote)
	    lista = lista1+lista2
	return lista

lista = [2,3,1,4,1,7,9,5,6,4,5,7]
print(lista)
print(recursi(lista))

	