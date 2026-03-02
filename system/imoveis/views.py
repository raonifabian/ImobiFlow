from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django_weasyprint import WeasyTemplateResponseMixin
from .models import Imovel

class HomeView(TemplateView):
    template_name = 'imoveis/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Opcional: Mostrar apenas os 3 primeiros imóveis na home como destaque
        context['imoveis_destaque'] = Imovel.objects.all()[:3]
        return context

class ImovelListView(ListView):
    model = Imovel
    template_name = 'imoveis/imovel_list.html'  # Especifica o template a ser usado
    context_object_name = 'imoveis'
    paginate_by = 10  # Paginação: 10 imóveis por página

class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'imoveis/imovel_detail.html'
    context_object_name = 'imovel'

class ImovelPDFView(WeasyTemplateResponseMixin, ImovelDetailView):
    # Usa o mesmo contexto da DetailView, mas com um template otimizado para PDF
    template_name = 'imoveis/imovel_pdf.html'
    pdf_attachment = True  # Força o download do arquivo
    pdf_filename = 'ficha_imovel.pdf'