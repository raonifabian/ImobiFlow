from django.urls import path
from .views import HomeView, ImovelListView, ImovelDetailView, ImovelPDFView, ImportarCSVView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalogo/', ImovelListView.as_view(), name='imovel_list'),
    path('<int:pk>/', ImovelDetailView.as_view(), name='imovel_detail'),
    path('<int:pk>/pdf/', ImovelPDFView.as_view(), name='imovel_pdf'),
    path('importar/', ImportarCSVView.as_view(), name='importar_csv'),
]