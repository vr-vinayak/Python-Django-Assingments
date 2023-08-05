from .models import Product, User
from rest_framework import status
from .paginator import CustomPagination
from rest_framework.views import APIView
from .serializers import ProductSerializer, LoginSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

# from rest_framework_jwt.views import ObtainJSONWebToken
# from rest_framework_jwt.serializers import JSONWebTokenSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }   

class LoginViews(APIView):
    def post(self, request, format=None):
        """Login with email and password payload."""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email').lower()
            password = serializer.data.get('password')
            user_obj = User.objects.filter(email=email).first()
            if user_obj:
                user_serializer = UserLoginSerializer(instance=user_obj, context={'request': request})
                user = authenticate(
                    email=user_obj.email.lower(), password=password)
                if user is not None:
                    user_id = user.id
                    token = get_tokens_for_user(user)
                    return Response(data={"token": token, "id": user_id, "user": user_serializer.data, 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
                else:
                    return Response(data={"user": user_serializer.errors, 'status': status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(data={'message': 'User with this email does not exists.', 'status':status.HTTP_403_FORBIDDEN}, status=status.HTTP_403_FORBIDDEN)

# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='add-product')
    def add_product(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': 'success','data': serializer.data, 'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'failure','data': serializer.errors, 'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['put'], url_path='update-product')
    def update_product(self, request, pk=None):
        product_obj=self.get_object()
        serializer = ProductSerializer(product_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': 'success','data': serializer.data, 'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'failure','data': serializer.errors, 'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'], url_path='delete-product')
    def delete_product(self, request, pk=None):
        product_obj = self.get_object()
        product_obj.delete()
        return Response(data={'message': f'product deleted successfully {product_obj}', 'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)