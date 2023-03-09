from django.urls import path

from property.views import properties, property_single, property_edit, property_create, property_delete

app_name = 'property'

urlpatterns = [
    path('', properties, name='properties'),  # http://127.0.0.1:8000/property/
    path('property_detail/<int:id>/', property_single),
    path('property_edit/<int:id>/', property_edit),
    path('create/', property_create),
    path('property_delete/<int:id>/', property_delete)
    ]
