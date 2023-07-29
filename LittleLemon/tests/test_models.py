from django.test import TestCase
from restaurant.models import Menu
        
# Import the TestCase class from the django.tests module.
# Use it as base and declare a test class, for example, MenuTest. 
# Define an instance method that adds a new instance of the Menu model. 
# Call the assertEqual() method of the test class that compares the string representation of the newly added object with the anticipated value.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")