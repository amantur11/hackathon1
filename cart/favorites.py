from django.conf import settings
from product.models import Product


class Favorites(object):
    """class избранного"""
    def __init__(self, request):
        """
        Инициализируем избранного
        """
        self.session = request.session
        fav = self.session.get(settings.FAV_SESSION_ID)
        if not fav:
            fav = self.session[settings.FAV_SESSION_ID] = []
        self.fav = fav


    def add(self, product):
        """метод для добавления"""
        product_id = product.id
        if product_id not in self.fav:
            self.fav.append(product_id)
            self.save()
            

    def save(self):
        """Обновление сессии fav"""
        self.session[settings.FAV_SESSION_ID] = self.fav
        #Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True


    def remove(self, product):
        """Удаление товара из избранного"""
        
        product_id = product.id
        if product_id in self.fav:
            print(self.fav)
            self.fav.remove(product_id)
            self.save()

    def clear(self):
        # удаление избранного из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True