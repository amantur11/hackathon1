from rest_framework import serializers
from cart import favorites
from .models import Product, CollectionProducts, Slider, ImageProducts, CallBack
from about_us.models import Benefits
# from product.models import Like, Rating, Favorite


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    favo = serializers.SerializerMethodField('fav')

    class Meta:
        model = Product
        fields = '__all__'


    def fav(self, obj):
        favorites = self.context.get('fav')
        print(favorites)
        if obj.id in favorites:
            return True
        return False


class ProductCartSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField('get_quantity')
    image = serializers.SerializerMethodField('get_image')
    class Meta:
        model = Product
        fields = '__all__'

    def get_quantity(self, obj):
        quantity = self.context.get('filter')[str(obj.id)]['quantity']
        return quantity
    def get_image(self, obj):
        id = self.context.get('filter')[str(obj.id)]['image']
        return id

class MainSerializer(serializers.ModelSerializer):
    def get_attribute(self, instance):
        return super().get_attribute(instance)



class BenefistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = '__all__'
        


class ProductDetailSerializer(serializers.ModelSerializer):
    favo = serializers.SerializerMethodField('fav')

    class Meta:
        model = Product
        # fields = 'id get_images title vendor_code text size_range cloth quantity_in_line material checkbox_hit checkbox_new collection price discount new_price favo'.split()
        fields = '__all__'

    def fav(self, obj):
        favorites = self.context.get('fav')
        print(favorites)
        if obj.id in favorites:
            return True
        return False


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionProducts
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class CallbackSesializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=5)
    phone = serializers.CharField(max_length=100)

    class Meta:
        model = CallBack
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.email')
    
    
    class Meta:
        model = Product
        fields = '__all__'


