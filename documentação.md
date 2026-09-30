# Manual do Projeto Django

## 1. Visão geral

Este documento descreve, de forma sequencial, a configuração e a estrutura do projeto Django desenvolvido em ambiente Windows.

O projeto utiliza:

- Python
- Django 6.1.1
- Ambiente virtual (`venv`)
- PowerShell
- Visual Studio Code
- Banco de dados padrão do Django
- Uma aplicação chamada `core`

A aplicação possui como objetivo inicial implementar um blog simples, no qual os posts são cadastrados pelo painel administrativo do Django e posteriormente exibidos na página inicial.

---

# 2. Estrutura do projeto

O projeto está localizado em:

```text
C:\Users\Aluno\Desktop\rebecaMIvDjango
A estrutura esperada é:

rebecaMIvDjango/
│
├── venv/
│
├── meu_projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── manage.py
```
# 2.1. Função dos principais elementos
venv/

Contém o ambiente virtual do projeto.

O ambiente virtual mantém as dependências do projeto isoladas das demais instalações do Python no computador.

manage.py

É o arquivo de gerenciamento do projeto Django.

Por meio dele são executados comandos como:

python manage.py runserver
python manage.py check
python manage.py migrate
python manage.py createsuperuser
meu_projeto/

É o pacote de configuração principal do projeto.

Entre seus arquivos estão:

settings.py — configurações do Django.
urls.py — URLs principais.
asgi.py — configuração para servidores ASGI.
wsgi.py — configuração para servidores WSGI.
core/

É a aplicação Django responsável pela funcionalidade do blog.

Uma aplicação representa uma parte funcional do projeto.

templates/

Contém os arquivos HTML utilizados para apresentar as páginas ao usuário.

# 3. Ambiente virtual
## 3.1. Ativação

Antes de executar comandos relacionados ao projeto, o ambiente virtual deve estar ativo.

No PowerShell:

.\venv\Scripts\Activate.ps1

Quando a ativação é bem-sucedida, o terminal apresenta (venv) antes do caminho:

(venv) PS C:\Users\Aluno\Desktop\rebecaMIvDjango>

Isso indica que os comandos Python executados naquele terminal utilizarão o ambiente virtual.

# 4. Instalação do Django

Com o ambiente virtual ativado:

python -m pip install django

A instalação pode ser verificada com:

django-admin --version

Neste projeto, a versão utilizada é:

6.1.1
5. Aplicação core

A aplicação core concentra as funcionalidades do blog.

Ela contém os principais componentes da aplicação:

core/
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
└── templates/

Cada arquivo possui uma responsabilidade específica.

Arquivo	Responsabilidade
models.py	Define os dados da aplicação
views.py	Processa as requisições
urls.py	Define as rotas da aplicação
admin.py	Configura o painel administrativo
templates/	Contém as páginas HTML
6. Model: criando o Post

O modelo representa a estrutura dos dados que serão armazenados no banco de dados.

Arquivo:

core/models.py

Código:

from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
6.1. Classe Post
class Post(models.Model):

A classe Post representa uma publicação do blog.

Ela herda de:

models.Model

Essa herança faz com que a classe seja reconhecida pelo Django como um modelo de banco de dados.

6.2. Campo titulo
titulo = models.CharField(max_length=200)

Armazena o título do post.

CharField é utilizado para textos de tamanho limitado.

Neste caso, o limite é de 200 caracteres.

6.3. Campo conteudo
conteudo = models.TextField()

Armazena o conteúdo da publicação.

TextField é apropriado para textos maiores.

6.4. Campo data_criacao
data_criacao = models.DateTimeField(auto_now_add=True)

Armazena a data e a hora em que o registro foi criado.

O parâmetro:

auto_now_add=True

faz com que esse valor seja preenchido automaticamente na criação do objeto.

6.5. Método __str__
def __str__(self):
    return self.titulo

Define como o objeto será representado textualmente.

No painel administrativo, por exemplo, o Django poderá apresentar o título do post em vez de uma representação genérica do objeto.

7. Administração do modelo

Para que o modelo Post possa ser administrado pelo Django Admin, ele deve ser registrado.

Arquivo:

core/admin.py

Código:

from django.contrib import admin
from .models import Post

admin.site.register(Post)

O processo é:

models.py
    ↓
Post
    ↓
admin.py
    ↓
Django Admin

Depois do registro, o modelo poderá ser administrado pelo painel administrativo.

8. View da página inicial

A View é responsável por processar a requisição recebida e determinar qual resposta deve ser apresentada.

Arquivo:

core/views.py

Código:

from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-data_criacao')

    return render(request, 'core/home.html', {'posts': posts})
8.1. Importação do render
from django.shortcuts import render

render() é utilizado para combinar um template HTML com dados e produzir a resposta da página.

8.2. Importação do Post
from .models import Post

O ponto (.) indica que o módulo models pertence à aplicação atual.

O Post deve ser importado de models.py.

Não deve ser utilizado:

from django.http import Post

Essa importação causou anteriormente:

ImportError: cannot import name 'Post' from 'django.http'

O motivo é que Post é um modelo criado na aplicação, e não uma classe fornecida por django.http.

8.3. Função home
def home(request):

Define a View responsável pela página inicial.

O parâmetro request representa a requisição recebida pelo Django.

8.4. Consulta aos posts
posts = Post.objects.all().order_by('-data_criacao')

Post.objects.all() solicita todos os objetos Post.

O método:

.order_by('-data_criacao')

ordena os registros pela data de criação em ordem decrescente.

O sinal - indica a ordem decrescente.

Assim, os posts mais recentes aparecem primeiro.

8.5. Renderização do template
return render(request, 'core/home.html', {'posts': posts})

A View envia três informações principais:

A requisição (request);
O template que deve ser utilizado;
Os dados que serão disponibilizados ao template.

O dicionário:

{'posts': posts}

disponibiliza a consulta do banco para o HTML através da variável posts.

9. Sistema de URLs

O Django utiliza URLs para determinar qual View deve responder a cada endereço.

O projeto possui dois níveis de roteamento:

meu_projeto/urls.py
        ↓
core/urls.py
        ↓
views.py

Essa divisão permite manter as URLs principais separadas das URLs específicas da aplicação.

10. URLs principais do projeto

Arquivo:

meu_projeto/urls.py

Configuração:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
10.1. Rota do administrador
path('admin/', admin.site.urls)

Define o endereço:

/admin/

Esse endereço direciona para o painel administrativo do Django.

10.2. Inclusão das URLs da aplicação
path('', include('core.urls'))

Indica que as URLs da aplicação core serão utilizadas a partir da raiz do site.

Assim:

http://127.0.0.1:8000/

é encaminhado para core.urls.

11. URLs da aplicação

Arquivo:

core/urls.py

Código:

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

A rota:

path('', home, name='home')

associa o endereço vazio à função:

home

Portanto:

http://127.0.0.1:8000/

executa:

home(request)
12. Templates

Templates são arquivos responsáveis pela apresentação da interface.

A View procura o template:

core/home.html

Para que o Django encontre esse arquivo, a estrutura deve ser:

core/
└── templates/
    └── core/
        └── home.html

O caminho completo é:

core/templates/core/home.html

A segunda pasta core é utilizada para organizar os templates por aplicação e evitar conflitos entre arquivos com o mesmo nome.

13. Template home.html

Arquivo:

core/templates/core/home.html

Conteúdo:

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Meu Blog</title>
</head>

<body>

    <h1>Meu Blog</h1>

    {% for post in posts %}

        <article>
            <h2>{{ post.titulo }}</h2>

            <p>{{ post.conteudo }}</p>

            <small>
                Publicado em {{ post.data_criacao }}
            </small>
        </article>

        <hr>

    {% empty %}

        <p>Nenhum post publicado ainda.</p>

    {% endfor %}

</body>

</html>
14. Template Language do Django

O Django possui uma linguagem própria para inserir dados e lógica simples dentro dos templates.

14.1. Exibir uma variável

A sintaxe:

{{ post.titulo }}

exibe o valor do atributo titulo.

Da mesma forma:

{{ post.conteudo }}

exibe o conteúdo do post.

E:

{{ post.data_criacao }}

exibe a data de criação.

14.2. Percorrer os posts

O trecho:

{% for post in posts %}

inicia um loop que percorre os objetos enviados pela View.

O loop é encerrado por:

{% endfor %}
14.3. Quando não existem posts

O bloco:

{% empty %}
    <p>Nenhum post publicado ainda.</p>

é executado quando a variável posts não contém registros.

15. Fluxo completo da aplicação

Quando o usuário acessa:

http://127.0.0.1:8000/

ocorre a seguinte sequência:

1. Navegador
       ↓
2. meu_projeto/urls.py
       ↓
3. core/urls.py
       ↓
4. views.py
       ↓
5. Post.objects.all()
       ↓
6. Banco de dados
       ↓
7. View recebe os posts
       ↓
8. home.html recebe os dados
       ↓
9. Django gera o HTML
       ↓
10. Navegador apresenta a página

Esse fluxo representa a interação básica entre URL, View, Model, banco de dados e Template.

16. Verificação do projeto

O Django possui um mecanismo para verificar problemas de configuração.

O comando utilizado é:

python manage.py check

O projeto passou pela verificação, apresentando apenas o seguinte aviso:

(urls.W005) URL namespace 'admin' isn't unique.

Esse aviso indica que o namespace admin está sendo registrado mais de uma vez.

Ele não impediu o servidor de desenvolvimento de iniciar, mas deve ser corrigido antes de considerar a configuração concluída.

17. Executar o servidor

Para iniciar o servidor de desenvolvimento:

python manage.py runserver

Quando iniciado corretamente, o terminal apresenta um endereço semelhante a:

Starting WSGI development server at http://127.0.0.1:8000/

A aplicação pode então ser acessada pelo navegador:

http://127.0.0.1:8000/

O servidor pode ser encerrado no PowerShell com:

CTRL + C
18. Erros encontrados e correções
18.1. Importação incorreta de Post
Erro
from django.http import Post
Problema

Post foi criado pelo próprio projeto em core.models, portanto não pertence a django.http.

Correção
from .models import Post
18.2. Template inexistente
Erro
django.template.exceptions.TemplateDoesNotExist: core/home.html
Problema

A View procurava:

core/home.html

mas o arquivo não estava disponível na estrutura de templates esperada.

Estrutura correta
core/
└── templates/
    └── core/
        └── home.html
18.3. Aviso de namespace do Admin
Aviso
(urls.W005) URL namespace 'admin' isn't unique.
Situação

O servidor continua funcionando, porém existe uma duplicação na configuração das URLs do administrador.

Esse problema deve ser investigado no arquivo:

meu_projeto/urls.py

e em qualquer outro arquivo que esteja incluindo ou registrando novamente as URLs administrativas.

19. Comandos principais utilizados
Comando	Função
.\venv\Scripts\Activate.ps1	Ativa o ambiente virtual
python -m pip install django	Instala o Django
django-admin --version	Exibe a versão do Django
python manage.py check	Verifica problemas de configuração
python manage.py runserver	Inicia o servidor de desenvolvimento
python manage.py migrate	Aplica migrações ao banco
python manage.py createsuperuser	Cria usuário administrador
20. Próximas etapas

A implementação ainda não está concluída. A sequência recomendada é:

Confirmar o funcionamento do home.html.
Corrigir o aviso de namespace duplicado do admin.
Executar as migrações:
python manage.py migrate
Criar o usuário administrador:
python manage.py createsuperuser
Iniciar o servidor:
python manage.py runserver
Acessar:
http://127.0.0.1:8000/admin/
Criar um Post pelo painel administrativo.
Acessar:
http://127.0.0.1:8000/
Verificar se o post cadastrado aparece na página inicial.
21. Arquitetura atual

A arquitetura básica implementada pode ser resumida da seguinte forma:

                    DJANGO
                       │
        ┌──────────────┼──────────────┐
        │              │              │
       URL            View           Model
        │              │              │
        │              │              │
        └──────→      Dados     ←──────┘
                       │
                       ▼
                   Template
                       │
                       ▼
                   Navegador

Cada camada possui uma responsabilidade:

URL: identifica qual recurso foi solicitado.
View: processa a requisição.
Model: representa e consulta os dados.
Template: apresenta os dados.
Banco de dados: armazena as informações.
Admin: fornece uma interface para administrar os modelos.

A separação dessas responsabilidades é uma das bases da organização de aplicações Django.