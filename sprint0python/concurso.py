
respuesta = None
puntos = 0
print('Cuántas patas tiene un gato?')
print('a.1')
print('b.3')
print('c.4')
	respuesta = input('Selecciona tu respuesta (a,b,c)')
	while(respuesta != 'a') & (respuesta != 'b') & (respuesta != 'c'):
		respuesta = input('Respuesta no válida. Prueba con :(a,b,c)')
	if (respuesta == 'a') | (respuesta == 'b'):
		print('Respuesta incorrecta. Menos 5 puntos :/')
		puntos -= 5
	else:
		print('Respuesta correcta. Has sumado 10 puntos :3')
		puntos += 10
	print('Cuánto es 2 + 2?')
	print('a.3')
	print('b.4')
	print('c.13')
	respuesta = input('Selecciona tu respuesta (a,b,c)')
	while(respuesta != 'a') & (respuesta != 'b') & (respuesta != 'c'):
		respuesta = input('Respuesta no válida. Prueba con :(a,b,c)')
	if (respuesta == 'a') | (respuesta == 'c'):
		print('Respuesta incorrecta. Menos 5 puntos :/')
		puntos -= 5
	else:
		print('Respuesta correcta. Has sumado 10 puntos :3')
		puntos += 10
	print('Cuántas manzanas le quedan a Manolito si al principio tenía 10 y luego se comió 2?')
	print('a.8')
	print('b.7')
	print('c.9')
	respuesta = input('Selecciona tu respuesta (a,b,c)')
	while(respuesta != 'a') & (respuesta != 'b') & (respuesta != 'c'):
		respuesta = input('Respuesta no válida. Prueba con :(a,b,c)')
	if (respuesta == 'b') | (respuesta == 'c'):
		print('Respuesta incorrecta. Menos 5 puntos :/')
		puntos -= 5
	else:
		print('Respuesta correcta. Has sumado 10 puntos :3')
		puntos += 10
	print('Puntuación final = '+str(puntos))
	
