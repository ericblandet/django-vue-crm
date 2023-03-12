from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, get_my_team, add_member, UserDetail, upgrade_plan, get_stripe_pub_key

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/upgrade_plan/', upgrade_plan, name='upgrade_plan'),
    path('teams/add_member/', add_member, name='add_member'),
    path('stripe/get_stripe_pub_key/',
         get_stripe_pub_key, name='get_stripe_pub_key'),
    path('', include(router.urls)),
]
