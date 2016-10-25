
import random
import math
def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    a = [x]
    b = [y]
    for i in range(n):
        if random.randrange(2) == 0:
            x = x + random.choice([1,-1])
        elif random.randrange(2) == 1:
            y = y + random.choice([1,-1])
    a.append(x)
    b.append(y)
    return math.sqrt((a[0] - a[1])**2 + (b[0] - b[1])**2)

x = input('Enter in your starting x coordinate.')
y = input('Enter in your starting y coordinate.')
n = input('How many times would you like to move?')

distance = drunkard_walk(int(x), int(y), int(n))
print("The drunkard started from", x, y) 
print(" After", n, "intersections, he's",
      distance, "blocks from where he started.")

