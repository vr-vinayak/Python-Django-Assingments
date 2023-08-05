from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product_checks')

app_name = 'product'

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user-login/', LoginViews.as_view(), name='user-login'),
]
