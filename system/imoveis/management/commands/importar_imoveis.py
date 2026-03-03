from django.core.management.base import BaseCommand
from imoveis.models import Imovel
import csv

class Command(BaseCommand):
    help = 'Importa imóveis a partir de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file', 
            type=str, nargs='?', # Torna o argumento opcional 
            default='sistem/imoveis/data/planilhas/imoveis_inicial.csv', #caminho padrão do arquivo
            help='Caminho para o arquivo CSV a ser importado'
            )

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        #Tenta abrir o arquivo CSV e processar os dados, tratando possíveis erros como arquivo não encontrado ou colunas faltando
        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Usamos update_or_create para não duplicar imóveis se rodar o script 2x
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
            self.stdout.write(self.style.SUCCESS('Dados processados com sucesso!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Arquivo não encontrado.'))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'Coluna faltando no CSV: {e}'))