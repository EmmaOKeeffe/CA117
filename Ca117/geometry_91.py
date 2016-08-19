class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5

class Shape(object):
    
    def __init__(self, p1):
        self.p1 = p1
        

    def side(self):
        l = [self.p1, self.p2, self.p3]
        return l

    def circumference(self):
        return self.p1 + self.p2 + self.p3

class Triangle(Shape):
    
    def area(self):
        s = (self.p1 + self.p2 + self.p3) / 2
        a = (s(s - self.p1)(s - self.p2)(s - self.p3))**0.5

class Square(Shape):
    
    def area(self):
         return self.p1 ** 2

def main():

    t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
    print(t1.sides())
    print(t1.circumference())
    print(t1.area())

    s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
    print(s1.sides())
    print(s1.circumference())
    print(s1.area())

if __name__ == '__main__':
    main()
