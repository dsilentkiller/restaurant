
from django.urls import path, include
from vendor import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'vendor'
urlpatterns = [


    path('list/', views.VendorListView.as_view(), name='list'),
    path('create/', views.VendorCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.VendorUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.VendorDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.VendorDeleteView.as_view(), name='delete'),
    path('search', views.SearchView, name='search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
