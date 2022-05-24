cubes = [x**3 for x in range (100) if  x%2 != 0 ]
print(cubes)
some_of_numbs = 0
some_of_numbs_list=[]

for i in range(len(cubes)):
  my_str = str(cubes[i])
  my_list = list(my_str)   
for i in range(len(my_list)):
  my_list[i] = int(my_list[i])    
for i in range(len(my_list)):
  some_of_numbs = some_of_numbs + my_list[i]
if some_of_numbs % 7 == 0:
        print(some_of_numbs)
some_of_numbs_list.append(some_of_numbs)
print('Числа, которые делятся на 7 - ', some_of_numbs_list)

cubes = [(x**3)+17 for x in range(100) if x%2 == 0]
print(cubes)
some_of_numbs = 0
some_of_numbs_list_with_numbers =[]

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

for i in range(len(my_list)):
        some_of_numbs = some_of_numbs + my_list[i]

if some_of_numbs % 7 == 0:
        print(some_of_numbs)
        some_of_numbs_list_with_numbers.append(some_of_numbs)

if some_of_numbs % 7 == 0:
        print(some_of_numbs)
        some_of_numbs_list_with_numbers.append(some_of_numbs)

print('Числа, которые делятся на 7 - ',some_of_numbs_list_with_numbers)