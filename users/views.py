from rest_framework import status, generics, serializers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from .serializers import UserSerializer, TrainingSerializer, UserTrainingSerializer
from .models import Training, UserTraining

User = get_user_model()

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        if data['password'] != data['confirm_password']:
            return Response({"error": "Password dan Confirm Password tidak sama"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                password=data['password'],
                fullname=serializer.validated_data['fullname'],
                phone_number=serializer.validated_data.get('phone_number', ''),
                role=serializer.validated_data['role']
            )
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Credentials tidak valid"}, status=status.HTTP_401_UNAUTHORIZED)

class TrainingListView(generics.ListAPIView):
    serializer_class = TrainingSerializer

    def get_queryset(self):
        queryset = Training.objects.all()
        category_name = self.request.query_params.get('category', None)
        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)
        return queryset

        
class UserTrainingListView(generics.ListAPIView):
    serializer_class = UserTrainingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserTraining.objects.filter(user=self.request.user)

