import math 
class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """
my_point = Point()
my_point.x = 1
my_point.y = 1

my_point1 = Point()
my_point1.x = 3
my_point1.y = 3

def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))

# print_point(my_point)

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2) 

# print(distance_between_points(my_point, my_point1))

class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    Corner is a point type 
    """
jerry_rect = Rectangle()
jerry_rect.width = 10
jerry_rect.height = 10
jerry_rect.corner = my_point


def find_center(rect):
    """Returns a Point at the center of a Rectangle.
    rect: Rectangle
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# print_point(find_center(jerry_rect))


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

def print_rectangle(rect):
    print('width: ', rect.width, 'height: ', rect.height)
    print('the lower-left corner is,', rect.corner.x, rect.corner.y)
    print_point(rect.corner)
    
# print_rectangle(jerry_rect)
# grow_rectangle(jerry_rect,5,10)
# print_rectangle(jerry_rect)

def main():
    my_point = Point()
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my point an instance of Point?', isinstance(my_point,Point))
        
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


# if __name__ == '__main__':
#     main()

#--------------------------------------------------------------------------------Exercise 2------------------------------------------------------------------------------------------------


class Circle: 
 """Represents a point in 2-D space.
     attributes: x, y
 """

class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """
my_point = Point()
my_point.x = 1
my_point.y = 1

class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    Corner is a point type 
    """


def point_in_circle(point,circle):
    if (point.x > (circle.center.x + circle.radius)) or (point.x < (circle.center.x - circle.radius)):
        return False
    elif (point.y > (circle.center.y + circle.radius)) or (point.y > (circle.center.y - circle.radius)):
        return False 
    else:
        return True


def rect_in_circle(rect, circle):
    if (rect.corner.x > (circle.center.x + circle.radius)) or (rect.corner.x < (circle.center.x - circle.radius)):
        return False
    elif (rect.corner.y > (circle.center.y + circle.radius)) or (rect.corner.y > (circle.center.y - circle.radius)):
        return False 
    else:
        return True 

def main():
    my_circle = Circle()
    my_circle.center = my_point
    my_circle.center.x = 150
    my_circle.center.y = 100
    my_circle.radius = 75 

    print(point_in_circle(my_point, my_circle))

    jerry_rect = Rectangle()
    jerry_rect.width = 10
    jerry_rect.height = 10
    jerry_rect.corner = my_point

    print(rect_in_circle(jerry_rect, my_circle))

main()

