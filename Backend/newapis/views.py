from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from medical_record.models import DPI
from users.models import Utilisateur
from .serializers import DPIDetailSerializer, DpiCreateSerializer, QRCodeSerializer, UserSerializer, DPIListSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class DPIInfoView(generics.RetrieveAPIView):
    queryset = DPI.objects.all()
    serializer_class = DPIDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id_dpi'

class DPIListView(ListAPIView):
    queryset = DPI.objects.select_related('patient','patient__utilisateur').all()
    serializer_class = DPIListSerializer

class DPICreationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DpiCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        serializer.save()  
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QRCodeView(RetrieveAPIView):
    queryset = DPI.objects.all()
    serializer_class = QRCodeSerializer
    lookup_field = 'id_dpi'


