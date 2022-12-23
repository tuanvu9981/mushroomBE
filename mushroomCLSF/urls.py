# TEST FOR FUN. DONT CARE THIS
from mushroomCLSF.views.test_api import test_function, test

# REAL WORK HERE !
from django.urls import path
from mushroomCLSF.views.naive_bayes_view import naive_bayes_classify
from mushroomCLSF.views.decision_tree_view import decision_tree_classify

urlpatterns = [
    path('hello', test_function),
    path('test', test),

    path('naive-bayes', naive_bayes_classify),
    path('decision-tree', decision_tree_classify),
]
