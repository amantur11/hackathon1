from spam.models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'


    def create(self, validata_data):
        if Contact.objects.filter(email=validata_data['email']).exists():
            raise serializers.ValidationError('ты уже подписан!') 
        return super().create(validata_data)
        