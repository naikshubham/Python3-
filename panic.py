phrase="Don't panic"
plist=list(phrase)
print(phrase)
print(plist)
print('------------------------------')
stri=[]
for i in phrase:
	if (i=='o' or i=='n' or i=='t' or i=='a' or i=='p') and i not in stri:
		stri.append(i)
print(stri)		
var=stri.pop()
stri.insert(3,var)
stri=''.join(stri)
print(stri)
print('-------------------------------')
string=''.join(plist)
print(plist)
print(string)
