from django.urls import path, include
from . import views
from .views import ContactView, CategoryView

urlpatterns = [
    path('contacts', ContactView.as_view(), name='contacts'),
    path('categories', CategoryView.as_view(), name='contacts')
]