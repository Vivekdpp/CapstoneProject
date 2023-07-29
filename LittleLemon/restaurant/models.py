from django.db import models

# Create your models here.


class Booking(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self) -> str:
        return super().__str__()
    
class Menu(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    inventory = models.IntegerField()  
    
    def __str__(self) -> str:
        return super().__str__() # Here, the __str__ method is defined to call the __str__ method of the superclass using super().__str__(). By doing this, it will return the string representation of the object as defined in the superclass. This is useful when you want to extend the functionality of the superclass's __str__ method in a subclass, and you still want to retain some of the original behavior.
    # or 
    # def __str__(self):
    #   return f'{self.title} : {str(self.price)}' , Here,  the __str__ method is defined to create a custom string representation for the object. It uses an f-string to format the output, where self.title and self.price are attributes of the object. The method returns a string containing the title and price in a specific format. For example, if self.title is "Product A" and self.price is 19.99, the __str__ method would return the string: "Product A : 19.99".
