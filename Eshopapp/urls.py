from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Eshopapp.controller import authview, cart, wishlist, order
from Eshopapp.checkout import checkout
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collections/', views.collections, name='collections'),
    path('collections/<str:slug>/', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',
         views.productview, name='productview'),
    path('product-list', views.productlist, name='productlist'),

    path('register/', authview.user_registeration, name='user_registration'),
    path('login/', authview.user_login, name='user_login'),
    path('logout/', authview.user_logout, name='user_logout'),

    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('showwishlist/', wishlist.showwishlist, name='showwishlist'),
    path('add-to-wishlist', wishlist.addtowishlist, name='addtowishlist'),
    path('remove-wishlist-item', wishlist.removeWishlistItem,
         name='removeWishlistItem'),

    path('cart/', cart.cartview, name='cartview'),
    path('update-cart', cart.update_cart, name='update_cart'),
    path('delete-cart-item', cart.delete_cart_item, name='delete_cart_item'),

    path('checkout/', checkout.checkout_items, name='checkout'),
    path('place-order', checkout.placeorder, name='placeorder'),
    path('proceed-to-pay', checkout.razorpaycheck),

    path('my-orders', order.index, name='myorders'),
    path('view-order/<str:t_no>', order.vieworder, name='vieworder'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
