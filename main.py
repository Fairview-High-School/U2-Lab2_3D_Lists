listA = ["","","","" ]
listB = ["Gesell","Peoples","Chilton","Strode" ]
listC = [["Tim","Gesell"],["Scott", "Peoples"],["Adam","Chilton"],["Paul","Strode"] ]
listD = ["Gesell",["Scott", "Peoples"],"Chilton",["Paul","Strode"] ]

print (listA)
print (listB)
print (listC)
print (listD)

print (len(listA))
print (len(listB))
print (len(listC))
print (len(listD))

print(listA[0]) #item 1 of listA
print(listB[2]) #item 3 of listB
print(listC[1]) #item 2 of listC
print(listD[-1]) #item last of listD

print(listB[0][1]) #item 2 of item 1 of list B
print(listC[0][1]) #item 2 of item 1 of list C
print(listD[0][1]) #item 2 of item 1 of list D (this doesn't work in Snap!)
print(listD[1][0]) #item 2 of item 1 of list D

print(listB[1:]) #all but the first element (skipping element 0) of list B
print(listC[1][1:]) #all but the first element (skipping element 0) of item 2 of list C
