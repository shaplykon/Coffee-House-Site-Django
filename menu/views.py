from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from article.models import Post
from .models import Coffee, Tea, Dessert


class CoffeeView(ListView):
    model = Coffee
    template_name = 'menu/coffee.html'


class DessertsView(ListView):
    model = Dessert
    template_name = 'menu/desserts.html'


class TeaView(ListView):
    model = Tea
    template_name = 'menu/tea.html'


def detail_coffee(request, id):
    coffee = get_object_or_404(Coffee, id=id)
    if request.method == 'POST':
        coffee = get_object_or_404(Coffee, id=request.POST.get('product_id'))
        if coffee.favourite.filter(id=request.user.id).exists():
            coffee.favourite.remove(request.user)
            in_favourite = False
        else:
            coffee.favourite.add(request.user)
            in_favourite = True
    else:
        in_favourite = False
        if coffee.favourite.filter(id=request.user.id).exists():
            in_favourite = True
    return render(request, 'menu/coffee_detail.html', {'coffee': coffee, 'in_favourite': in_favourite})


def detail_dessert(request, id):
    dessert = get_object_or_404(Dessert, id=id)
    if request.method == 'POST':
        dessert = get_object_or_404(Dessert, id=request.POST.get('product_id'))
        if dessert.favourite.filter(id=request.user.id).exists():
            dessert.favourite.remove(request.user)
            in_favourite = False
        else:
            dessert.favourite.add(request.user)
            in_favourite = True
    else:
        in_favourite = False
        if dessert.favourite.filter(id=request.user.id).exists():
            in_favourite = True
    return render(request, 'menu/dessert_detail.html', {'dessert': dessert, 'in_favourite': in_favourite})


def detail_tea(request, id):
    tea = get_object_or_404(Tea, id=id)
    if request.method == 'POST':
        tea = get_object_or_404(Tea, id=request.POST.get('product_id'))
        if tea.favourite.filter(id=request.user.id).exists():
            tea.favourite.remove(request.user)
            in_favourite = False
        else:
            tea.favourite.add(request.user)
            in_favourite = True
    else:
        in_favourite = False
        if tea.favourite.filter(id=request.user.id).exists():
            in_favourite = True
    return render(request, 'menu/tea_detail.html', {'tea': tea, 'in_favourite': in_favourite})


def favourites(request):
    full_coffee_list = Coffee.objects.all()
    full_tea_list = Tea.objects.all()
    full_desserts_list = Dessert.objects.all()
    full_post_list = Post.objects.all()
    tea_list = []
    coffee_list = []
    desserts_list = []
    posts_list = []
    for coffee in full_coffee_list:
        for user in coffee.favourite.all():
            if user.get_username() == request.user.get_username():
                coffee_list.append(coffee)

    for tea in full_tea_list:
        for user in tea.favourite.all():
            if user.get_username() == request.user.get_username():
                tea_list.append(tea)

    for dessert in full_desserts_list:
        for user in dessert.favourite.all():
            if user.get_username() == request.user.get_username():
                desserts_list.append(dessert)

    for post in full_post_list:
        for user in post.likes.all():
            if user.get_username() == request.user.get_username():
                posts_list.append(post)

    return render(request, 'menu/favourites.html',
                  {'coffee_list': coffee_list, 'tea_list': tea_list, 'desserts_list': desserts_list,
                   'posts_list': posts_list})
