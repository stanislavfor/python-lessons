def tri(h, a):
  return 0.5 * h * a

def rect(a, b):
  return a * b

def circle(r):
  return 3.14 * r ** 2

def main():

  print("Start of Modul_1")

  print("Start of calculating the area (a complex shape = )")

  area = rect(20, 30) + tri(5, 10) - circle(5)

  print(area)

  print("End of Modul_1")

# main()


if __name__ == '__main__':
  main()

# или
# if __name__ == '__main__':  

#   print("Start of Modul_1")

#   print("Start of calculating the area (a complex shape = )")

#   area = rect(20, 30) + tri(5, 10) - circle(5)

#   print(area)

#   print("End of Modul_1")