
from django.urls import path, include
from menus import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'menus'
urlpatterns = [

    path('', views.Base, name='home'),
    path('list/', views.MenuItemListView.as_view(), name='list'),
    path('create/', views.MenuItemCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.MenuItemUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.MenuItemDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.MenuItemDeleteView.as_view(), name='delete'),
    path('search', views.SearchView, name='search'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
