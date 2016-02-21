# piedra, papel  y python
from random import randint
opciones=['piedra','papel','python']
pc=(opciones[randint(0,2)])
usuario = ""
while usuario != 'q':
	usuario= input ('piedra, papel o python (para detener el juego presona Q)').lower()
	if pc == usuario:
		print('Empate')
	else:
		if (usuario=='piedra' and pc=='papel'):
			print('Pierdes')
		elif (usuario=='piedra' and pc=='python'):
			print('Tu ganas' ) 
		elif (usuario=='papel' and pc=='python'):
			print('Pierdes')
		elif (usuario=='papel' and pc=='piedra'):
			print('Tu ganas' ) 
		elif (usuario=='python' and pc=='piedra'):
			print('Tu pierdes' ) 
		elif (usuario=='python' and pc=='papel'):
			print('Tu ganas' ) 
		elif (usuario='q'):
			print('adios')
		else:
			print('opcion no valida')


	  