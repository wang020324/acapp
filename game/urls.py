from django.urls import path
from game.views import index # 掉包函数


urlpatterns = [
        path("",index,name="index"),
]

