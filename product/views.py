from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, CollectionProducts, Slider, CallBack
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ProductListSerializer, CollectionSerializer, ProductDetailSerializer, BenefistSerializer, SliderSerializer, ProductSerializer, CallbackSesializer
from rest_framework import status, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.db.models import Q
from about_us.models import Benefits
from cart.favorites import Favorites
from rest_framework import filters
import random
from rest_framework.decorators import api_view, permission_classes
from product.tasks import big_function



class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# class ProductListAPIView(APIView):  
#     queryset = Product.objects.all()    
#     pagination_class = PageNumberPagination
#     serializer_class = ProductListSerializer


    # def get_serializer_context(self):
    #     fav = Favorites(self.request)
    #     return {'fav': fav.fav}
        


class Page4Pagination(PageNumberPagination):
    page_size = 4

# class MainSliderAPIView(ListAPIView):
#     queryset = Slider.objects.all()
#     serializer_class = SliderSerializer

class MainSliderAPIView(APIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    


# class MainBenefistAPIView(ListAPIView):
#     queryset = Benefits.objects.all()
#     serializer_class = BenefistSerializer
#     pagination_class = Page4Pagination


class MainBenefistAPIView(APIView):
    queryset = Benefits.objects.all()
    serializer_class = BenefistSerializer
    pagination_class = Page4Pagination


class MainPageHitAPIVIew(ListAPIView):
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer

    def get_serializer_context(self):
        fav = Favorites(self.request)
        return {'fav': fav.fav}

    def get_queryset(self):
        return Product.objects.filter(checkbox_hit=True)


# class MainPageNewAPIVIew(ListAPIView):
#     queryset = Product.objects.all()
#     pagination_class = PageNumberPagination
#     serializer_class = ProductListSerializer
class MainPageNewAPIVIew(APIView):
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer

    def get_serializer_context(self):
        fav = Favorites(self.request)
        return {'fav': fav.fav}

    def get_queryset(self):
        return Product.objects.filter(checkbox_new=True)


class ProductDetailAPIView(APIView):

    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer


    def get(self, request, id):
        fav = Favorites(request)
        try:    
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
        products = Product.objects.filter(~Q(id = product.id) & Q(collection_id = product.collection_id))
        data_2 = ProductListSerializer(products[:5], many=True, context = {'fav': fav.fav}).data
        data = ProductDetailSerializer(product, context = {'fav': fav.fav}).data
        return Response(data=[data, data_2])


# class CollectionListAPIView(ListAPIView):
#     queryset = CollectionProducts.objects.all()
#     pagination_class = PageNumberPagination
#     serializer_class = CollectionSerializer
class MainPageNewAPIVIew(APIView):
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer



# class SearchAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     pagination_class = PageNumberPagination
#     serializer_class = ProductListSerializer
class SearchAPIView(APIView):
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer
    
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())


        if queryset.count() == 0:
            queryset = self.queryset
            collection_list = set(queryset.values_list('collection'))
            product = [random.choice(queryset.filter(collection_id = n)) for n in collection_list]
            serializer = self.get_serializer(product[:5], many=True).data
            return Response(data=[{'message': f'По вашему запросу ничего не найдено!'}] + serializer)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(data=serializer.data + [{'check_list' : queryset.values_list('title')}])

        return Response(data=serializer.data)
    
    def get_serializer_context(self):
        fav = Favorites(self.request)
        return {'fav': fav.fav}


    

class CollectionDetailAPIView(ListAPIView):
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(collection_id=id)

    def get_serializer_context(self):
            fav = Favorites(self.request)
            return {'fav': fav.fav}


class Page5Pagination(PageNumberPagination):
    page_size = 5


class CollectionNewAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = Page5Pagination

    def get_queryset(self):
        return Product.objects.filter(checkbox_new = True)

    def get_serializer_context(self):
            fav = Favorites(self.request)
            return {'fav': fav.fav}


class CallbackAPIView(CreateAPIView):
    queryset = CallBack.objects.all()
    serializer_class = CallbackSesializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if not serializer.is_valid():
            return Response(data={'errors':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        phone = request.data.get('phone')
        movie = CallBack.objects.create(name=name, phone=phone)
        return Response(data={'message': "ok"}, status=status.HTTP_201_CREATED)


class ProductModelViewSet(viewsets.ModelViewSet):  # полный крад 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class ProductMixin(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.ListModelMixin,
#                     viewsets.GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



