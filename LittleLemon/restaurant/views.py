from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerializer  # Import the MenuSerializer or replace with your serializer
from .models import Menu, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
   return render(request, 'index.html', {})

# ListCreateAPIView will handle both GET(list) and POST(create) method calls.
# We set the queryset to retrieve all Menu instances, and 
# the serializer_class to use the MenuSerializer for serialization and deserialization.

class MenuItemsView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()  # Replace 'Menu' with the name of your model
    serializer_class = MenuSerializer # Replace with your serializer
    
 # RetrieveUpdateDestroyAPiView will handle for GET (Retrieve), PUT (Update), and DELETE (Destroy) method calls.  
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Replace 'Menu' with the name of your model
    serializer_class = MenuSerializer # Replace with your serializer
    
class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  # Replace 'Menu' with the name of your model
    serializer_class = BookingSerializer