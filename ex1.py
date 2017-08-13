#print("start test")

#for i in range(4):
#    print(i)
#    print("test")
    
#print("end test 1")

#for banana in range(20):
#    print(banana)
#    print(banana * 2)


#l=[int(x) for x in input().split()]
'''
def div(l):
	dl=[]
	for i in range(1,len(l)):
		if (l[i]%7 ==0 and l[i]%5 !=0):
			dl.append(l[i])
	return(dl)
n=[]
n=div(l)	
print(n)		
'''
l=[]
for i in range(2000,3201):
	if(i%7==0 and i%5!=0):
		l.append(str(i))
print(','.join(l))
				
	

