def Area_of_triangle():
    a = float(input('enter first side'))
    b = float(input('enter second side'))
    c = float(input('enter third side'))

    s = (a + b + c) / 2
    print(s)


    area = (s * (s - a) * (s - b) * (s - c)) * 0.5
    print('Area of triangle is %0.2f' % area)


print(Area_of_triangle())

