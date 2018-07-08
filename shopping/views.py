from django.shortcuts import render, get_object_or_404

# Create your views here.
from shopping.models import Goods, GoodsType


def index(request):
    contents = GoodsType.objects.all()
    typegoods = []
    for each in contents:
        a = Goods.objects.filter(goodstype=each)[:3]
        typegoods.append((each, a))
    context = {"typegoods": typegoods, "contents":contents}
    return render(request, 'shopping/home.html', context)


def singlepage(request, foo_id):
    contents = GoodsType.objects.all()
    content = get_object_or_404(GoodsType,id=foo_id)
    typegoods = [(content, Goods.objects.filter(goodstype=content, selling=True)[:5])]
    context = {"typegoods": typegoods, "contents":contents}
    return render(request, 'shopping/home.html', context)

def detail(request, foo_id, goods_id):
    contents = GoodsType.objects.all()
    goods = get_object_or_404(Goods,id=goods_id, selling=True)
    if goods.selling:
        context = {"goods": goods, "contents":contents}
        return render(request, 'shopping/detail.html', context)