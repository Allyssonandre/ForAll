from django.contrib import admin
from django.contrib.auth import get_permission_codename
from embed_video.admin import AdminVideoMixin
from .models import Postagem
from .models import VideosCurtos
from .models import Comentario
from .models import Perfil
from .models import Momentos,Eccommence,Pensamento, Comente, Loja,ComentaPosts,Spotify,LojaPremium,IncricaoPremium,Parceiros,MessageUser

class Posts(admin.ModelAdmin):
	list_display = ('titulo','comenta','user','criado')
	search_fields = ('user',) 

admin.site.register(Postagem, Posts) 
admin.site.register(VideosCurtos)
admin.site.register(Comentario)
admin.site.register(Perfil)
admin.site.register(Momentos)
admin.site.register(Eccommence)
admin.site.register(Pensamento)
admin.site.register(Comente)
admin.site.register(Loja)
admin.site.register(ComentaPosts)
admin.site.register(Spotify)
admin.site.register(LojaPremium)
admin.site.register(IncricaoPremium)
admin.site.register(Parceiros)
admin.site.register(MessageUser)
# CLASSE ADMIN
class MyModelAdmin(admin.ModelAdmin):
   readonly_fields = ('field')
admin.site.site_header = "ForAll"