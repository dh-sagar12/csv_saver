from django.urls import path

from home.views import AllCategoriesView
from . import views



urlpatterns = [
    path('category/', AllCategoriesView.as_view(), name='all_category'),
    path('', views.ListProductView.as_view(), name='list_product'),
    path('receipt/<str:order_uuid>', views.PrintReceipt, name='print_receipt'),
    path('<str:slug>/', views.ViewProductPage.as_view(), name='view_product'),
    path('category/<str:category_url>/', views.CategoryProductView.as_view(), name='category_products'),
    path('checkout/<str:slug>/', views.CheckoutView.as_view(), name='checkout_page'),


]