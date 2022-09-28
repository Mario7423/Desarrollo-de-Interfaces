import time
from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2
opcion = input('Menú\na. Fibonacci 1\nb. Fibonacci 2\n\tSelecciona una opción(a,b)')
while(opcion != 'a') & (opcion != 'b'):
	opcion = input('Opción no válida, prueba con (a,b)')
if opcion == 'a':
	num = input('Qué número quieres utilizar en la sucesión Fibonacci?')
	start_time = time.time()
	print(funcion_fibonacci(num))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
else:
	num = input('Qué número quieres utilizar en la sucesión Fibonacci 2?')
	start_time = time.time()
	print(funcion_fibonacci2(num))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')

