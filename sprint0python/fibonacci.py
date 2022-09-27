
def funcion_fibonacci(num):
	if num==0:
		return 0
	elif num==1:
		return 1
	else:
		return(funcion_fibonacci(int(num)-1) + funcion_fibonacci(int(num)-2))

			
