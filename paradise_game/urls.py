from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from games.views import HomeTemplate, ShopTemplate, AboutTemplate, ContactTemplate, add_to_cart,\
    view_cart, place_order, remove_from_cart, clear_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplate.as_view(), name='home'),
    path('shop/', ShopTemplate.as_view(), name='shop'),
    path('about/', AboutTemplate.as_view(), name='about'),
    path('contact/', ContactTemplate.as_view(), name='contact'),
    # path('login/', LoginTemplate.as_view(), name='login'),
    # path('cart/', CartTemplate.as_view(), name='cart'),
    # path('wishlist/', WishlistTemplate.as_view(), name='wishlist'),
    path('user/', include('users.urls')),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('place-order/', place_order, name='place_order'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('clear-cart/', clear_cart, name='clear_cart'),
    # path('orders/', view_orders, name='view_orders')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
