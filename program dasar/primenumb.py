#program untuk cek bilangan prima
num = int(input("Masukkan bilangan= "))


flag = False
if num == 1:
  print(num, "adalah bukan bilangan prima")
elif num > 1:
  for i in range(2,num):
    if num % i == 0:
      flag = True
    break
if flag:
  print(num, "adalah bukan bilangan prima")
else:
  print(num, "adalah bilangan prima")