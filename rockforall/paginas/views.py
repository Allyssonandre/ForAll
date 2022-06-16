from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse 
from django.urls import reverse
from .models import Postagem
from .forms import Post
from .models import VideosCurtos
from .forms import Videos
from .models import Perfil
from .forms import CriarPerfil
from .forms import Comentapost
from .models import Comentario
from .models import Parceiros
from .models import Momentos,Eccommence,Pensamento,ComentaPosts,Spotify,LojaPremium,IncricaoPremium,MessageUser
from .forms import MomentosHistoria,EccommenceForm,Penso,Loja,PostsComente,MeuSpotify,PremiumLoja,SolicitacaoPremium,MessageToUser
from django.http import HttpResponseRedirect
import datetime
from django.contrib.auth.models import User,Group

#********************************* INICIO ******************************************************************
 
# *******************INDEX**********************
def index(request):
	loja  = Loja.objects.all()[:4]
	comenta = Comentario.objects.all()
	comentados = ComentaPosts.objects.all().order_by('-data_comenta')[:3]
	return render(request, 'inicio/index.html',{'loja':loja,'comenta':comenta,'comentados':comentados})

#***********************************************
 
#*************TEMPLATE DAS POSTAGENS NO PERFIL FORALL************
@login_required 
def perfil(request):
	postados   =  Postagem.objects.all().order_by('-criado')
	produtos   =  Eccommence.objects.all().order_by('-produto_criado')[:2]
	videos     =  VideosCurtos.objects.all().order_by('-criadoem')[:4]
	todoPost   =  Postagem.objects.all().order_by('-criado')[:2]
	comentados =  Comentario.objects.all().order_by('-data')[:2]
	pensando   =  Pensamento.objects.all().filter(user=request.user).order_by('-foiCriado')[:1]
	meusComentados = ComentaPosts.objects.all().filter(user=request.user).order_by('-data_comenta')[:2]
	spotify  = Spotify.objects.all().filter(user=request.user).order_by('-criadoEm')
	todospotify  = Spotify.objects.all().order_by('-criadoEm')
	comentariosTempoReal = ComentaPosts.objects.all().order_by('-data_comenta')[:1]
	incricaopremium = IncricaoPremium.objects.all().filter(user=request.user)
	mensagemUmUsuario = MessageUser.objects.all().filter(sendUser=request.user)
	meusmomentos   = Momentos.objects.all().order_by('-criacao')[:3]
	meuspostscomentados = ComentaPosts.objects.all().order_by('-data_comenta')[:1]
	

	post = Post(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if post.is_valid():
			obj = post.save(commit=False)
			obj.user = request.user;
			obj.save()
			messages.info(request, "Sua Postagem foi criada, você pode continua postando.")
			return redirect('perfil')
	else:
		post = Post()

	pensamento = Penso(request.POST or None)
	if request.method == 'POST':
		if pensamento.is_valid():
			obj = pensamento.save(commit=False)
			obj.user = request.user;
			obj.save()
			messages.info(request, "Pensamento postado com sucesso!!.")
			return redirect('perfil')
	else:
		pensamento = Penso()



	c = {'postados':postados,'produtos':produtos,'videos':videos,'todoPost':todoPost,
	'comentados':comentados,'pensamento':pensamento,'pensando':pensando,'meusComentados':meusComentados,
	'spotify':spotify,'todospotify':todospotify,'comentariosTempoReal':comentariosTempoReal,'incricaopremium':incricaopremium,'post':post
	, 'mensagemUmUsuario':mensagemUmUsuario, 'meusmomentos':meusmomentos, 'meuspostscomentados':meuspostscomentados}
	return render(request, 'inicio/perfil.html', c)

#************************************************

#*********TEMPLATE PARA CRIAR POSTAGENS, IMPLEMENTAÇÃO ANTIGA**********
#@login_required
#def formulario(request):
#	post = Post(request.POST or None, request.FILES or None)
#	if request.method == 'POST':
#		if post.is_valid():
#			obj = post.save(commit=False)
#			obj.user = request.user;
#			obj.save()
#			messages.info(request, "Sua Postagem foi criada, você pode continua postando.")
#			return redirect('/formulario')
#	else:
#		post = Post()
#		return render(request, 'inicio/formulario.html', {'post':post})


#**********TEMPLATE DE PESQUISA DE POSTAGEM *****
def postados(request):
	busca = request.GET.get('busca')
	if busca:
		postados = Postagem.objects.all().filter(categoria__icontains=busca)
	else:
		postados  =  Postagem.objects.all().order_by('-criado')
	return render(request, 'inicio/ver.html',{'postados':postados})

#*******TEMPLATE PARA EDITAR POSTAGEM DA PÁGINA INICIAL***********
@login_required
def editar(request, id):
	formu = get_object_or_404(Postagem, pk=id)
	form = Post(instance=formu)
	if(request.method == 'POST'):
		form = Post(request.POST, instance=formu)
		if(form.is_valid()):
			formu.save()
			messages.info(request, 'A postagem escolhida foi editada!!')
			return redirect('/meusposts')
		else:
			return render(request, 'inicio/editar.html', {'form': form, 'formu': formu})
	else:
		return render(request, 'inicio/editar.html', {'form': form, 'formu': formu})
#*****************************************************

#*******TEMPLATE PARA EDITAR POSTAGEM DO PERFIL***********

@login_required
def EditaDePerfil(request, id):
	formu = get_object_or_404(Postagem, pk=id)
	form = Post(instance=formu)
	if(request.method == 'POST'):
		form = Post(request.POST, instance=formu)
		if(form.is_valid()):
			formu.save()
			messages.info(request, 'A postagem escolhida foi editada!!')
			return redirect('/Perfil-completo')
		else:
			return render(request, 'inicio/editar.html', {'form': form, 'formu': formu})
	else:
		return render(request, 'inicio/editar.html', {'form': form, 'formu': formu})
#***************************************************************************************

#************TEMPLATE PARA DELETA POSTAGEM NO CAMINHO /meuposts************
@login_required
def deleta(request, id):
	deletando = get_object_or_404(Postagem, pk=id)
	deletando.delete()
	messages.info(request, 'Essa postagem foi excluida!!')
	return redirect('/meusposts')
#******************************************************
 
#************TEMPLATE PARA DELETA POSTAGEM NO CAMINHO /Perfil-completo************
@login_required
def deletaPerfil(request, id):
	deletando = get_object_or_404(Postagem, pk=id)
	deletando.delete()
	messages.info(request, 'Essa postagem foi excluida!!')
	return redirect('/Perfil-completo')
#******************************************************

#******************************MEMBROS DA REDE SOCIAL**********************************#

@login_required
def Membros(request):
	membros_forall = Perfil.objects.all()
	return render(request, 'inicio/membros.html', {'membros_forall': membros_forall})
	
#*************************************************************************************

#**************TEMPLATE PARA POSTA VÍDEOS*************
@login_required
def videos(request):
	videos = Videos(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if videos.is_valid():
			obj = videos.save(commit= False)
			obj.user = request.user;
			obj.save()
			messages.info(request, "Vídeo publicado, você pode posta novamente.!!")
			return redirect('/videos')
	else:
		videos = Videos()
		return render(request, 'inicio/videos.html', {'videos':videos})
#******************************************************

#*****TEMPLATE DOS VIDEOS DE UM USÚARIO ESPECIFICO******
@login_required 
def mostravideos(request):
	videospostados  =  VideosCurtos.objects.all().filter(user=request.user).order_by('-criadoem')
	return render(request, 'inicio/meusvideos.html', {'videospostados':videospostados})
#*******************************************************
#*****TEMPLATE DE TODAS AS POSTAGENS DE UM USUÁRIO EM ESPECIFICO
@login_required
def Meuposts(request):
	postagens = Postagem.objects.all().filter(user=request.user).order_by('-criado')
	return render(request, 'inicio/meusposts.html', {'postagens':postagens})

#*******TEMPLATE PARA DELETA VÍDEOS*********************
@login_required
def deletavideo(request, id):
	deletavideo = get_object_or_404(VideosCurtos, pk=id)
	deletavideo.delete()
	messages.info(request, 'Vídeo excluido!!')
	return redirect('mostravideos')
#*******************************************************

#******TEMPLATE DE PESQUISA DE VIDEOS POSTADOS**********
def videospublicados(request):
	busca = request.GET.get('busca')
	if busca:
		videospostados  =  VideosCurtos.objects.all().filter(categoria__icontains=busca)
	else:
		videospostados = VideosCurtos.objects.all().order_by('-criadoem')
	return render(request, 'inicio/videospublicados.html',{'videospostados':videospostados})
#*******************************************************

#**TEMPLATE DE DETALHES DAS POSTAGENS DE USUARIO EM ESPECIFICO**
def postdetalhes(request, id):
	detalhes = get_object_or_404(Postagem,pk=id)
	detalhes.post_views = detalhes.post_views + 1
	detalhes.save()
	return render(request, 'inicio/postdetalhes.html', {'detalhes':detalhes})
#*******************************************************

#def likeView(request,pk):
#	likepost = get_object_or_404(Postagem, id=request.POST.get('postagem_id'))
#	likepost.like.add(request.user)
#	return HttpResponseRedirect(reverse('postaDetalhe', args=[str(pk)]))

#******TEMPLATE DE TERMOS*************
def termos(request):
	return render(request, 'inicio/termos.html')
#*******************************************************

#*****TEMPLATE DA CRIAÇÃO DE UM PERFIL DE UM USUARIO****
@login_required
def criarperfil(request):
	perfil = CriarPerfil(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if perfil.is_valid():
			obj = perfil.save(commit=False)
			obj.user = request.user;
			obj.save()
			messages.info(request, "Seu Perfil já foi criado")
			return redirect('/perfil')
	else:
		perfil = CriarPerfil()
		return render(request, 'inicio/criaperfil.html', {'perfil':perfil})

#*********************************************************


#*********TEMPLATE PARA EDITA PERFIL**********************
@login_required
def editaperfil(request, id):
	perfil = get_object_or_404(Perfil,pk=id)
	edite  = CriarPerfil(instance=perfil)
	if(request.method == 'POST'):
		edite = CriarPerfil(request.POST,instance=perfil)
		if(edite.is_valid()):
			edite.user = request.user;
			perfil.save()
			messages.info(request, 'Perfil editado com sucesso.!!')
			return redirect('perfil')
		else:
			return render(request, 'inicio/editaperfil.html', {'edite':edite,'perfil':perfil})
	else:
		return render(request, 'inicio/editaperfil.html', {'edite':edite,'perfil':perfil})
#***********************************************************

#***************TEMPLATE DE COMENTARIOS NO BLOG*********************
def comentando(request,id):
	perfil = Comentapost(request.POST or None, request.FILES or None,pk=id)
	if request.method == "POST":
		perfil = Comentapost(request.POST)
		if perfil.is_valid():
			comment = perfil.save(commit=False)
			comment.user = request.user;
			comment.save()
			return redirect('comentarios')
	else:
		perfil = Comentapost()
		return render(request, 'inicio/comentando.html', {'perfil': perfil})
#**************************************************************

#*********TEMPLATE DE MÁTERIAS DO SITE*************************
def tutorial(request):
	return render(request, 'inicio/tutorial.html')
#**************************************************************

#********TEMPLATE DE PESQUISA DAS POSTAGENS(LOGADO)************
@login_required
def verpostagens(request):
	busca = request.GET.get('busca')
	if busca:
		postados  =  Postagem.objects.all().filter(categoria__icontains=busca)
	else:
		postados = Postagem.objects.all().order_by('-criado')

	return render(request, 'inicio/verpostados.html',{'postados':postados})
#***************************************************************

#******TEMPLATE DE PESQUISA DE TODOS OS VIDEOS(LOGADO)**********
@login_required
def todosvideos(request):
	busca = request.GET.get('busca')
	if busca:
		postados  =  VideosCurtos.objects.all().filter(categoria__icontains=busca)
	else:
		postados = VideosCurtos.objects.all().order_by('-criadoem')

	return render(request, 'inicio/todosvideos.html',{'postados':postados})
#****************************************************************

#************TEMPLATE DE MÁTERIAS DO BLOG************************
def indicacao(request):
	return render(request, 'inicio/indicacao.html')
#****************************************************************
#***********TEMPLATE DE MATÉRIAS DO BLOG*************************
def destaque(request):
	return render(request, 'inicio/destaque.html')
#****************************************************************

#****TEMPLATE DE DETALHES DOS VÍDEOS DE USUARIO EM ESPECIFICO****
def detalhesVideos(request, id):
	detalhesvideos = get_object_or_404(VideosCurtos,pk=id)
	detalhesvideos.post_views = detalhesvideos.post_views + 1
	detalhesvideos.save()
	return render(request, 'inicio/detalhesvideos.html', {'detalhesvideos':detalhesvideos})
#******************************************************************

#******TEMPLATE DO FORMULÁRIO PARA COMENTÁRIO DE POSTAGENS********* 
def formulariocomentario(request):
	comentados = Comentapost(request.POST or None , request.FILES or None)
	if request.method == 'POST':
		comentados = Comentapost(request.POST)
		if comentados.is_valid():
			comenta = comentados.save(commit=False)
			comenta.user = request.user;
			comenta.save()
			messages.info(request, 'Seu comentário foi publicado, para ver faça login ou se torne membro do ForAll se cadastrando.!!')
			return redirect('formulariocomentario')
	else:
		comentados = Comentapost()
		return render(request, 'inicio/formulariocomentario.html',{'comentados':comentados})
#**********************************************************************
	
#****TEMPLATE COM TODOS OS COMENTÁRIOS SOBRE AS POSTAGENS DE USUÁRIOS****	
@login_required
def comentados(request):
	busca = request.GET.get('busca')
	if busca:
		comentado = Comentario.objects.all().filter(comentando__user__id__icontains=busca)
	else:
		comentado = Comentario.objects.all().order_by('-data')
	return render(request ,'inicio/todoscomentarios.html', {'comentado':comentado})
#************************************************************************


#*************TEMPLATE PARA CRIAR STORIES********************************

@login_required
def momentos(request):
	momentos = MomentosHistoria(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if momentos.is_valid():
			momento = momentos.save(commit=False)
			momento.user = request.user;
			momento.save()
			messages.info(request, 'Momento publicado, você pode publica mais.')
			return redirect('momentos')
	else:
		momentos = MomentosHistoria()
		return render(request, 'inicio/momentos.html',{'momentos':momentos})

#***************************************************************************

#*****************TEMPLATE COM TODO OS STORIES******************************

@login_required
def verstories(request):
	momentos = Momentos.objects.all().order_by('-criacao')
	return render(request, 'inicio/vermomentos.html',{'momentos':momentos})

#***************************************************************************

#*************TEMPLATE DE DETALHES DOS STORIES******************************
@login_required
def detalhestories(request, id):
	detalhes = get_object_or_404(Momentos, pk=id)
	detalhes.visto = detalhes.visto + 1
	detalhes.save()
	return render(request, 'inicio/detalhe_stories.html',{'detalhes':detalhes})
#****************************************************************************

#**************TEMPLATE PARA A CRIAÇÃO DE ANÚNCIO DE UM SÓ PRODUTO***************
@login_required
def criaranuncio(request):
	produtos  = EccommenceForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if produtos.is_valid():
			produto = produtos.save(commit=False)
			produto.user = request.user;
			produto.save()
			messages.info(request, 'Seu produto foi cadastrado')
			return redirect('perfil')
	else:
		produtos = EccommenceForm()
		return render(request, 'inicio/criar_anuncio.html',{'produtos':produtos})
#********************************************************************************

#********************TEMPLATE DE PESQUISA DE PRODUTOS****************************
@login_required
def produtos(request):
	busca = request.GET.get('busca')
	if busca:
		verprodutos = Eccommence.objects.all().filter(categori_produto__icontains=busca)
	else:
		verprodutos = Eccommence.objects.all().order_by('-produto_criado')
	return render(request, 'inicio/produtos.html',{'verprodutos':verprodutos})
#*********************************************************************************

#**********************TEMPLATE DE STORIES DE USUÁRIO ESPECIFICO******************
@login_required
def meustories(request):
	stories = Momentos.objects.all().filter(user=request.user).order_by('-criacao')
	return render(request, 'inicio/meu_storie.html',{'stories':stories})
#*********************************************************************************

#**********************TEMPLATE PARA DELETA STORIES*******************************
@login_required
def deletastories(request, id):
	deletaStories = get_object_or_404(Momentos, pk=id)
	deletaStories.delete()
	messages.info(request, 'Stories excluido!!')
	return redirect('meustories')
#**********************************************************************************

#****************TEMPLATE COM TODO OS COMENTARIOS DE UM USÁRIO ESPECIFICO**********	
@login_required
def postcomentados(request):
	comentado = Comentario.objects.all().filter(comentando__user=request.user).order_by('-data')
	return render(request ,'inicio/meuscomentarios.html',{'comentado':comentado})
#**********************************************************************************

#******************TEMPLATE DE DETALHES DE UM PRODUTO******************************
@login_required
def detalheproduto(request, id):
	detalheProduto = get_object_or_404(Eccommence, pk=id)
	detalheProduto.view_produto = detalheProduto.view_produto + 1
	detalheProduto.save()
	return render(request, 'inicio/detalhe_produto.html',{'detalheProduto':detalheProduto})


#******************TEMPLATE DE BUSCA DE PRODUTOS POR USUÁRIO******************************

@login_required
def meusProdutos(request):
	meus_produtos = Eccommence.objects.all().filter(user=request.user).order_by('-produto_criado')
	return render(request, 'inicio/meusanuncios.html', {'meus_produtos':meus_produtos})


#******************TEMPLATE DE DELETA PRODUTOS******************************

@login_required
def deletaproduto(request,id):
	delete_produto = get_object_or_404(Eccommence, pk=id)
	delete_produto.delete()
	messages.info(request, 'Anúncio excluido')
	return redirect('meusProdutos')


#******************TEMPLATE PARA DELETA COMENTÁRIOS******************************

@login_required
def deletacomentarios(request,id):
	delete_comentario = get_object_or_404(Comentario, pk=id)
	delete_comentario.delete()
	messages.info(request , 'O comentário foi excluido.')
	return redirect('postcomentados')


#******************TEMPLATE DE TERMOS DE USO DA LOJA******************************

@login_required
def termosloja(request):
	return render(request, 'inicio/termos_loja.html')
#*****************TEMPLATE DE CONTEÚDO********************************************
def artigo(request):
	return render(request, 'inicio/artigo-son-house.html')

#******* SALA DE BATE-PAPO *********
@login_required
def Sala(request):
	return render(request, 'inicio/chart.html')
  

#******* SALA *********
@login_required
def room(request, room_name):
	return render(request, 'inicio/room.html', {'room_name': room_name})


#****TEMPLATE DA LOJA PRIVADA DO FORALL******************************************
def MinhaLoja(request):
	loja  = Loja.objects.all().order_by('-criando')
	return render(request, 'inicio/loja.html',{'loja':loja})

#******** DETALHE DE PRODUTOS DA LOJA PRIVADA DO FORALL
def ProdutoDetalhe(request, id):
	loja = get_object_or_404(Loja, pk=id)
	return render(request, 'inicio/detalhe-loja.html',{'loja':loja})

#*****TEMPLATE DE CONTEÚDO DO BLOG*******
def Dica(request):
	return render(request, 'inicio/dica.html')

#*****TEMPLATE DE CONTEÚDO DO BLOG*******

def BreveHistoria(request):
	return render(request, 'inicio/Breve_Historia.html')

#*****TEMPLATE DE CONTEÚDO DO BLOG*******

def Primeiraresenha(request):
	return render(request,'inicio/Primeira-resenha.html')

#*****TEMPLATE DE CONTEÚDO DO BLOG*******

def Segundaresenha(request):
	return render(request,'inicio/Segunda-resenha.html')
#*****TEMPLATE DE CONTEÚDO DO BLOG*******

def Terceiraresenha(request):
	return render(request,'inicio/Terceira-resenha.html')
#*****TEMPLATE DE CONTEÚDO DO BLOG*******

def Quartaresenha(request):
	return render(request,'inicio/Quarta-resenha.html')

#*****TEMPLATE DE CONTEÚDO DO BLOG*******

def Quintaresenha(request):
	return render(request,'inicio/Quinta-resenha.html')

#*****TEMPLATE DE CONTEÚDO DO BLOG*******

def RedacaoReportagem(request):
	return render(request, 'inicio/Redacao_reportagem.html')


# DISPLAY DOS MEUS PARCEIROS(DESLOGADO)
def Meus_Parceiros(request):
	busca = request.GET.get('busca')
	if busca:
		parceiros = Parceiros.objects.all().filter(ramo__icontains=busca)
	else:
		colaborador = Parceiros.objects.all()
		paginator   = Paginator(colaborador,30)
		pagina      = request.GET.get('page')
		parceiros   = paginator.get_page(pagina)
	return render(request, 'inicio/parceiros.html', {'parceiros':parceiros})


# DETALHES DOS MEUS PARCEIROS(DESLOGADO)
def EspacoParceiro(request,id):
	parceiros = get_object_or_404(Parceiros, pk=id)
	parceiros.view_parceiro = parceiros.view_parceiro + 1
	parceiros.save()
	return render(request, 'inicio/Espaco_parceiro.html', {'parceiros':parceiros})

# DISPLAY DOS MEUS PARCEIROS(LOGADO)
@login_required
def ParceirosLogado(request):
	busca = request.GET.get('busca')
	if busca:
		parceiros_logados = Parceiros.objects.all().filter(ramo__icontains=busca)
	else:
		colaboradores = Parceiros.objects.all()
		paginator     = Paginator(colaboradores,30)
		pagina        = request.GET.get('page')
		parceiros_logados = paginator.get_page(pagina)
	return render(request, 'inicio/Parceiros_Logado.html', {'parceiros_logados':parceiros_logados})


# DETALHES DOS MEUS PARCEIROS LOGADOS
@login_required
def ParceiroLogadoDetalhe(request,id):
	parceiros_logado_detalhe = get_object_or_404(Parceiros, pk=id)
	return render(request, 'inicio/Parceiro-Logado-detalhe.html', {'parceiros_logado_detalhe':parceiros_logado_detalhe})


#**********************************************************************************************
#******************** VIEW DE EXCLUIR PENSAMENTO **********************************
@login_required
def ExcluiPensamento(request,id):
	delete_pensamento = get_object_or_404(Pensamento, pk=id)
	delete_pensamento.delete()
	messages.info(request , 'Pensamento excluído.')
	return redirect('perfil')

# TEMPLATE DE DETALHE DA POSTAGENS DOS USUÁRIOS(LOGADO)
@login_required
def DetalhePost(request,id):
	post = get_object_or_404(Postagem, pk=id)
	return render(request , 'inicio/Post-Detalhe.html', {'post':post})

# VIEW DE CRIAÇÃO DE COMENTÁRIO DE UMA POSTAGEM
@login_required
def DetalharPost(request,id):
	postagem = Postagem.objects.get(pk=id)
	if request.method == 'POST':
		form = PostsComente(request.POST)
		if form.is_valid():
			formu = form.save(commit=False)
			formu.user = request.user;
			formu.postagem = postagem;	
			formu.save()
			messages.info(request, "Seu comentário foi compartilhado, você pode posta mais sobre isto ou volta para seu perfil!!")
			return HttpResponseRedirect(reverse('detalhar-post', args=[id]))
	else:
		form = PostsComente()
		return render(request,'inicio/detalhar_post.html',{'form':form,'postagem':postagem})



# VIEW DE CRIAÇÃO DE UMA PLAYLIST SPOTIFY
@login_required
def PlayList(request):
	spotify = MeuSpotify(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if spotify.is_valid():
			obj = spotify.save(commit=False)
			obj.user = request.user;
			obj.save()
			messages.info(request, "Sua playlist foi publicada!!")
			return redirect('perfil')
	else:
		spotify = MeuSpotify()
		return render(request, 'inicio/playlist.html',{'spotify':spotify})

# VIEW PARA DELETA UMA PLAYLIST SPOTIFY
@login_required
def DeletePlay(request, id):
	spotify = get_object_or_404(Spotify, pk=id)
	spotify.delete()
	messages.info(request, 'Essa playlist foi deletada!!')
	return redirect('perfil')


# DELETA PLAYLIST DO PERFIL COMPLETO
@login_required

def DeletaPlayPerfil(request, id):
	spotify = get_object_or_404(Spotify, pk=id)
	spotify.delete()
	messages.info(request, 'Essa playlist foi deletada!!')
	return redirect('Perfil-completo')

# DASHBOARD ADMINISTRATIVO
@login_required
def Usuarios(request):
	usuario    = Perfil.objects.all()
	group      = Group.objects.get(name="PremiumLoja").user_set.all()
	usuario.data = datetime.datetime.now()
	return render(request, 'inicio/usuario.html',{'usuario':usuario,'group':group})

# TEMPLATE DE TODAS AS SOLICITAÇÕES DE INSCRIÇÃO NO MARKTPLACE E-COMMERCE PREMIUM(DASHBOARD ADMINISTRATIVO)
@login_required
def InscritosPremium(request):
	inscritos = IncricaoPremium.objects.all()
	return render(request, 'inicio/inscritospremium.html',{'inscritos':inscritos})

#--------------------------------------------------------------
#*****TEMPLATE DE CONTEÚDO DO BLOG*******
def Redacao(request):
	return render(request, 'inicio/redacao.html')

# VIEW DE CRIAÇÃO DE ANÚNCIOS DO MARKTPLACE E-COMMERCE USUÁRIO PREMIUM
@login_required
def Premium(request):
	userpremium = PremiumLoja(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if userpremium.is_valid():
			obj = userpremium.save(commit=False)
			obj.user = request.user;
			obj.save()
			messages.info(request, "A postagem do seu produto foi cadastrada!!, Boas vendas.")
			return redirect('/lojapremium')
	else:
		userpremium = PremiumLoja()
		return render(request, 'inicio/lojapremium.html', {'userpremium':userpremium})

# VIEW DE CRIAÇÃO DA SOLICITAÇÃO MARKTPLACE E-COMMERCE USUÁRIO PREMIUM
@login_required
def InscricaoPremium(request):
	incricaopremium = SolicitacaoPremium(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if incricaopremium.is_valid():
			o = incricaopremium.save(commit=False)
			o.user = request.user;
			o.save()
			messages.info(request, "Inscrição realizada com sucesso, você receberá um link de pagamento em 24 Horas.")
			return redirect('perfil')
	else:
		incricaopremium = SolicitacaoPremium()
		return render(request, 'inicio/inscricaopremium.html', {'incricaopremium':incricaopremium})


# VIEW DE CANCELAMENTO DE INCRIÇÃO MARKTPLACE E-COMMERCE USUÁRIO PREMIUM
@login_required
def CancelaPremium(request, id):
	cancelepremium = get_object_or_404(IncricaoPremium, pk=id)
	cancelepremium.delete()
	messages.info(request, 'Sua inscrição Premium foi cancelada!!, mas você pode se inscrever novamente, atráves do botão "Quero ser premium".')
	return redirect('perfil')


# EDITA INSCRIÇÃO DE USUÁRIOS PREMIUM, PARA POSTAGEMS DE PRODUTOS DO GRUPO PremiumLoja FORALL

#@login_required
#def EditarPremium(request, id):
#	premium = get_object_or_404(IncricaoPremium, pk=id)
#	premium_model = SolicitacaoPremium(instance=premium)
#	if request.method == 'POST':
#		premium_model = SolicitacaoPremium(request.POST, instance=premium)
#		if premium_model.is_valid():
#			premium_model.save()
#			messages.info(request , 'Usuário editado.')
#			return redirect('inscritospremium')
#		else:
#			return render(request, 'inicio/editarpremium.html', {'premium_model':premium_model,'premium':premium})
#	else:
#		return render(request, 'inicio/editarpremium.html', {'premium_model':premium_model,'premium':premium})


# VIEW DE PRODUTOS MARKTPLACE E-COMMERCE USUÁRIO PREMIUM
def ProdutoPremium(request):
	busca = request.GET.get('busca')
	if busca:
		produtopremium = LojaPremium.objects.all().filter(nome_produto__icontains=busca)
	else:
		premium = LojaPremium.objects.all()
		paginator = Paginator(premium,20)
		pagina     = request.GET.get('page')
		produtopremium = paginator.get_page(pagina)
	return render(request, 'inicio/produtopremium.html',{'produtopremium':produtopremium})


# DETALHE DOS ANÚNCIOS PREMIUMS

def DetalhePremium(request, id):
	produtopremium = get_object_or_404(LojaPremium, pk=id)
	produtopremium.view_produto = produtopremium.view_produto + 1
	produtopremium.save()
	return render(request, 'inicio/detalheProdutoPremium.html',{'produtopremium':produtopremium})

# PRODUTOS PREMIUMS DENTRO DO PERFIL DOS MEMBROS

@login_required
def ProdutosPremiums(request):
	busca = request.GET.get('busca')
	if busca:
		produtopremium = LojaPremium.objects.all().filter(nome_produto__icontains=busca)
	else:
		premium = LojaPremium.objects.all()
		paginator = Paginator(premium,30)
		pagina     = request.GET.get('page')
		produtopremium = paginator.get_page(pagina)
	return render(request, 'inicio/produtospremiums.html',{'produtopremium':produtopremium})

# DETALHE DE UM PRODUTO DE TODOS OS USUÁRIOS PREMIUM

@login_required
def DetalhesPremium(request, id):
	detalhepremium = get_object_or_404(LojaPremium, pk=id)
	return render(request, 'inicio/detalhespremiums.html', {'detalhepremium':detalhepremium})

# DETALHE E EDIÇÃO DE PRODUTOS DE UM USUÁRIO.

@login_required
def DetalhesPremiumUsuario(request):
	busca = request.GET.get('busca')
	if busca:
		detalhepremium = LojaPremium.objects.all().filter(user=request.user,nome_produto__icontains=busca)
	else:
		premium = LojaPremium.objects.all().filter(user=request.user)
		paginator = Paginator(premium,20)
		pagina     = request.GET.get('page')
		detalhepremium = paginator.get_page(pagina)
	return render(request, 'inicio/detalhes_usuario_premium.html',{'detalhepremium':detalhepremium}) 


# EDITAR OS ANÚNCIOS PREMIUMS
@login_required
def EditarAnuncioPremium(request, id):
	editar_anuncio = get_object_or_404(LojaPremium,pk=id)
	editar  = PremiumLoja(instance=editar_anuncio)
	if(request.method == 'POST'):
		editar = PremiumLoja(request.POST,instance=editar_anuncio)
		if(editar.is_valid()):
			editar_anuncio.save()
			messages.info(request, 'Seu anúncio foi editado com sucesso!!.')
			return redirect('/anuncios_usuarios_premium')
		else:
			return render(request, 'inicio/editar_anuncio_premium.html', {'editar':editar,'editar_anuncio':editar_anuncio})
	else:
		return render(request, 'inicio/editar_anuncio_premium.html', {'editar':editar,'editar_anuncio':editar_anuncio})

# DELETAR ANÚNCIO PREMIUM
@login_required
def DeletaAnuncioPremium(request,id):
	deletar_anuncio = get_object_or_404(LojaPremium, pk=id)
	deletar_anuncio.delete()
	messages.info(request, 'Anúncio excluído.')
	return redirect('anuncios_usuarios_premium')

# CRIAR MENSAGEM DE UM USUÁRIO PARA OUTRO 
@login_required
def MinhaMensagem(request):
	mensagemUmUsuario = MessageUser.objects.all().filter(sendUser=request.user)

	mensagem = MessageToUser(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if mensagem.is_valid():
			obj = mensagem.save(commit=False)
			obj.user = request.user;
			obj.save()
			messages.info(request, "Mensagem enviada com sucesso.")
			return redirect('MinhasMensagens')
	else:
		mensagem = MessageToUser()

	return render(request, 'inicio/minhas_mensagens.html', {'mensagemUmUsuario':mensagemUmUsuario, 'mensagem':mensagem})

# DELETA MENSAGEM
@login_required
def DeletaMinhaMensagem(request, id):
	deletaMensagem = get_object_or_404(MessageUser, pk=id)
	deletaMensagem.delete()
	messages.info(request, 'Mensagem deletada!!')
	return redirect('MinhasMensagens')


# PÁGINA PARA CONTEÚDO

def BobMould(request):
	return render(request, 'inicio/Bob-mould.html')


def ArtistasBrasileiros(request):
	return render(request, 'inicio/Artistas_Brasileiros.html')



def bandaIrlanda(request):
	return render(request, 'inicio/Bandas_islandesas.html')


def DropsBuffalo(request):
	return render(request, 'inicio/Drops_Buffalo.html')

def SouthernRock(request):
	return render(request, 'inicio/southern_rock.html')

def RadioPlaylist(request):
	return render(request, 'inicio/playlist_forall.html')

def powerMetal(request):
	return render(request, 'inicio/power-metal-bandas.html')

def jonathanHulten(request):
	return render(request, 'inicio/nada-trivial-jonathanHulten.html')

def DicasQuadrinhos(request):
	return render(request, 'inicio/Dicas_Quardinhos.html')

def Testando(request):
	return render(request, 'inicio/Testando.html')

@login_required
def perfilCompleto(request):
	meus_posts = Postagem.objects.all().filter(user=request.user)
	meusmomentos   = Momentos.objects.all().filter(user=request.user).order_by('-criacao')[:3]
	postados   =  Postagem.objects.all().order_by('-criado')[:5]
	videospostados  =  VideosCurtos.objects.all().filter(user=request.user).order_by('-criadoem')[:3]
	todospotify  = Spotify.objects.all().filter(user=request.user).order_by('-criadoEm')[:3]
	return render(request, 'inicio/Perfil_completo.html',{'meus_posts':meus_posts,
		'meusmomentos':meusmomentos,'postados':postados
		,'videospostados':videospostados,'todospotify':todospotify})



