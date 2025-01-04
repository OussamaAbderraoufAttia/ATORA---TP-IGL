from django.urls import path
from .views import ConsultationCreateView, DPICreationView, DPIInfoView, DoctorBilanListView, DoctorBilanValidateView, LaborantinBilanListView, LaborantinBilanUpdateView, QRCodeView, SoinCreateView, SoinListView, SoinUpdateView, UserDetailView,LogoutView,DPIListView

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dpi/<int:id_dpi>/', DPIInfoView.as_view(), name='dpi'),
    path('dpis/', DPIListView.as_view(), name='dpi-list'),
    path('create/', DPICreationView.as_view(), name='create_dpi'),
    path('<int:id_dpi>/qrcode/', QRCodeView.as_view()),
    path('soins/infirmier/<int:infirmier_id>/', SoinListView.as_view(), name='soin-list'),
    path('consultations/add/', ConsultationCreateView.as_view(), name='consultation-add'),
    path('doctor/consultations/', ConsultationCreateView.as_view(), name='consultation-create'),
    path('laborantin/bilans/', LaborantinBilanListView.as_view(), name='laborantin-bilan-list'),
    path('laborantin/bilans/<int:pk>/', LaborantinBilanUpdateView.as_view(), name='laborantin-bilan-update'),
    path('doctor/bilans/', DoctorBilanListView.as_view(), name='doctor-bilan-list'),
    path('doctor/bilans/<int:pk>/validate/', DoctorBilanValidateView.as_view(), name='doctor-bilan-validate'),
    path('soins/create/', SoinCreateView.as_view(), name='soin-create'),
    path('soins/update/<int:pk>/', SoinUpdateView.as_view(), name='soin-update'),



    


]