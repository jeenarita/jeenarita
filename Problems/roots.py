import math

def find_roots(a, b, c):
    part2 =math.sqrt((b*b) - (4 * a * c))
    two_a = 2 * a
    
    root_1 = ((-b) + part2)/two_a
    root_2 = ((-b) - part2)/two_a
  
    return (root_1, root_2)

print(find_roots(2, 10, 8))