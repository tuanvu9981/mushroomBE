from django.urls import path
from mushroomCLSF.views import test_function, test

urlpatterns = [
    path('hello', test_function),
    path('test', test),
]
