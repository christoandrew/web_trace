from django.contrib import admin

# Register your models here.
from web.models import Topic, Article

admin.site.register(Topic)
admin.site.register(Article)