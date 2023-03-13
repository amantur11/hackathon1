from rest_framework import serializers
from .models import About, News, Help, HelpImages, Offer, FooterTwo, FooterOne


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = 'title text get_images'.split()


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'images title text'.split()


class HelpImagesSerialiser(serializers.ModelSerializer):
    class Meta:
        model = HelpImages
        fields = '__all__'


class HelpISerialiser(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = 'question answer'.split()


class OfferSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = 'title text'.split()


class FooterOneSerialiser(serializers.ModelSerializer):
    class Meta:
        model = FooterOne
        fields = '__all__'


class FooterTwoSerialiser(serializers.ModelSerializer):
    class Meta:
        model = FooterTwo
        fields = '__all__'