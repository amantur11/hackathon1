from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from product.models import Product
from product.views import ProductAPIView, ProductModelViewSet
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView



User = get_user_model()


class ProductTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

        product = [
            Product(title='cat1'),
            Product(title='cat2'),
            Product(title='cat3')
        ]
        Product.objects.bulk_create(product)

        self.setup_user()


    def setup_user(self):
        self.user = User.objects.create_user(
            email = 'test2@test2.com',
            password= 'test123',
            is_active = True
        )
    
    def test_get_product(self):
        request = self.factory.get('api/v1/product')
        view = ProductAPIView.as_view({'get': 'list'})
        response = view(request)
        print(response.data)
        assert response.status_code
        assert len(response.data)
        assert response.data[0]['title'] == 'cat1'

    def test_post_product(self):
        data = {
            'title': 'cat4'
        }
        request = self.factory.post('api/v1/product/',data)
        force_authenticate(request, self.user)
        view = ProductAPIView.as_view({'post': 'create'})
        response = view(request)


        assert response.status_code == 201
        assert Product.objects.filter(title='cat4').exists()


class Producttest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.setup_product()
        self.setup_user()
        self.access_token = self.setup_user_token()



    def setup_user_token(self):
        data = {
            'email': 'test2@test2.com',
            'password': 'test123'
        }

        request = self.factory.post('api/v1/account/login/', data)
        view = TokenObtainPairView.as_view()
        response = view(request)

        return response.data['access']
    

    @staticmethod
    def setup_product():
        product =[
            Product(title='c1'),
            Product(title='c2'),
            Product(title='c3'),
        ]  
    
        Product.objects.bulk_create(product)

       
    def setup_user(self):
        self.user = User.objects.create_user(
            email = 'test2@test2.com',
            password='test123',
            is_active = True
        )

    def test_post_product(self):
        image = open('media/products/test.png','rb')
        print(image)
        data = {
            'category': Product.objects.first(),
            'title': 'test_product',
            'price': 20,
            'amount': 20,
            'image': image
        }


        request = self.factory.post('api/v1/product/modelviewset_crud/', data, HTTP_AUTHORIZATION='Bearer' + self.access_token)
        view = ProductModelViewSet.as_view({'post':'create'})
        response = view(request)

        assert response.status_code == 201
        assert Product.objects.filter(title='test_product').exists()



