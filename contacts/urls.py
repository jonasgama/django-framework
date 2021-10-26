from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CategoriesViewSet, ContactsViewSet

router = SimpleRouter()
router.register('contacts', ContactsViewSet)
router.register('categories', CategoriesViewSet)


urlpatterns = [
]