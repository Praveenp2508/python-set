#set---------- {} / set()

set={2,3,6,5,4,7,2,7,5,5,1}
print(set)

thisset={'apple','banana','cherry'}
thisset.discard(5)
print(thisset)

a,b= {2,45,7,9,23},{43,6,7,9,2}
print(a.difference(b))
print(a)
b.difference_update(a)
print(b)

s={20,30,40,50,60,70,30,40,10}
print(type(s))

print(s)

day={'mon','tue','wed','thu','fri','sat','sun'}
print(day)
