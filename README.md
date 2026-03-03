# 🏢 ImobiFlow

```{=html}
<p align="center">
```
`<b>`{=html}Sistema de Gestão e Catalogação de
Imóveis`</b>`{=html}`<br>`{=html} Aplicação web moderna para
administração, vitrine e geração de documentação imobiliária.
```{=html}
</p>
```

------------------------------------------------------------------------

## 🚀 Sobre o Projeto

O **ImobiFlow** é uma aplicação web desenvolvida em **Django** para
facilitar a administração, catalogação e exibição de imóveis.

O sistema atende tanto à:

-   🌐 **Exibição pública** (vitrine e catálogo)
-   🏢 **Gestão interna** (importação de dados e geração de documentos)

Projetado com foco em organização, performance e apresentação visual
premium.

------------------------------------------------------------------------

## 🖼️ Funcionalidades (V1)

✔ **Vitrine Digital (Landing Page)**\
Página inicial moderna com destaques e chamadas para ação.

✔ **Catálogo de Imóveis**\
Listagem completa com paginação e layout em cards responsivos.

✔ **Ficha Detalhada + Exportação em PDF**\
Geração automática de ficha técnica em PDF (via WeasyPrint), pronta para
envio ao cliente ou impressão.

✔ **Importação de Dados em Massa (CSV)**\
- Via interface web (acesso restrito a administradores) - Via comando
customizado no Django (CLI)

✔ **Painel Administrativo Completo**\
Gestão avançada via Django Admin com filtros e busca.

✔ **Design Premium e Responsivo**\
- Estilização customizada\
- Efeitos de glassmorphism\
- Animações suaves com Animate.css

------------------------------------------------------------------------

## 🛠️ Stack Tecnológica

### 🔙 Backend

-   Python 3.12
-   Django 5.0+
-   PostgreSQL 16
-   Pandas
-   Openpyxl

### 📄 Documentos

-   WeasyPrint
-   django-weasyprint

### 🖼️ Imagens

-   Pillow

### 🎨 Frontend

-   HTML5
-   CSS3 customizado
-   Bootstrap 5
-   Animate.css

### 🐳 Infraestrutura

-   Docker
-   Dev Containers (VS Code)

------------------------------------------------------------------------

## ⚙️ Como Executar o Projeto

O projeto foi configurado para rodar de forma padronizada usando **Dev
Containers + Docker**.

------------------------------------------------------------------------

### ✅ Pré-requisitos

-   Docker instalado e em execução
-   Visual Studio Code
-   Extensão Dev Containers

------------------------------------------------------------------------

### 📥 1. Clone o Repositório

``` bash
git clone https://github.com/seu-usuario/imobiflow.git
cd imobiflow
```

------------------------------------------------------------------------

### 💻 2. Abra no VS Code

``` bash
code .
```

------------------------------------------------------------------------

### 🐳 3. Reabra no Dev Container

O VS Code detectará a pasta `.devcontainer` e perguntará se deseja abrir
no container.

Clique em:

Reopen in Container

O Docker irá: - Construir a imagem - Subir o PostgreSQL - Instalar
dependências automaticamente

------------------------------------------------------------------------

### 🗄️ 4. Aplicar Migrações

``` bash
python system/manage.py makemigrations
python system/manage.py migrate
```

------------------------------------------------------------------------

### 👤 5. Criar Superusuário

``` bash
python system/manage.py createsuperuser
```

------------------------------------------------------------------------

### ▶ 6. Rodar o Servidor

``` bash
python system/manage.py runserver
```

Acesse:

http://localhost:8000

------------------------------------------------------------------------

## 📂 Importação de Dados (CSV)

O sistema permite popular o banco rapidamente com arquivos CSV.

### 🔹 Opção 1 --- Interface Web (Recomendado)

1.  Faça login como administrador\
2.  Clique em Importar CSV\
3.  Envie seu arquivo

### 🔹 Opção 2 --- Terminal

``` bash
python system/manage.py importar_imoveis
```

Para arquivo específico:

``` bash
python system/manage.py importar_imoveis caminho/do/arquivo.csv
```

------------------------------------------------------------------------

## 📌 Roadmap Futuro

-   [ ] Sistema de autenticação para corretores
-   [ ] Dashboard analítico
-   [ ] Upload múltiplo de imagens
-   [ ] API REST
-   [ ] Deploy automatizado

------------------------------------------------------------------------

## 📄 Licença

Este projeto está sob a licença **MIT**.\
Consulte o arquivo `LICENSE` para mais informações.

------------------------------------------------------------------------

## 👨‍💻 Autor

Desenvolvido por Raoni\
Projeto de portfólio / sistema real de gestão imobiliária.
