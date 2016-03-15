print("Введите необходимые значения для функции: ax^2+bx+c")
a1=int(input("Введите a "));
b1=int(input("Введите b "));
c1=int(input("Введите c "));
def f(x):
      return a1*x**2+b1*x+c1;
a=int(input("Введите первую точку "));
b=int(input("Введите вторую точку "));
e=int(input("Введите Эпсилон "));
ss=0
n=(b-a)/e
#dx=(b-a)/n
x1=a
for i in range (int(n)):
      s=f(x1)*e #dx
      ss=ss+s
      x1=x1+e #dx
print (ss)

      
