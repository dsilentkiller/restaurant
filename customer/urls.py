from django.shortcuts import render
from customer import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'customer'
urlpatterns = [


    path('list/', views.CustomerListView.as_view(), name='list'),
    path('create/', views.CustomerCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.CustomerUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.CustomerDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.CustomerDeleteView.as_view(), name='delete'),
    path('search', views.SearchView, name='search'),
    # path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
