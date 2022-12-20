from django.urls import path
from Recharge_app.views import (Home,PlanView,SelectPlan, RechargeView,RechargeCheck)

urlpatterns = [
    path('',Home.as_view(),name='Home'),
    path('plans/',PlanView.as_view(),name='Plans'),
    path('selectplan',SelectPlan.as_view(),name='SelectPlan'),
    path('recharge/',RechargeView.as_view(),name='Recharge'),
    path('check/',RechargeCheck.as_view(),name='RechargeCheck')
]

