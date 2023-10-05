from django.urls import path
from product.views import *
from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='admin_dashboard'),
    path('orders/', ManageOrdersView.as_view(), name='manage_order'), 
    path('orders/<int:order_id>/', EditOrderView.as_view(), name='edit_order'), 
    path('inventory/', ManageInventoryView.as_view(), name='manage_inventory'),
    path('inventory/new', AddEditInventoryView.as_view(), name='add_inventory'), 
    # path('inventory/<int:inventory_id>', AddEditInventoryView.as_view(), name='edit_inventory'),
    path('setting/', SettingView.as_view(), name='settting'),
    path('products/', ManageProductView.as_view(), name='manage_product'),
    path('products/add', AddEditProductView.as_view(), name='add_product'),
    path('products/edit/<int:product_id>', AddEditProductView.as_view(), name='edit_product'),
    path('category/', ManageCategoryView.as_view(), name='manage_category'),
    path('bannerimage/', ManageBannerImageView.as_view(), name='manage_banner_images'), 
    path('bannerimage/new', AddEditBannerImages.as_view(), name='add_banner_images'), 
    path('bannerimage/<int:banner_id>', AddEditBannerImages.as_view(), name='edit_banner_images'), 
    path('category/new', AddEditCategoryView.as_view(), name='add_category'),
    path('category/<int:category_id>', AddEditCategoryView.as_view(), name='edit_category'),

    # path('', AdminHomePage, name='AdminHomePage'),
    # path('product/', ManageProductPage, name='ManageProductPage'),
    # path('product/new', AddProductPage, name='AddProductPage'),
    # path('product/<int:id>', EditProduct, name='EditProduct'),
    # path('featureproduct/', ManageFeatureProductPage, name='ManageFeatureProductPage'), 
    # path('featureproduct/new', AddFeatureProductPage, name='AddFeatureProductPage'), 
    # path('featureproduct/<int:id>', EditFeatureProduct, name='EditFeatureProduct'),

    # path('orders/', ManageOrdersPage, name='ManageOrdersPage'), 
    # path('orders/<int:id>', EditOrders, name='EditOrders')

]