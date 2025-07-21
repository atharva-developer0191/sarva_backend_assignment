from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include
from .import views

urlpatterns = [
    path('api/wheel-specification/submit/', views.submit_wheel_specification),
    path("api/bogie-checksheet/submit/", views.submit_bogie_checksheet, name="submit_bogie_checksheet"),
    path('api/wheel-specification/', views.get_wheel_specifications),
]