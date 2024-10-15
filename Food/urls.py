from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    path("", views.ping, name="ping"),
    path("index/", views.HomeView.as_view(), name="index"),
    path("<int:item_id>/", views.detail_view, name="detail_view"),
    path("add/", views.add_item, name="add_item"),
    path("update/<int:item_id>/", views.update_item, name="update_item"),
    path("delete/<int:item_id>/", views.delete_item, name="delete_item"),
]
