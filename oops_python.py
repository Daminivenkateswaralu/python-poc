
class polygon():
    def __init__(self, sides):
        self.sidesNumber = sides
        print("The number of sides of Polygon is " + str(self.sidesNumber))
    def sideLengths(self):
        self.sides = [float(input("Enter length of side "+str(i+1)+" : \t")) for i in range(self.sidesNumber)]
    def perimeter(self):
        a=0
        for i in range(len((self.sides))):
            a += self.sides[i]
        return a

class triangle(polygon):
    def __init__ (self):
        polygon.__init__(self,3)

class square(polygon):
    def __init__ (self):
        print("The number of sides for square is 4 and length of all sides are equal")
    def sideLengths(self):
        self.sides = float(input("Enter Square side length: \t"))
    def perimeter(self):
        return self.sides*4
    def area(self):
        return (self.sides*self.sides)

polygon_obj = polygon(5)
polygon_obj.sideLengths()
perimeter = polygon_obj.perimeter()
print("Perimeter of polygon with " + str(polygon_obj.sidesNumber) + " sides is " + str(perimeter))

# Inheritance
triangle_obj = triangle()
triangle_obj.sideLengths()
tri_perimeter= triangle_obj.perimeter()
print("Perimeter of triangle is " + str(tri_perimeter))

# Polymorphism
square_obj = square()
square_obj.sideLengths()
square_perimeter= square_obj.perimeter()
square_area= square_obj.area()
print("Perimeter of square is " + str(square_perimeter) + "\n Area of square is " + str(square_area))