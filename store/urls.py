from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/profile/', views.profile, name='profile'),
    # path('accounts/signup/', views.account_signup, name='signup'),
    # path('accounts/login/', views.account_login, name='login'),
    # path('accounts/logout/', views.logout, name='logout'),
    # path('accounts/password_reset/', views.password_reset, name='password_reset'),
    # path('accounts/password_reset/done/', views.password_reset_done, name='password_reset_done'),
    
    path("store/", StoreAPIView.as_view(), name="store"),
    path("cart/", CartAPIView.as_view(), name="cart"),
    path("checkout/", CheckoutAPIView.as_view(), name="checkout"),
    path("update_item/", UpdateItemAPIView.as_view(), name="update_item"),
    path("process_order/", ProcessOrderAPIView.as_view(), name="process_order"),
    path("order_history/", OrderHistoryAPIView.as_view(), name="order_history"),

]
