
from django.urls import path, include
from order import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'order'

urlpatterns = [
    path('list/', views.OrderListView.as_view(), name='list'),
    path('create/', views.OrderCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.OrderUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.OrderDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.OrderDeleteView.as_view(), name='delete'),
    path('search', views.SearchView, name='search'),
    path('submit_form/', views.handle_form_submission, name='submit_form'),
    # path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
