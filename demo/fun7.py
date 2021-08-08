def area_of_circle(r):
    pi = 3.14
    return float(pi * r * r)


def cube(num):
    
    return num * num * num


def area_of_triangle(l, h):
    return float(0.5 * l * h)


def fibo_series(num):
    f1 = 0
    f2 = 1
    if num == 1:
        print(f1)
    else:
        print(f1)
        print(f2)
        for i in range(2, num):
            temp = f1 + f2
            f1 = f2
            f2 = temp
            print(temp)


print('select operation:')
print('1.area of circle')
print('2.cube')
print('3.area of triangle')
print('4.fibo series')

choice = input('enter choice (1/2/3/4):')

if choice == '1':
    r = float(input('enter radius of circle:'))
    print('Area of circle is %0.6f' % area_of_circle(r))

elif choice == '2':
    num = int(input('enter number:'))
    print('cube is %d' % cube(num))

elif choice == '3':
    l = float(input('enter length:'))
    h = float(input('enter height:'))
    print('Area of triangle is %0.2f' % area_of_triangle(l, h))

elif choice == '4':
    num = int(input('enter number:'))
    print(fibo_series(num))

else:
    print('invalid output')
