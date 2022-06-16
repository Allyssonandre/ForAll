from django import forms
from .models import *
from django.forms.widgets import Widget
from .models import Postagem
from .models import VideosCurtos
from .models import Perfil
from .models import Comentario
from .models import Momentos
from .models import Eccommence,Pensamento,Loja,ComentaPosts,Spotify,LojaPremium,IncricaoPremium,MessageUser
# FORM DAS POSTAGENS
class Post(forms.ModelForm):
	class Meta:
		model  = Postagem
		fields = 'titulo','categoria','imagem_do_post','comenta'

# FORM DAS POSTAGENS DE VÍDEOS
class Videos(forms.ModelForm):
	class Meta:
		model  = VideosCurtos
		fields = 'titulo','categoria','video','comenta' 

# FORM DE TODOS OS COMENTÁRIOS DE POST DA
class Comentapost(forms.ModelForm):
	class Meta:
		model  = Comentario
		fields = 'comentando','nome','comente'

# FORM DE PERFIL EXTENDIDO DO DJANGO		
class CriarPerfil(forms.ModelForm):
	class Meta:
		model  = Perfil
		fields = 'cep','rua','bairro','cidade','uf','image','escolaridade','termos'

# FORM DOS STORIES DOS USUÁRIOS
class MomentosHistoria(forms.ModelForm):
	class Meta:
		model  = Momentos
		fields = 'momento','img1','img2','cidade','estado','descrever'

# FORM DO E-COMMERCE MARKETPLACE FORALL, COM UM SÓ ANÚNCIO 		
class EccommenceForm(forms.ModelForm):
	descrever_produto = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	class Meta:
		model  = Eccommence
		fields = 'nome','titulo_produto','categori_produto','tipo_transacao','cidade_mora','estado_mora','cartao','estado_produto','preco_produto','contato','image_produto','descrever_produto'

# FORM DAS FRASE DO USUÁRIO
class Penso(forms.ModelForm):
	class Meta:
		model  = Pensamento
		fields = 'ideia', 

# FORM DE COMENTÁRIO UM POST DE UM USUÁRIO MEMBRO
class PostsComente(forms.ModelForm):
	class Meta:
		model = ComentaPosts
		fields = 'opniao','comentarios'


# FORM DE POSTAGEM DE UM PLAYLIST SPOTIFY
class MeuSpotify(forms.ModelForm):
	class Meta:
		model  = Spotify
		fields = 'video', 

# FORM PARA POSTAGEM DE ANÚNCIOS DO MARKTPLACE E-COMMERCE FORALL 
class PremiumLoja(forms.ModelForm):
	class Meta:
		model  = LojaPremium
		fields = 'nome','nome_produto','categori_produto','tipo_transacao','cidade_mora','estado_mora','cartao','estado_produto','preco_produto','contato','image_produto','descrever_produto'


# FORM PARA SOLICITA A PARTICIPAÇÃO E-COMMERCE FORALL PREMIUM
class SolicitacaoPremium(forms.ModelForm):
	class Meta:
		model = IncricaoPremium
		fields = 'nomeCompleto','email','cidade','meuEstado','termos'


# FORM PARA MENSAGENS DE USUÁRIO PARA USUÁRIO

class MessageToUser(forms.ModelForm):
	class Meta:
		model = MessageUser
		fields= 'sendUser','messagem' 
