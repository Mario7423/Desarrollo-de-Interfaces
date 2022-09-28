def funcion_fibonacci2(num):
	import math
	raiz = math.sqrt(5)
	a=(1+raiz)/2
	b=(1-raiz)/2
	if num==0:
		return 0
	elif num==1:
		return 1
	else:
		return int((((a ** int(num)) - (b ** int(num))) / raiz))
