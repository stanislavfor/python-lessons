import copy

# my_list = [1234, 3456, 456, [345, 567, 345, 23, 
#{'один':1, 'два':2, 'три':3}]]
# num = 34
# num_1 = num

# my_list_1 = my_list
# my_list_1[3] = 0

# print(my_list)
# print(my_list_1)

# my_list_2 = my_list.copy()

# my_list_2[2] = '***'
# my_list_2[-1][2] = 999
# my_list_2[-1][-1]['два'] = 222

# print(my_list)
# print(my_list_1)
# print(my_list_2)

# my_list_3 = copy.deepcopy(my_list)



my_list = [1234,3456,5678,456, [345,567,345,23, 
{'один': 1, 'два': 2, 'три': 3}]]

num = 34
num_1 = num

my_list_1 = my_list
my_list_1[3] = 0

print(my_list)
print(my_list_1)

my_list_2 = my_list.copy()

my_list_2[2] = '***'
# my_list_2[-1][2] = 999
my_list_2[-1][2] = 999
my_list_2[-1][4]['два'] = 222

print()
print(my_list)
print(my_list_2)

my_list_3 = copy.deepcopy(my_list)
my_tuple = (123,2345,456,2345,567, [1111,2222,333])
my_tuple[-1][1]=0


