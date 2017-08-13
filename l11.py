def divisors():
	l=[]
	for i in range(2000,3201):
		if i%7==0 and i%5==0:
			l.append(i)
	print(','.join(l))
divisors()
