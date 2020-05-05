phrase = "Don't panic!"
plist = list(phrase)
plist2=[]
print (plist)
for i in range(4):
    plist.pop()
#plist.remove(')
plist.pop(0)
plist.pop(2)
print(plist)
for i in range(4):
   abc =plist.pop()
   plist2.append(abc)
   print (abc)
plist.insert(2," ")
xyz=plist2.pop()
plist2.insert(0,xyz)
plist2.pop()
plist.extend(plist2)
print("plist =  ", plist)
print("plist2 = ",plist2)
print ("this is the day that the Lord has made")