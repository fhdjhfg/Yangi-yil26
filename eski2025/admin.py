from django.contrib import admin
from .models import Category,CategoryListApiView,
# Register your models here.

# Register your models here.


admin.site.register(CategoryListApiView)

class CategoryListApiView(admin.ModelAdmin):
    malumot = ('mavzu', 'vaxt', 'created_at')


