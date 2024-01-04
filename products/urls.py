from django.urls import path
from . import views

urlpatterns = [
    # Products URLs
    path('products/', views.all_products, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),

    # Static Pages URLs
    path('help/', views.help, name='help'),
    path('swimming/', views.swimming, name='swimming'),
    path('function/', views.function, name='function'),
    path('pilates/', views.pilates, name='pilates'),

    # Blog URLs
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
