from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ContactView, CategoryView, CategoriesView, ContactsView, CategoriesViewSet, ContactsViewSet

router = SimpleRouter()
router.register('contacts', ContactsViewSet)
router.register('categories', CategoriesViewSet)


urlpatterns = [
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('contacts/<str:pk>', ContactView.as_view(), name='contact'),
    path('contacts/<str:name_pk>/categories/<int:category_fk>', ContactView.as_view(), name='contacts_category'),
    path('categories', CategoriesView.as_view(), name='contacts'),
    path('categories/<int:pk>', CategoryView.as_view(), name='contact'),
    path('categories/<int:category_pk>/contacts', CategoriesView.as_view(), name='category_contacts'),
]