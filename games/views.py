from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min
import json
from django.views.decorators.http import require_POST
from django.contrib.auth.models import AnonymousUser

from .models import GameModel, GenreModel, GameModeModels, PlatformModels, CartModel, OrderModel


class HomeTemplate(ListView):
    template_name = 'index.html'
    queryset = GameModel.objects.all()
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if isinstance(self.request.user, AnonymousUser):
            context['cart_items'] = 0
        else:
            context['cart_items'] = CartModel.objects.filter(user=self.request.user)
        return context


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
        if isinstance(self.request.user, AnonymousUser):
            context['cart_items'] = 0
        else:
            context['cart_items'] = CartModel.objects.filter(user=self.request.user)

        context['min_price'], context['max_price'] = GameModel.objects.aggregate(
            Min('price'),
            Max('price')
        ).values()

        return context


class AboutTemplate(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if isinstance(self.request.user, AnonymousUser):
            context['cart_items'] = 0
        else:
            context['cart_items'] = CartModel.objects.filter(user=self.request.user)
        return context


class ContactTemplate(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if isinstance(self.request.user, AnonymousUser):
            context['cart_items'] = 0
        else:
            context['cart_items'] = CartModel.objects.filter(user=self.request.user)
        return context


@login_required
def add_to_cart(request):
    print("add_to_cart view called")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            game_id = data.get('game_id')
            quantity = int(data.get('quantity', 1))
            print(f"game_id: {game_id}, quantity: {quantity}")
            if not game_id:
                raise ValueError("game_id is missing")
            game = get_object_or_404(GameModel, id=game_id)
            cart_item, created = CartModel.objects.get_or_create(user=request.user, game=game)
            if not created:
                cart_item.quantity = quantity  # Update the quantity if item already exists in cart
            else:
                cart_item.quantity = quantity  # Set the quantity if it's a new item in cart
            cart_item.save()
            return JsonResponse({'message': 'Added to cart'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
def view_cart(request):
    cart_items = CartModel.objects.filter(user=request.user)
    total_price = sum(item.game.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def place_order(request):
    if request.method == 'POST':
        cart_items = CartModel.objects.filter(user=request.user)
        if cart_items.exists():
            for item in cart_items:
                OrderModel.objects.create(
                    user=request.user,
                    game=item.game,
                    quantity=item.quantity
                )
                item.delete()
            return JsonResponse({'message': 'Order placed successfully'})
        return JsonResponse({'message': 'No items in cart'}, status=400)


@login_required
@require_POST
def remove_from_cart(request):
    try:
        data = json.loads(request.body)
        game_id = data.get('game_id')
        if not game_id:
            return JsonResponse({'error': 'game_id is missing'}, status=400)
        cart_item = CartModel.objects.filter(user=request.user, game_id=game_id).first()
        if cart_item:
            cart_item.delete()
            return JsonResponse({'message': 'Item removed from cart'})
        return JsonResponse({'error': 'Item not found in cart'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def clear_cart(request):
    CartModel.objects.filter(user=request.user).delete()
    return redirect('view_cart')
# @login_required
# def view_orders(request):
#     orders = OrderModel.objects.filter(user=request.user)
#     return render(request, 'orders.html', {'orders': orders})
