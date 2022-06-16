from django.contrib import admin
from django.urls import path, include
# IMPORT DAS CONFIGURAÇÕES DA IMAGEM
from django.conf import settings
from django.contrib.auth import views as auth_views
# ------------------------------------
# CAMINHO DA IMAGEM, IMPORTANDO O STATIC
from django.conf.urls.static import static
# URL´S DE REDEFIÇÃO DE SENHA
urlpatterns = [
path('admin/', admin.site.urls),
path('',include('paginas.urls')),
path('',include('redacao.urls')),  
path('accounts/',include('accounts.urls')),
path('accounts/', include('django.contrib.auth.urls')),
path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registraton/password_reset_form.html'),
   name='password_reset'),
path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'
   ),name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'
   ),name='password_reset_confirm'),
path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'
   ),  name='password_reset_complete'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # imagem de perfil
