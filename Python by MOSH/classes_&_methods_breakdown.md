╔══════════════════════════════════════════════════════════╗
║                🐍 PYTHON: CLASSES & FUNCTIONS             ║
╚══════════════════════════════════════════════════════════╝

1. CLASS → The blueprint / recipe
   ┌───────────────────────────────────────┐
   │ class Dog:                             │
   │     def bark(self):                    │  <- Method (inside class)
   │         print("Woof!")                 │
   └───────────────────────────────────────┘

2. OBJECT → A thing made from the class
   ┌───────────────────────────┐
   │ my_dog = Dog()            │  <- Object (instance of Dog)
   └───────────────────────────┘

3. METHOD → A function that belongs to a class
   - Always defined *inside* the class.
   - First parameter is `self` (the object itself).
   - Called with a dot:
       my_dog.bark()
   - Under the hood:
       Dog.bark(my_dog)

4. FUNCTION → Independent code block
   - Defined *outside* any class.
   - Called directly with arguments.
     Example:
       def greet(name):
           print("Hello", name)

       greet("Alice")   # passes "Alice" explicitly

5. BUILT-IN FUNCTION vs METHOD
   - Built-in function: works on many types
       len("abc")   # works on strings, lists, tuples, etc.
   - Method: specific to that object’s type
       "abc".upper()   # only for strings

6. BIG PICTURE:
   ┌─────────────┐
   │ CLASS       │   ← defines methods & attributes
   └─────┬───────┘
         │
         ▼
   ┌─────────────┐
   │ OBJECT      │   ← "instance" of a class
   └─────┬───────┘
         │
         ▼
   obj.method()  ← method gets `self` automatically
   func(obj)     ← you pass the object yourself