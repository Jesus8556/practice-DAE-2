from django.contrib import admin

# Register your models here.
from .models import Categoria , Post
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post)
