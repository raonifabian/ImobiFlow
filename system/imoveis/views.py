import csv
import io
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django_weasyprint import WeasyTemplateResponseMixin
from .forms import ImportarCSVForm
from .models import Imovel

# View para a página inicial, mostrando uma visão geral dos imóveis disponíveis
class HomeView(TemplateView):
    template_name = 'imoveis/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Opcional: Mostrar apenas os 3 primeiros imóveis na home como destaque
        context['imoveis_destaque'] = Imovel.objects.all()[:3]
        return context

# View para listar todos os imóveis disponíveis, com paginação
class ImovelListView(ListView):
    model = Imovel
    template_name = 'imoveis/imovel_list.html'  # Especifica o template a ser usado
    context_object_name = 'imoveis'
    paginate_by = 15  # Paginação: 10 imóveis por página

# View para exibir detalhes de um imóvel específico
class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'imoveis/imovel_detail.html'
    context_object_name = 'imovel'

# View para gerar PDF da ficha do imóvel usando WeasyPrint
class ImovelPDFView(WeasyTemplateResponseMixin, ImovelDetailView):
    # Usa o mesmo contexto da DetailView, mas com um template otimizado para PDF
    template_name = 'imoveis/imovel_pdf.html'
    pdf_attachment = True  # Força o download do arquivo
    pdf_filename = 'ficha_imovel.pdf'

# View para importar imóveis via CSV, acessível apenas por superusuários (Admin)
class ImportarCSVView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'imoveis/importar_csv.html'
    form_class = ImportarCSVForm
    success_url = reverse_lazy('imovel_list') # Redireciona para o catálogo após sucesso

    # Regra de Segurança: Apenas superusuários (Admin) podem acessar essa view
    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        arquivo = form.cleaned_data['arquivo_csv']

        try:
            # Decodifica o arquivo da memória para texto
            decoded_file = arquivo.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)

            contador = 0
            for row in reader:
                Imovel.objects.update_or_create(
                    referencia=row['referencia'],
                    defaults={
                        'titulo': row['titulo'],
                        'finalidade': row['finalidade'].lower(),
                        'tipo_imovel': row['tipo_imovel'].lower(),
                        'valor': row['valor'],
                        'area': row['area'],
                        'quartos': row['quartos'],
                        'cidade': row['cidade'],
                        'bairro': row['bairro'],
                        'publicado': row['publicado'].lower() == 'true'
                    }
                )
                contador += 1
            
            # Mensagem de sucesso para o usuário
            messages.success(self.request, f'{contador} imóveis importados/atualizados com sucesso!')
        except Exception as e:
            messages.error(self.request, f'Erro ao processar o arquivo CSV. Verifique a formatação. Erro: {str(e)}')
            return self.form_invalid(form)

        return super().form_valid(form)