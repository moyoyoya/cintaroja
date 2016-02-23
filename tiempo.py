def hora(tiempo):
	tiempo = tiempo.lower()
	lista = []
	suma = tiempo[0]+tiempo[1]
	suma = int(suma)
	for i in tiempo:
		if i == 'p':
			suma+= 12
	return str(suma) + tiempo[2:8]




print(hora(input()))





