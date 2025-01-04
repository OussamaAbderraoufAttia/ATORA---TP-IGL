from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from medical_record.models import BilanBiologique, Soin, Consultation,DPI
from users.models import Utilisateur
from .serializers import BilanBiologiqueSerializer, DPIDetailSerializer, DpiCreateSerializer, QRCodeSerializer, UserSerializer, DPIListSerializer,SoinSerializer, ConsultationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response



class SoinListView(generics.ListAPIView):
    serializer_class = SoinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        infirmier_id = self.kwargs['infirmier_id']
        return Soin.objects.filter(infirmier=infirmier_id)


'''
 send me this 
{
  "dpi": 1,
  "description_medecin": "Patient needs daily wound care.",
  "observation": "Wound is healing well."
}

i will respond with this 
{
  "id_soin": 1,
  "dpi": 1,
  "date_soin": "2023-10-01",
  "infirmier": 1,
  "description_medecin": "Patient needs daily wound care.",
  "observation": "Wound is healing well."
}
la ma 3jbattekch ma tkhdmch
'''
class SoinCreateView(generics.CreateAPIView):
    queryset = Soin.objects.all()
    serializer_class = SoinSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        infirmier = self.request.user.infirmier
        serializer.save(infirmier=infirmier)
'''
 send me this 
 {
  "description_medecin": "Patient needs daily wound care and medication.",
  "observation": "Wound is healing well, but redness observed."
}
i will respond with this
{
  "id_soin": 1,
  "dpi": 1,
  "date_soin": "2023-10-01",
  "infirmier": 1,
  "description_medecin": "Patient needs daily wound care and medication.",
  "observation": "Wound is healing well, but redness observed."
}

'''


class SoinUpdateView(generics.UpdateAPIView):
    queryset = Soin.objects.all()
    serializer_class = SoinSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        infirmier = self.request.user.infirmier
        serializer.save(infirmier=infirmier)

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


#####################################Consultation ++ Bilans############################################

'''
send me this
{
  "dpi": 2,
  "resume": {
    "symptoms": "Severe abdominal pain and nausea",
    "diagnosis": "Gastritis",
    "details": "Advised to avoid spicy food and take antacids."
  },
  "ordonnance": {
    "prescription": [
      {
        "dose": "20mg",
        "duree": "14 days",
        "medicament": {
          "nom": "Omeprazole",
          "description": "Proton pump inhibitor",
          "quantite": 28
        }
      },
      {
        "dose": "10mg",
        "duree": "10 days",
        "medicament": {
          "nom": "Metoclopramide",
          "description": "Antiemetic and gut motility stimulator",
          "quantite": 20
        }
      }
    ]
  },
  "bilan_biologique": {
    "description": "Normal blood count",
  },
  "bilan_radiologue": {
    "description": "No abnormalities detected",
  }
}

i will respond with this
{
    "dpi": 1,
    "resume": {
        "diagnostic": null,
        "symptomes": null,
        "details": null,
    },
    "ordonnance": {
        "date_prescription": "2025-01-04",
    },
    "bilan_biologique": null,
    "bilan_radiologue": null
}


'''
class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

class LaborantinBilanListView(generics.ListAPIView):
    serializer_class = BilanBiologiqueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BilanBiologique.objects.filter(status__in=[BilanBiologique.REQUESTED, BilanBiologique.DONE])


'''
send me this
{
  "mesures": [
    {
      "param": "Cholesterol",
      "valeur": "200 mg/dL"
    }
  ]
}

'''  
class LaborantinBilanUpdateView(generics.UpdateAPIView):
    queryset = BilanBiologique.objects.all()
    serializer_class = BilanBiologiqueSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(laborantin=self.request.user.laborantin, status=BilanBiologique.DONE)

class DoctorBilanListView(generics.ListAPIView):
    serializer_class = BilanBiologiqueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BilanBiologique.objects.filter(status=BilanBiologique.DONE)
    
class DoctorBilanValidateView(generics.UpdateAPIView):
    queryset = BilanBiologique.objects.all()
    serializer_class = BilanBiologiqueSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(status=BilanBiologique.VALIDATED)