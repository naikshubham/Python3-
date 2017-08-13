n=int(input("Enter a no"))
def fact(n):
	fact=1
	while(n>=1):
		fact=fact*n
		n-=1
	return fact
f=fact(n)
print("Factorial ", f)
