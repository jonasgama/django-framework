# Create your views here.
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from contacts.models import Contact, Category
from contacts.permissions import SuperUserContacts
from contacts.serializers import ContactSerializer, CategorySerializer


class ContactsViewSet(viewsets.ModelViewSet):
    permission_classes = (SuperUserContacts,
                          permissions.DjangoModelPermissions,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @action(detail=True, methods=['get'])
    def categories(self, request, pk=None):
        contact = self.get_object()
        serializer = CategorySerializer(contact.category)
        return Response(serializer.data)


class CategoriesViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def contacts(self, request, pk=None):
        self.pagination_class.page_size = 10
        category = self.get_object()
        page = self.paginate_queryset(category.contacts.all())
        serializer = ContactSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
