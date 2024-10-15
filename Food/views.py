from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .forms import itemForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

# Create your views here.


def ping(request):
    return HttpResponse("pong")


# def home(request):
#     query_set = Item.objects.all()
#     context = {"items": query_set}
#     return render(request, "food/index.html", context)


class HomeView(ListView):
    model = Item  # This is the model that the view will be working with
    template_name = "food/index.html"
    context_object_name = "items"

    # def get_queryset(self):
    #     # Return a custom queryset
    #     return Item.objects.all()


def detail_view(request, Item_id):
    query_set = Item.objects.get(pk=Item_id)
    context = {"Item": query_set}
    return render(request, "food/detail_view.html", context)


def add_item(request):
    if request.method == "POST":
        form = itemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("food:index")

    else:
        form = itemForm()
    return render(request, "Food/create_Item.html", {"form": form})


def update_item(request, Item_id):
    instance = Item.objects.get(pk=Item_id)
    form = itemForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "Food/create_Item.html", {"form": form, "Item": instance})


def delete_item(request, Item_id):
    instance = get_object_or_404(Item, pk=Item_id)
    if request.method == "POST":
        instance.delete()
        return redirect("food:index")
    return render(request, "Food/delete_Item.html", {"Item": instance})
