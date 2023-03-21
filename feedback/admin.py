from django.contrib import admin
from feedback.models import Like, Rating, Favorite



admin.site.register(Like)
# admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favorite)
