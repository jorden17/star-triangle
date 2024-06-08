def lower_triangle(height):
    for i in range(1, height + 1):
        print('* ' * i)

def upper_triangle(height):
    for i in range(height, 0, -1):
        print('* ' * i)

def pyramid_triangle(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '* ' * i)


print("Lower Triangle:")
lower_triangle(5)

print("\nUpper Triangle:")
upper_triangle(5)

print("\nPyramid Triangle:")
pyramid_triangle(5)
