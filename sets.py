set_a = {1,2,3,4}
set_b = {3,4,5,6}

#union |
print(set_a.union(set_b))

#intersection &
print(set_a.intersection(set_b))

#difference - 
print(set_a.difference(set_b))

#symmetric difference ^
print(set_a.symmetric_difference(set_b))

#add
set_a.add(10)
print(set_a)
#remove
set_a.discard(1)
print(set_a)
