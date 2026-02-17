from django.db import models
from django.utils.text import slugify

class Imovel(models.Model):
    # Usando tuplas para garantir a ordem e o par (valor, rótulo)
    FINALIDADE_CHOICES = [
        ("venda", "Venda"),
        ("compra", "Compra"),
        ("aluguel", "Aluguel"),
    ]
    
    TIPO_CHOICES = [
        ("apartamento", "Apartamento"),
        ("casa", "Casa"),
        ("kitnet", "KitNet"),
        ("salao", "Salão"),
    ]

    referencia = models.CharField(max_length=30)
    titulo = models.CharField(max_length=100)
    finalidade = models.CharField(max_length=30, choices=FINALIDADE_CHOICES)
    tipo_imovel = models.CharField(max_length=30, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.PositiveIntegerField()
    quartos = models.PositiveIntegerField()
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    publicado = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, max_length=150)
    
    foto_imovel = models.ImageField(upload_to="imoveis/fotos/%Y/%m/", blank=True, null=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True) # Atualiza a cada save

    def __str__(self):
        return f"{self.referencia} - {self.titulo}"

    # Gera o slug automaticamente antes de salvar
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)