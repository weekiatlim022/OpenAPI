from django.urls import path
from . import views

urlpatterns = [
    path('heartbeat', views.heartbeat, name='Epoch Time'),
    path('vehicles', views.vehicles_list, name="All Vehicles"),
    path('vehicle/<str:vehicle_id>', views.vehicle_detail, name="Vehicle Details"),
    path('vehicle', views.vehicle_create, name="Create Vehicle"),
    path('vehicle/<str:vehicle_id>/create-or-update', views.vehicle_create_or_update, name="Create or Update Vehicle"),
    path('vehicle/<str:vehicle_id>/update', views.vehicle_update, name="Update Vehicle"),
    path('vehicle/<str:vehicle_id>/delete', views.vehicle_delete, name="Delete Vehicle"),
]