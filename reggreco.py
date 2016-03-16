n = int(input("Введите кол-во опытов"))
x = []
y = []
#for i in range(n):
	#x.append(0)
	#y.append(0)
print("Введите наблюдения x")
for i in range(n):
      print('Наблюдение №', str(i + 1))
      x.append(int(input()))
print("Введите наблюдения y")
for i in range(n):
      print('Наблюдение №', str(i + 1))
      y.append(int(input()))
s1=0
for i in range(n):
      s1 = s1+x[i]*y[i]
s2 = sum(x)
s3 = sum(y)
s4 = 0
for i in range(n):
      s4=s4+x[i]**2
p1=(n*s1-s2*s3)
p2=(n*s4-s2**2)
p=p1/p2
d1=(s4*s3-s2*s1)
d2=(n*s4-s2**2)
d=d1/d2
z=p*(int(input("Введите желаемое наблюдение ")))+d
print(z)
