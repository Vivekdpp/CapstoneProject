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
        return super().__str__()