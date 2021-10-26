from django.db.models import Avg
from rest_framework import serializers
from .models import Category, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Contact
        fields = (
            'id',
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

    def validate_rate(self, value):
        if 1.0 <= value <= 5.0:
            return value
        raise serializers.ValidationError('range between 1 to 5')


class CategorySerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    contacts_averages = serializers.SerializerMethodField()

    def get_contacts_averages(selfs, obj):
        avg = obj.contacts.aggregate(Avg('rate')).get('rate__avg')
        if avg is None:
            return 0
        return round(avg * 2)/2

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'contacts',
            'contacts_averages',
        )
