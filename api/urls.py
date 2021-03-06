from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views


urlpatterns = [
    path('', views.BranchList.as_view()),
    path('banks/', views.BankList.as_view()),
    path('client-manager/', views.ClientManagerList.as_view()),
    path('clients/', views.ClientList.as_view()),
    path('accounts/', views.AccountList.as_view()),
    path('transfer/', views.TransferList.as_view()),
    path('withdraw/', views.WithdrawList.as_view()),
    path('deposit/', views.DepositList.as_view()),
     ]
