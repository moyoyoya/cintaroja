# Punto de terminaci[on

#[]


def fibo(numero):
	if numero > 2:
		return fibo(numero-1) + fibo(numero-2)
	else:
		return numero-1

print(fibo(35))

def facrecur(numero):
	if numero != 0:
		return numero * facrecur(numero-1)
	else: 
		return 1

print(facrecur(10))

def itera(numero):
	cosa = 1
	for i in range (numero+1):
		if i != 0:
			cosa *=  i
	return cosa
print(itera(10))
