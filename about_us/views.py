from django.shortcuts import render
from rest_framework.views import APIView
from .models import About, News, HelpImages, Help, Offer, FooterOne, FooterTwo
from .serializers import AboutSerializer, NewsSerializer, HelpImagesSerialiser, HelpISerialiser, OfferSerialiser, FooterOneSerialiser, FooterTwoSerialiser
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

class AboutUsAPIView(ListAPIView):
    """О нас"""
    serializer_class = AboutSerializer
    """API О нас"""
    def get(self, request):
        model = About.objects.all()
        data = AboutSerializer(model, many=True).data

        return  Response(data=data)      


class NewsListAPIView(ListAPIView):
    """API Новостей"""
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    queryset = News.objects.all()


class HelpAPIViews(ListAPIView):
    serializer_class = HelpISerialiser
    """API помощь"""
    def get(self, request):
        model = Help.objects.all()
        images = HelpImages.objects.all()
        data = HelpISerialiser(model, many=True).data
        image = HelpImagesSerialiser(images, many=True).data
        return  Response(data=image+data)  


class OfferAPIView(APIView):
    """API offer"""
    def get(self, request):
        offer = Offer.objects.all()
        data = OfferSerialiser(offer, many=True).data
        return Response(data=data)


class FooterAPIView(APIView):
    def get(self, request):
        footerone = FooterOne.objects.all()
        footertwo = FooterTwo.objects.all()
        data = FooterOneSerialiser(footerone, many=True).data
        data2 = FooterTwoSerialiser(footertwo, many=True).data
        return Response(data=data+[{'second' :data2}])