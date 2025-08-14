class Person:
    def __init__(self, name):
        self.name = name  # "self.name" belongs to *this* object
    
    def greet(self):
        return f"Hi, I'm {self.name}."

p1 = Person("Remuel")
p2 = Person("Alex")

print(p1.greet())  # Hi, I'm Remuel.
print(p2.greet())  # Hi, I'm Alex.