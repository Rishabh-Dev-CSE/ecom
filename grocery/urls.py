

from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('category/<int:id>', views.categorypage),
    path('products/<int:id>', views.productDetails),
    path('addtocart', views.addtocart),
    path('loginuser', views.loginUser),
    path('cart', views.viewCart),
    path('deletecart', views.deleteCart),
    path('updatecart', views.updateCart),
    path('checkout', views.checkout),
    path('complete_payment', views.success),
    path('myorder',views.orderlist)

    
]
