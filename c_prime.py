n1=int(input("Enter range:"))
n2=int(input("Enter n2:"))

def prime(t):
	return(factors(t)==[1,t])
def factors(t):
	flist=[]
	for i in range(1,t+1):
		if(t%i == 0):
			flist=flist+[i]
	return(flist)
t=n1
fflist=[]
while(t!=n2+1):
	p=prime(t)	
	if (p==True or t==1):
		fflist.append(t)
	t+=1
print("Prime numbers between",n1,"and n2",n2,"are : -->",fflist)
