from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import mixins, viewsets
from spam.models import Contact
from spam.serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated

class ContactAPIView(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(email=self.request.user.email)

    