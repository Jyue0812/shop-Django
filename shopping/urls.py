from django.urls import path
from shopping import views

app_name = "shopping"
urlpatterns = [
    path('', views.index, name='index'),
    path('<foo_id>/', views.singlepage, name='singlepage'),
    path('<foo_id>/<goods_id>', views.detail, name='detail'),
]