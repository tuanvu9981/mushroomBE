from django.urls import path
from mushroomCLSF.views import test_function

urlpatterns = [
    path('hello', test_function),
]
