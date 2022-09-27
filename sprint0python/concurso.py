class Concurso:
	respuesta = None
	print('Cuántas patas tiene un gato?')
	print('a.1')
	print('b.3')
	print('c.4')
	respuesta = input('Selecciona tu respuesta (a,b,c)')
	while(respuesta != 'a') & (respuesta != 'b') & (respuesta != 'c'):
		respuesta = input('Respuesta no válida. Prueba con :(a,b,c)')
	if (respuesta == 'a') | (respuesta == 'b'):
		print('Respuesta incorrecta')
	else:
		print('Respuesta correcta')
	
	
