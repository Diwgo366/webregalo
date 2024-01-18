from django.urls import path
from regalo import views

urlpatterns = [
    path('regalo/', views.my_view),
]
