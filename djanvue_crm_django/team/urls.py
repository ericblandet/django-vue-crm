from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (TeamViewSet, UserDetail, add_member,
                    create_checkout_session, get_my_team, get_stripe_pub_key,
                    upgrade_plan, stripe_webhook, check_session, cancel_plan)

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/upgrade_plan/', upgrade_plan, name='upgrade_plan'),
    path('teams/add_member/', add_member, name='add_member'),
    path('teams/cancel_plan/', cancel_plan, name='cancel_plan'),
    path('stripe/get_stripe_pub_key/',
         get_stripe_pub_key, name='get_stripe_pub_key'),
    path('stripe/create_checkout_session/',
         create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook/',
         stripe_webhook, name='stripe_webhook'),
    path('stripe/check_session/',
         check_session, name='check_session'),


    path('', include(router.urls)),
]
