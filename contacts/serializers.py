from rest_framework import serializers
from .models import Category, Contact


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


class CategorySerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'name',
            'contacts'
        )
