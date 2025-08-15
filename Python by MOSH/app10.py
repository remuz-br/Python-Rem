#class sample
class Point:        #declaration
    def move(self): #this is called the method, the self parameter the only means that the function could access attributes or method in its own class
        print("move")

    def draw(self):
        print("draw")


point1 = Point() #creating an object, declaring it similar to declaring a data and storing the class inside
point1.draw() #calling the object and accessing its methods