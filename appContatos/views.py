from django.shortcuts import render, get_object_or_404
# ↓ Importar o modulo ↓ DbTabContatos
from .models import DbTabContatos
# O . ↑ É um detalhe importante
# ↓ Importando o erro 404 ↓
# from django.http import Http404, response
# ↓ Para fazer a paginação do django ↓↘
from django.core.paginator import Paginator

# Create your views here.

# Vou copiar e preservar esse método para ver como era antes
# def index(request):
#   Aqui não é ponto (.) é barra ( / )
#   -------------------------------- ↓ -----------------
#   return render(request, 'appContatos/contatoIndex.html')
# Pasta Templates past appContatos ↑   e     ↑ arquivo.html da past appContatos


# Este metodo foi copiado para ser alterado com um dicionário {}
def index(request):
    # Esta ↓ variável irá ser passada como chave do dicionário
    varHtmlContatos = DbTabContatos.objects.all()
    # Utilizando o ↓ Paginator
    paginacao = Paginator(varHtmlContatos, 10)
    page = request.GET.get('p')
    varHtmlContatos = paginacao.get_page(page)
    return render(request, 'appContatos/contatoIndex.html', {
        # Aqui ↓ a chave do dicionário
        'passaHtmlContatos': varHtmlContatos, 
        # Aqui  recebe a variável acima ↑
    })


# Aqui colocar a TAG HTML ↓ do path '<int:contato_id>'
def verContato(request, contato_id):
    # Esta ↓ variável irá ser passada como chave do dicionário
    # varHtmlContatoUnico = DbTabContatos.objects.get(id=contato_id)
    # ----------------------- Trocar all por get ↑ e utilizar ↖ o contato_id
    # Substituição para o tratamento ↓ do erro 404 ↓
    varHtmlContatoUnico = get_object_or_404(DbTabContatos, id=contato_id)
    return render(request, 'appContatos/verContato.html', {
        # ------------------ Criar o arquivo ↑ verContato.html
        # Aqui ↓ a chave do dicionário
        'passaHtmlContato': varHtmlContatoUnico
        # Aqui  recebe a variável acima ↑
    }
    )
