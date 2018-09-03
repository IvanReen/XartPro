from django.conf.urls import url

from art import views

urlpatterns = [
    url(r'^show/(\d+)/', views.show),
    url(r'^qbuy/(\d+)/', views.qbuy),
    url(r'^buystate/(\d+)/', views.buystate),
]
