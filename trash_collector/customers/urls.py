from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('details/', views.details, name='details'),
    path('edit', views.edit, name='edit'),
    path('suspend', views.suspend, name='suspend'),
    path('pickup', views.pickup, name='pickup')
]
