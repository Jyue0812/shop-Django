from django.db import models

# Create your models here.
# 商品类别
class GoodsType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category',blank=True)

    class Meta:
        db_table = 'GoodsType'
        verbose_name_plural = 'GoodsType'

    def __str__(self):
        return self.name

# 产品列表
class Goods(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category',blank=True)
    goodstype = models.ForeignKey(GoodsType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    stock = models.BooleanField(default=0)
    # 已上架
    selling = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Goods'
        ordering = ('createdat',)
        verbose_name_plural = 'Goods'

    def __str__(self):
        return self.name