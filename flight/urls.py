from django.urls import path, include
from rest_framework.routers import DefaultRouter
from flight import views

router = DefaultRouter()
router.register('flight', views.FlightViewSet)
router.register('passenger', views.PassengerViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('flightServices/', include(router.urls)),
    path('flightServices/findFlights/', views.find_flights),
    path('flightServices/saveReservation/', views.save_reservation),
]

