from django.urls import path
# IMPORT DAS VIEWS
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
path('',views.index, name="principal"),
#path('formulario/',views.formulario, name="formulario"),  # IMPLEMENTAÇÃO ANTIGA
path('perfil/',views.perfil, name="perfil"),
path('postados/',views.postados, name="postados"),
path('editar/<int:id>',views.editar, name="editar"),
path('deleta/<int:id>',views.deleta, name="deleta"),
path('videos/',views.videos, name="videos"),
path('mostravideos/', views.mostravideos, name="mostravideos"),
path('deletavideo/<int:id>',views.deletavideo, name="deletavideo"),
path('videospublicados/',views.videospublicados, name="videospublicados"),
path('criarperfil/',views.criarperfil, name="criarperfil"),
path('postdetalhes/<int:id>',views.postdetalhes, name="postdetalhes"),
path('editaperfil/<int:id>',views.editaperfil, name="editaperfil"),
#path('like_post/<int:pk>', LikeView,name="like_post"),
path('termos/', views.termos, name='termos'),
path('postados/<int:id>/addcomentario/', views.comentando, name='addcomentario'),
path('tutorial/', views.tutorial,name="tutorial"),
path('verpostagens/',views.verpostagens,name="verpostagens"),
path('todosvideos/',views.todosvideos,name="todosvideos"),
path('indicacao/',views.indicacao,name="indicacao"),
path('destaque/',views.destaque,name="destaque"),
path('detalhesVideos/<int:id>',views.detalhesVideos, name='detalhesVideos'),
path('formulariocomentario/',views.formulariocomentario, name='formulariocomentario'),
path('comentados/',views.comentados,name='comentados'),
path('momentos/', views.momentos, name='momentos'),
path('verstories/',views.verstories, name='verstories'),
path('detalhestories/<int:id>', views.detalhestories, name='detalhestories'),
path('criaranuncio/', views.criaranuncio, name='criaranuncio'),
path('produtos/', views.produtos, name='produtos'),
path('meustories/', views.meustories, name='meustories'),
path('deletastories/<int:id>', views.deletastories,name='deletastories'),
path('postcomentados/',views.postcomentados,name='postcomentados'),
path('detalheproduto/<int:id>',views.detalheproduto, name='detalheproduto'),
path('meusProdutos/',views.meusProdutos, name='meusProdutos'),
path('deletaproduto/<int:id>', views.deletaproduto,name='deletaproduto'),
path('deletacomentarios/<int:id>',views.deletacomentarios,name='deletacomentarios'),
path('termosloja/',views.termosloja,name='termosloja'),
path('son-house/',views.artigo,name='son-house'),
path('loja/',views.MinhaLoja,name="loja"),
path('detalhe-produto/<int:id>',views.ProdutoDetalhe,name="detalhe-produto"),
path('SalaForAll/',views.Sala,name="SalaForAll"),
path('paginas/<str:room_name>/',views.room, name='room'),
path('dicas/',views.Dica,name="dicas"), # CONTEÚDO
path('breve-historia/',views.BreveHistoria,name="breve-historia"), # CONTEÚDO
path('Primeira-resenha/', views.Primeiraresenha, name="Primeira-resenha"), # CONTEÚDO
path('Segunda-resenha/', views.Segundaresenha, name="Segunda-resenha"), # CONTEÚDO
path('Terceira-resenha/', views.Terceiraresenha, name="Terceira-resenha"), # CONTEÚDO
path('Quarta-resenha/', views.Quartaresenha, name="Quarta-resenha"), # CONTEÚDO
path('Quinta-resenha/', views.Quintaresenha, name="Quinta-resenha"), # CONTEÚDO
path('meusposts/',views.Meuposts,name="meusposts"), # CONTEÚDO
path('pensamento/<int:id>',views.ExcluiPensamento,name="pensamento"),
path('postaDetalhe/<int:id>',views.DetalhePost,name="postaDetalhe"), # DETALHE DO POST
path('detalhar-post/<int:id>',views.DetalharPost,name="detalhar-post"),
path('spotify/', views.PlayList,name="spotify"),
path('deletePlay/<int:id>', views.DeletePlay,name='deletePlay'),
#path('Like/<int:id>',views.Like, name='Like'),
#path('DisLike/<int:id>',views.Dislike, name='DisLike'),
path('user',views.Usuarios,name="user"),
path('redacao',views.Redacao, name="redacao"), # CONTEÚDO
path('lojapremium',views.Premium,name="lojapremium"),
path('inscricaopremium',views.InscricaoPremium,name='inscricaopremium'),
path('cancelapremium/<int:id>', views.CancelaPremium,name='cancelapremium'),
path('inscritospremium',views.InscritosPremium,name="inscritospremium"),
path('produtopremium/',views.ProdutoPremium,name="produtopremium"),
path('detalheprodutopremium/<int:id>',views.DetalhePremium, name="detalheprodutopremium"),
path('produtospremius/',views.ProdutosPremiums,name="produtospremius"),
path('detalharprodutopremium/<int:id>',views.DetalhesPremium,name="detalharprodutopremium"),
path('anuncios_usuarios_premium/', views.DetalhesPremiumUsuario,name="anuncios_usuarios_premium"),
path('editar_anuncio_premium/<int:id>',views.EditarAnuncioPremium,name="editar_anuncio_premium"),
path('Deleta_anuncio_premium/<int:id>',views.DeletaAnuncioPremium, name="Deleta_anuncio_premium"),
path('Redacao_reportagem/',views.RedacaoReportagem, name="Redacao_reportagem"), # CONTEÚDO
path('Parceiros/',views.Meus_Parceiros,name="Parceiros"), # SEM ESTÁ LOGADO
path('Espaco_parceiro/<int:id>',views.EspacoParceiro,name="Espaco_parceiro"), # SEM ESTA LOGADO - DETALHES
path('ParceiroLogado/',views.ParceirosLogado,name="ParceiroLogado"),
path('Parceiro-logado-detalhe/<int:id>',views.ParceiroLogadoDetalhe,name="Parceiro-logado-detalhe"),
path('Bob_Mould/',views.BobMould,name="Bob_Mould"), # CONTEÚDO
path('Artistas-brasileiros/',views.ArtistasBrasileiros, name="Artistas-brasileiros"), # CONTEÚDO
path('banda-irlandesa/',views.bandaIrlanda, name="banda-irlandesa"), # CONTEÚDO
path('MinhasMensagens/',views.MinhaMensagem, name="MinhasMensagens"),
path('DeletaMinhasMensagens/<int:id>',views.DeletaMinhaMensagem, name="DeletaMinhasMensagens"),
path('Drops-buffalo/',views.DropsBuffalo,name="Drops-buffalo"), # CONTEÚDO
path('southern-rock/',views.SouthernRock,name="southern-rock"), # CONTEÚDO
path('cinema/',views.Cinema,name="cinema"),
path('playlist-forall/',views.RadioPlaylist,name="playlist-forall"), #CONTEÚDO
path('power-metal-bandas/',views.powerMetal,name="power-metal-bandas"), #CONTEÚDO
path('Nada-trivial-jonathan-hulten/',views.jonathanHulten,name="Nada-trivial-jonathan-hulten"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # imagem de perfil
   
