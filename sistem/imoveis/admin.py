from django.contrib import admin
from .models import Imovel

# Register your models here.

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na lista de imóveis
    list_display = ('referencia', 'titulo', 'tipo_imovel', 'finalidade', 'valor', 'publicado', 'criado_em')
    
    # Filtros laterais para facilitar a busca
    list_filter = ('finalidade', 'tipo_imovel', 'publicado', 'cidade')
    
    # Campos que permitem busca por texto
    search_fields = ('referencia', 'titulo', 'bairro', 'cidade')
    
    # Preenche o slug automaticamente enquanto você digita o título no Admin
    prepopulated_fields = {'slug': ('titulo',)}
    
    # Organiza os campos em seções dentro do formulário de edição
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('referencia', 'titulo', 'slug', 'publicado')
        }),
        ('Detalhes do Imóvel', {
            'fields': ('tipo_imovel', 'finalidade', 'valor', 'area', 'quartos')
        }),
        ('Localização', {
            'fields': ('cidade', 'bairro')
        }),
        ('Mídia', {
            'fields': ('foto_imovel',)
        }),
    )
    
    # Define campos de leitura (não editáveis pelo Admin)
    readonly_fields = ('criado_em', 'editado_em')