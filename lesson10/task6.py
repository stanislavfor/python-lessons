my_tuple = (123, 2345, 456, 2345, 567, [1111, 2222, 333])
a, b, *c = my_tuple
print(a)
print(b)
print(c)
print(' --- ')

my_tuple = ([1, 2, 3, 4, 5], [111, 222, 333, 444, 555], [123, 2345, 456, 2345, 567])
a, b, c = my_tuple
for q, w, e, r, t in my_tuple:
  print(q)
  print(w)
  print(e)
  print(r)
  print(t)
print(' --- ')

my_tuple = my_tuple = ([1,2,3,4,5],[111,222,333,444,555],[234,234,456,568,3456])
a, b, *c = my_tuple
for q, *w, e in my_tuple:
    print(q)
    print(w)
    print(e)  
print(' --- ')    
