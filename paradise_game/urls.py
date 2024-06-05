from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from games.views import HomeTemplate, ShopTemplate, AboutTemplate, ContactTemplate, LoginTemplate, CartTemplate, WishlistTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplate.as_view(), name='home'),
    path('shop/', ShopTemplate.as_view(), name='shop'),
    path('about/', AboutTemplate.as_view(), name='about'),
    path('contact/', ContactTemplate.as_view(), name='contact'),
    path('login/', LoginTemplate.as_view(), name='login'),
    path('cart/', CartTemplate.as_view(), name='cart'),
    path('wishlist/', WishlistTemplate.as_view(), name='wishlist'),
    path('user/', include('users.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
