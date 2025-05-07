from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_price, name='predict_price'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
]