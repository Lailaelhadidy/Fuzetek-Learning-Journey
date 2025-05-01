class Circle:
    def __init__(self, radius=None ):
        self.__radius= radius

    def Setradius(self, radius):
        self.__radius= radius

    def Getradius(self):
        return self.__radius

    def Getarea(self):
        return 3.14* (self.__radius ** 2)

    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)

    def __lt__ (self, another_circle): #>
        return self.__radius < another_circle.__radius
        #will return true of first<second

    def __gt__ (self, another_circle): #<
        return self.__radius > another_circle.__radius
        #will return true of first>second

    def __str__(self):
        return "Circle radius : " + str(self.__radius) #str for casting to change datatype
    #__str__ for printing object alone so when print(c1) he will give "Circle radius : 10"

c1= Circle(10)
c2= Circle(20)
c3= c1>c2
print(c3)
