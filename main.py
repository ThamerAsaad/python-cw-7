
# write your code here
class Person:

    def __init__(self , name, age  ):
        
         self.name = name
         self.age = age
    # name = "thamer"
    # age = 19 

    def is_adult(self):
        if self.age >= 18:
            print("You have too much responsibilities")
        elif self.age < 18:
            print("Lucky you")
    
    def __str__(self):
        return f"My {self.name} is John and I am {self.age} years old "



first_person =Person("Thamer" , 19)
first_person.is_adult()
print(first_person)