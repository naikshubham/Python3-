word = "Don't panic"
wlist=list(word)
print(wlist)
print("----------------------")
new_wlist1=wlist[1:3].copy()
new_wlist2=wlist[4:8].copy()
new_wlist=[]
new_wlist=new_wlist1+new_wlist2
print(new_wlist)
new_wlist.insert(2,new_wlist.pop(3))
new_wlist.insert(4,new_wlist.pop())
print(new_wlist)
new_word=''.join(new_wlist)
print(new_word)


