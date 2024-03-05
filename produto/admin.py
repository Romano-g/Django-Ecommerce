from django.contrib import admin
from produto.models import Produto, Variacao


class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 2


class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'descricao_curta', 'get_preco_formatado',
        'get_preco_formatado_promo',
    )
    inlines = [
        VariacaoInLine
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
