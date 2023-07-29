from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from test_models import MenuItemTest

class MenuViewTest(TestCase):
    def setup(self):
        self.menu_data =[
            #self.menu_data is assumed to be a list of dictionaries, where each dictionary contains data for creating a new Menu instance.
            {'title' : 'item1' , 'price': 3.99 },
            {'title': 'item2' , 'price' : 1.99},     
        ]
        self.menus = [] #This line initializes an empty list named menus. This list will be used to store the instances of the Menu model that we'll create in the following loop.
        # This line starts a loop that iterates over each item in the self.menu_data list. 
        
        for data in self.menu_data:
            menu = MenuItemTest.objects.create(**data)
            self.menus.append(menu)
            
        # Inside the loop, this line creates a new instance of the Menu model using the create() method provided by the Django's Object-Relational Mapping (ORM). 
        # The data dictionary contains the attributes for the Menu model, and by using the double asterisk (**), we unpack the dictionary and pass its key-value pairs as keyword arguments to the create() method. 
        # This way, the method can create a new Menu object with the provided data.
        # For example, if data is {'title': 'Menu Item 1', 'price': 9.99}, the create() method will create a new Menu instance with the title attribute set to 'Menu Item 1' and the price attribute set to 9.99.
        # After creating the Menu instance, we add it to the menus list using the append() method. This way, we keep track of all the test instances we've created during the loop.
        
    # Test methods in a unittest.TestCase class are methods whose names start with the prefix test_. 
    # When you run your test case, the test runner identifies and executes all the test methods.    
        
    def test_getall(self):
        all_menus = MenuItemTest.objects.all()
        serializer = MenuSerializer(all_menus, many=True) # This line creates a serializer instance named serializer by passing all_menus to the MenuSerializer class constructor.
        serialized_data = serializer.data  # The second argument, many=True, is used because we are serializing a QuerySet with multiple Menu instances. This informs the serializer that it needs to handle multiple objects.

        # Assert that the serialized data equals the response
        self.assertEqual(len(serialized_data), len(self.menu_data))  # This line is an assertion that checks whether the number of items in the serialized_data matches the number of items in the self.menu_data.
        
        # for i, menu_data in enumerate(self.menu_data):
        #     for key in menu_data.keys():
        #         self.assertEqual(serialized_data[i][key], menu_data[key])