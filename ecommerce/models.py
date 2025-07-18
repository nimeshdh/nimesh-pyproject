# from django.db import model























# class Animal:
#     def speak(self):
#         print("Animal function invoked")


# class Dog(Animal):
#     def speak(self):
#         print("Dog class function invoked")

#     def parentspeak(self):
#         super().speak()


# animal = Animal()
# animal.speak()         # Output: Animal function invoked

# dog = Dog()
# dog.parentspeak()      # Output: Animal function invoked
# dog.speak()








# class Student:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height

#     def greet(self):
#         print(
#             f"Hello, welcome to this class. My name is {self.name} and I am {self.age} years old.")


# student1 = Student("nimesh", 20, 5)
# student1.greet()

# class Users(models.Model):  # removed the extra space after 'models.'
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     birth_date = models.DateField(null=True)


# class Products(models.Model):
#     STATUS = [
#         ('P', 'Pending'),
#         ('C', 'Complete'),
#         ('F', 'Failed'),
#     ]

#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     payment_status = models.CharField(
#         max_length=1,
#         choices=STATUS,
#         default='P'  
#     )
