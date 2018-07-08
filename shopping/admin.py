from django.contrib import admin

# Register your models here.
from shopping.models import GoodsType, Goods

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'goodstype','price','stock','selling','createdat', 'updatedat']
    list_editable = ['name', 'goodstype', 'price', 'stock', 'selling']
    list_per_page = 10


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(Goods, GoodsAdmin)