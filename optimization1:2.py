m=int(input("Для нахождения минимума, введите: 1; для максимума: -1 "));
print("Введите необходимые значения для функции: ax^2+bx+c")
a=int(input("Введите a "));
b=int(input("Введите b "));
c=int(input("Введите c "));
f = lambda x: a*x**2+b*x+c;
x1 = float(input("Введите первую точку  "));
x2 = int(input("Введите вторую точку  "));
e = int(input("Введите Эпсилон  "));
while True:
      x=(x1+x2)/2
      n=x-e
      m=x+e
      if f(n)*m<f(m)*m:
            x2=x
      else:
          x1=x
      if (x2-x1) < e:
            break
x=(x2+x1)/2
print (x, f(x))
