from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('zip_code', views.zip_code, name="zip_code"),
    path('my_view', views.my_view, name="my_view"),
    path('confirm/<int:customer_id>', views.confirm, name="confirm"),
    path('un_confirm/<int:customer_id>', views.un_confirm, name="un_confirm")
]
