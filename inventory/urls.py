from django.shortcuts import render
from inventory import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'inventory'
urlpatterns = [
    # inventory
    path('list/', views.InventoryItemListView.as_view(), name='list'),
    path('create/', views.InventoryItemCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.InventoryItemUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.InventoryItemDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.InventoryItemDeleteView.as_view(), name='delete'),
    path('search', views.SearchView, name='search'),
    # path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

    # purchasebill
    path('purchase-list/', views.PurchaseItemListView.as_view(),
         name='purchase-list'),
    path('purchase-create/', views.PurchaseItemCreateView.as_view(),
         name='purchase-create'),
    path('purchase-update/<int:pk>',
         views.PurchaseItemUpdateView.as_view(), name='purchase-update'),
    path('purchase-detail/<int:pk>',
         views.PurchaseItemDetailView.as_view(), name='purchase-detail'),
    path('purchase-delete/<int:pk>',
         views.PurchaseItemDeleteView.as_view(), name='purchase-delete'),

    path('search', views.SearchView, name='search'),

    # kitchen bill
    path('kitchen-bill-list/', views.KitchenItemListView.as_view(),
         name='kitchen-bill-list'),
    path('kitchen-bill-create/', views.KitchenItemCreateView.as_view(),
         name='kitchen-bill-create'),
    path('kitchen-bill-update/<int:pk>',
         views.KitchenItemUpdateView.as_view(), name='kitchen-bill-update'),
    path('kitchen-bill-detail/<int:pk>',
         views.KitchenItemDetailView.as_view(), name='kitchen-bill-detail'),
    path('kitchen-bill-delete/<int:pk>',
         views.KitchenItemDeleteView.as_view(), name='kitchen-bill-delete'),
    path('inventory-dashboard', views.inventory_dashboard,
         name='inventory-dashboard'),
    path('calculate_total_sales', views.calculate_total_sales,
         name='calculate_total_sales'),

    path('inventory_sales_report', views.inventory_sales_report,
         name='inventory_sales_report'),

    path('search', views.SearchView, name='search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
