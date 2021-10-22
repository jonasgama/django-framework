# Create your views here.
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from contacts.models import Contact, Category
from contacts.serializers import ContactSerializer, CategorySerializer


class ContactsView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_pk = self.kwargs.get('category_pk')
        if category_pk:
            return Contact.objects.filter(category=category_pk)
        return self.queryset.all()


class ContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_object(self):
        name_pk = self.kwargs.get('name_pk')
        category_fk = self.kwargs.get('category_fk')
        print(name_pk and category_fk)
        if name_pk and category_fk:
            return get_object_or_404(self.get_queryset(),
                                     name=name_pk,
                                     category=category_fk)
        return self.queryset.all()


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContactsViewSet(viewsets.ModelViewSet):
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
        category = self.get_object()
        serializer=ContactSerializer(category.contacts.all(), many=True)
        return Response(serializer.data)
