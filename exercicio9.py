a = int(input("Choose one of the sides of a triangle: "))
b = int(input("Choose another side of a triangle "))
c = int(input("Choose the last side of a triangle "))

if (a + b <= c) and (a + c <= b) and (b + c <= a):
    print("This is a triangle")
    if a == b and a == c and b == c:
        print('This is a equilateral triangle')
    elif a == b or b == c or a == c:
        print('This is a isosceles triangle')
    else:
        print('This is a scalene triangle')
else:
    print('This is not a triangle')
