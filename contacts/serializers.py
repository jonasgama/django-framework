from rest_framework import serializers
from .models import Category, Contact


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Contact
        fields = (
            'name',
            'lastName',
            'telephone',
            'email',
            'creation_date',
            'update_date',
            'enable',
            'rate',
            'category'
        )
