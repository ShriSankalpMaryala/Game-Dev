My_tuple = ("Sankalp" , 12 , "England" , "Chicken Biryani")
print(type(My_tuple))
He_tuple = "India" , 48 , 57 , 28
print(type(He_tuple))
print(He_tuple[2])
# My_tuple.append ("Saharsh")
# print(My_tuple)

#packing
#unpacking

name, age, country, food = My_tuple
print(name)

new_tuple = ("Sankalp", [1,2,3],(3,4,5),"Saharsh",100)
print(new_tuple[0][3])
#slicing
print(new_tuple[2:5])

new_tuple[1][2]=10
print(new_tuple)