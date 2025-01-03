from django.urls import path
from .views import DPICreationView, DPIInfoView, QRCodeView, UserDetailView,LogoutView,DPIListView

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dpi/<int:id_dpi>/', DPIInfoView.as_view(), name='dpi'),
    path('dpis/', DPIListView.as_view(), name='dpi-list'),
    path('create/', DPICreationView.as_view(), name='create_dpi'),
    path('<int:id_dpi>/qrcode/', QRCodeView.as_view()),



    


]