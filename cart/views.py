from django.shortcuts import get_object_or_404
from .cart import Cart
from rest_framework.views import APIView
from product.models import ImageProducts, Product, CollectionProducts
from rest_framework.response import Response
from product.serializers import ProductSerializer, ProductCartSerializer
from .favorites import Favorites
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from .serializers import CartSerializer, OrderSerializer, CartUpdateSerializer
from .models import Order, OrderInfo, OrderProduct
from cart import serializers
import random


class Page12Pagination(PageNumberPagination):
    page_size = 12

class FavoritesListAPIView(ListAPIView):
    """Список избранного"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Page12Pagination

    def list(self, request, *args, **kwargs):
        fav = Favorites(self.request)
        queryset = self.get_queryset()
        if queryset.filter(id__in=fav.fav).count() == 0:
            collection_list = set(queryset.values_list('collection'))
            product = [random.choice(queryset.filter(collection_id = n)) for n in collection_list]
            serializer = self.get_serializer(product[:5], many=True).data
            return Response(data=[{'message': f'В вашем списке избранного пока нет товаров!'}] + serializer)

        page = self.paginate_queryset(queryset.filter(id__in=fav.fav))
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(data=[{'Product_quantity': f'{len(fav.fav)}'}] + serializer.data)

        return Response(data=[{'message': f'В вашем списке избранного {len(fav.fav)} товаров!'}] + serializer.data)
    


class FavoritesAddAPIView(APIView):
    """Добавить товар в избранное"""
    def post(self, request, id):
        fav = Favorites(request)
        product = get_object_or_404(Product, id = id)
        fav.add(product=product)
        return Response(data={'message': 'ok'})


class FavoritesDeleteAPIView(APIView):
    """Удалить из избранного"""
    def post(self, request, id):
        fav = Favorites(request)
        product = get_object_or_404(Product, id = id)
        fav.remove(product=product)
        return Response(data={'message': 'ok'})


class CartListAPIView(APIView):
    """Список корзины"""
    def get(self, request):
        cart = Cart(request)
        product_ids = cart.get_all()
        product = Product.objects.filter(id__in =product_ids)
        products = ProductCartSerializer(product, many=True, context={'filter': cart.cart}).data
        price = cart.get_total_price()
        prices = price['price']
        discount = price['discount_price']
        quantity_in_line = price['quantity_in_line']
        quantity = price['quantity']
        return Response(data = {'product': products , 'price': prices, 'discount': discount, 'total_price': prices-discount, 'quantity':quantity, 'quantity_in_line': quantity_in_line})


class CartOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if not serializer.is_valid():
            return Response(data={'errors':serializer.errors})
        cart = Cart(request)
        name = request.data['name']
        second_name = request.data['second_name']
        email = request.data['email']
        phone = request.data['phone']
        Country = request.data['Country']
        city = request.data['city']
        order = Order.objects.create(name=name,second_name=second_name,email=email,phone=phone,Country=Country,city=city)
        price = cart.get_total_price()
        prices = price['price']
        discount = price['discount_price']
        quantity_in_line = price['quantity_in_line']
        quantity = price['quantity']
        OrderInfo.objects.create(order_id = order.id, price=prices,discount=discount, total_price=prices-discount,quantity=quantity, quantity_in_line=quantity_in_line)
        for k in cart.cart.keys():
            for i in cart.cart[k]['image'].keys():
                quantity=cart.cart[k]['image'][str(int(i))]['quantity']
                OrderProduct.objects.create(order_id= order.id, image_id=int(i), products_id=k, quantity=quantity)
        return Response(data = self.serializer_class(order).data)


class CartAddAPIView(CreateAPIView):
    serializer_class = CartSerializer
    """Добавить товар в корзину"""
    def post(self, request):
        card = Cart(request)
        id = request.data['id']
        image_id = request.data['image_id']
        product = get_object_or_404(Product, id = id)
        card.add(product=product, image_id=image_id)
        return Response(data={'message': 'ok'})


class CartUpdateAPIView(CreateAPIView):
    serializer_class = CartUpdateSerializer
    """Обновляем товар в корзину"""
    def post(self, request):
        card = Cart(request)
        id = request.data['id']
        image_id = request.data['image_id']
        product = get_object_or_404(Product, id = id)
        quantity = request.data['quantity']
        data = card.update(product=product, image_id=image_id, quantity=quantity)
        return Response(data={'message': 'ok'})


class CartDeleteAPIView(APIView):
    """Удалить товар из корзины"""
    def post(self, request, id):
        card = Cart(request)
        product = get_object_or_404(Product, id = id)
        card.remove(product=product)
        return Response(data={'message': 'ok'})


class CartClearAPIVew(APIView):
    """Очистка корзины полностью"""
    def get(self, request):
        card = Cart(request)
        card.clear()
        return Response(data={'message': 'ok'})