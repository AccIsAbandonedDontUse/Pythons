import itertools
NumList = itertools.product('anything here', repeat=10) #Repeat is length of results, the first part is any letters/symbols etc you want in it
add = 0
for i in NumList: 
    print (''.join(i))
    add = add +1
print (add, "Combinations")