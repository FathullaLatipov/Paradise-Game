from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Max, Min

from .models import GameModel, GenreModel, GameModeModels, PlatformModels


class HomeTemplate(ListView):
    template_name = 'index.html'
    queryset = GameModel.objects.all()
    context_object_name = 'games'


class ShopTemplate(ListView):
    template_name = 'shop-page.html'
    context_object_name = 'games'
    paginate_by = 9

    def get_queryset(self):
        qs = GameModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        genre = self.request.GET.get('genre')
        game_mode = self.request.GET.get('game_mode')
        platform = self.request.GET.get('platform')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if genre:
            qs = qs.filter(genre_id=genre)

        if game_mode:
            qs = qs.filter(game_mode_id=game_mode)

        if platform:
            qs = qs.filter(platform_id=platform)

        if price:
            min_price, max_price = map(float, price.split(';'))
            qs = qs.filter(price__gte=min_price, price__lte=max_price)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = GenreModel.objects.all()
        context['game_models'] = GameModeModels.objects.all()
        context['platforms'] = PlatformModels.objects.all()

        context['min_price'], context['max_price'] = GameModel.objects.aggregate(
            Min('price'),
            Max('price')
        ).values()

        return context


class AboutTemplate(TemplateView):
    template_name = 'about-us.html'


class ContactTemplate(TemplateView):
    template_name = 'contact.html'


class LoginTemplate(TemplateView):
    template_name = 'login-register.html'


class CartTemplate(TemplateView):
    template_name = 'cart.html'