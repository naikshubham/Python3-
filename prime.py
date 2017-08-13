n=int(input("Enter n"))
def isprime(n):
	return(factors(n)==[1,n])
def factors(n):
	flist=[]
	for i in range(1,n+1):
		if (n%i == 0):
			flist=flist+[i]
#			print(flist)
	return(flist)


prime=isprime(n)
if (prime == True):
	print("n is prime")
else:
	print("n is not prime")
