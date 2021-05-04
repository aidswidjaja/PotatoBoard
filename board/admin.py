from django.contrib import admin

from .models import Post, Emergency, Information

admin.site.register(Post)
admin.site.register(Emergency)
admin.site.register(Information)