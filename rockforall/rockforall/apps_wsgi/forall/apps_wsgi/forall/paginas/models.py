import datetime
import os
from django.db import models
from embed_video.fields import EmbedVideoField 
from django.contrib.auth.models import User
# A classe Postagem tem um relacionamento com a classe comentario de OneToMany(1 para muitos)
# CLASSE CRIAR POSTAGEM
class Postagem(models.Model):
	titulo         = models.CharField(max_length=100,verbose_name='TÍTULO DA POSTAGEM')
	CATEGORIA = [
	('Música','Música'),
	('Cinema','Cinema'),
	('Dica','Dica'),
	('Curiosidade','Curiosidade'),
	('Diversão','Diversão'),
	('Outros','Outros')
	]
	categoria      = models.CharField(max_length=30,choices=CATEGORIA,verbose_name='CATEGORIA')
	imagem_do_post = models.ImageField(upload_to='media/posts', blank=False, verbose_name='IMAGEM DA POSTAGEM')
	comenta        = models.TextField(max_length=100, verbose_name='COMENTE: no máximo 150 caracteres')
	user           = models.ForeignKey(User,null=True, blank=True,on_delete= models.CASCADE, verbose_name='PUBLICADO COMO ?')
	criado         = models.DateTimeField(auto_now_add=True, verbose_name='CRIADO EM:') 
	mudado         = models.DateTimeField(auto_now=True)
	post_views     = models.IntegerField(default=0, null=True, blank=True)
	like           = models.ManyToManyField(User, related_name='liked')

	def contaLink(self):
		return self.like.count()

	def __str__(self):
		return 'Autor(%s) | Titulo(%s)' %(self.user,self.titulo);
#---------------------------------------------------------------------------------------------------

# CLASSE DE POSTAGENS DE VÍDEOS
class VideosCurtos(models.Model):
	video    = EmbedVideoField(verbose_name='LINK DO VÍDEO')
	titulo   = models.CharField(max_length=100, verbose_name='TÍTULO DO VÍDEO')
	CATEGORIA = [
	('Indicação','Indicação'),
	('YouTube','YouTube'),
	('Outros','Outros'),
	]
	categoria = models.CharField(max_length=30,choices=CATEGORIA,verbose_name='CATEGORIA DO VÍDEOS')
	comenta   = models.TextField(max_length=120,null=False,blank=False,verbose_name='COMENTE SOBRE ESTE VÍDEO')
	post_views= models.IntegerField(default=0, null=True,blank=True)
	user      = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE, verbose_name='Postado Por:')
	criadoem  = models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')
	mudadoem  = models.DateTimeField(auto_now=True)
 
	def __str__(self):
		return self.titulo;
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++		

# CLASSE DE COMENTÁRIO DE POSTAGENS RELACIONADA A VISITANTES DO SITE
class Comentario(models.Model):
	comentando  = models.ForeignKey(Postagem,on_delete=models.CASCADE, verbose_name='NOME DO AUTOR E O TITULO POSTAGEM') 
	nome        = models.CharField(max_length=100,null=True,blank=False, verbose_name="SEU NOME")
	comente     = models.TextField(max_length=100, verbose_name="Comente: no máximo 100 caracteres")
	data        = models.DateTimeField(auto_now_add=True,verbose_name="Data do comentário")
	datamudanca = models.DateTimeField(auto_now=True)
    
	def conta(self):
		return self.comentando.titulo.count()

	def __str__(self):
		return '%s - %s' %(self.comentando.titulo, self.nome);

#-----------------------------------------------------------------------------------------
# CLASSE DE PERFIL EXTENDIDO DO MODELO DE USUÁRIO DO DJANGO
class Perfil(models.Model):
	user = models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	cep = models.CharField(max_length=10)
	rua = models.CharField(max_length=60,blank=True)
	bairro = models.CharField(max_length=40,blank=True)
	cidade = models.CharField(max_length=40)
	uf     = models.CharField(max_length=2)
	image  = models.ImageField(upload_to='media/perfil', default='media/forall.png',null=True,blank=True, verbose_name='IMAGEM PERFIL :')
	escolaridade = models.CharField(max_length=30,verbose_name='ESCOLARIDADE') 
	termos   = models.CharField(max_length=4,verbose_name='TERMO DE USO E POLÍTICA DE PRIVACIDADE')
	data     = models.DateTimeField(auto_now_add=True)
	datamudanca = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.user);
 
#-----------------------------------------------------------------------------------------------
# CLASSE DE STORIES DE USUÁRIO MEMBRO
class Momentos(models.Model):
	user      = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE, verbose_name='Postado Por:')
	momento   = models.CharField(max_length=25,null=False,blank=False,verbose_name='TITULO DO MOMENTO. * 25 CARACTERES')
	img1      = models.ImageField(upload_to='media/stories', blank=False, verbose_name='IMAGEM 1')
	img2      = models.ImageField(upload_to='media/stories', blank=False, verbose_name='IMAGEM 2')
	CIDADE_RN_UF = [
    ('Acari','Acari'),
	('Afonso Bezerra', 'Afonso Bezerra'),
	('Agua Nova','Água Nova'),
	('Alexandria','Alexandria'),
	('Almino Afonso','Almino'),
	('Alto do Rodrigues','Alto do Rodrigues'),
	('Angicos','Angicos'),
	('Antônio Martins','Antônio Martins'),
	('Apodi','Apodi'),
	('Areia Branca','Areia Branca'),
	('Arez','Arez'),
	('Assu','Assu'),
	('Baia Formosa','Baía Formosa'),
	('Baraúna','Baraúna'),
	('Barcelona','Barcelona'),
	('Bento Fernandes','Bento Fernandes'),
	('Boa Saúde','Boa Saúde'),
	('Bodó','Bodó'),
	('Bom Jesus','Bom Jesus'),
	('Brejinho','Brejinho'),
	('Caicara do Norte','Caiçara do Norte'),
	('Caicara do Rio do Vento','Caiçara do Rio do Vento'),
	('Caicó','Caicó'),
	('Campo Grande','Campo Grande'),
	('Campo Redondo','Campo Redondo'),
	('Canguaretama','Canguaretama'),
	('Caraúbas','Caraúbas'),
	('Carnauba dos Dantas','Carnaúba dos Dantas'),
	('Carnaubais','Carnaubais'),
	('Ceará Mirim','Ceará-Mirim'),
	('Cerro corá','Cerro Corá'),
	('Coronel Ezequiel','Coronel Ezequiel'),
	('Coronel João Pessoa','Coronel João Pessoa'),
	('cruzeta','Cruzeta'),
	('Currais Novos','Currais Novos'),
	('Doutor Severiano','Doutor Severiano'),
	('Encanto','Encanto'),
	('Equador','Equador'),
	('Espirito Santo','Espírito Santo'),
	('Extremoz','Extremoz'),
	('Felipe Guerra','Felipe Guerra'),
	('Fernando Pedroza','Fernando Pedroza'),
	('Florãnia','Florânia'),
	('Francisco Dantas','Francisco Dantas'),
	('Frutuoso Gomes','Frutuoso Gomes'),
	('Galinhos','Galinhos'),
	('Goianinha','Goianinha'),
	('Governador Dix-sept Rosado','Governador Dix-Sept Rosado'),
	('Grossos','Grossos'),
	('Guamaré','Guamaré'),
	('Ielmo Marinho','Ielmo Marinho'),
	('Ipanguaçu','Ipanguaçu'),
	('Ipueira','Ipueira'),
	('Itajá','Itajá'),
	('Itaú','Itaú'),
	('Jaçanã','Jaçanã'),
	('Jandaíra','Jandaíra'),
	('Janduís','Janduís'),
	('Japi','Japi'),
	('Jardim de Angicos','Jardim de Angicos'),
	('Jardim de Piranhas','Jardim de Piranhas'),
	('Jardim do seridó','Jardim do Seridó'),
	('João Cãmara','João Câmara'),
	('João Dias','João Dias'),
	('José da Penha','José da Penha'),
	('Jucurutu','Jucurutu'),
	('Jundiá','Jundiá'),
	('Lagoa d´Anta','Lagoa dAnta'),
	('Lagoa de Pedras','Lagoa de Pedras'),
	('Lagoa de Velhos','Lagoa de Velhos'),
	('Lagoa Nova','Lagoa Nova'),
	('Lagoa Salgada','Lagoa Salgada'),
	('Lajes','Lajes'),
	('Lajes Pintadas','Lajes Pintadas'),
	('Lucrécia','Lucrécia'),
	('Luis Gomes','Luís Gomes'),
	('Macaiba','Macaíba'),
	('Macau','Macau'),
	('Major Sales','Major Sales'),
	('Marcelino Vieira','Marcelino Vieira'),
	('Martins','Martins'),
	('Maxaranguape','Maxaranguape'),
	('Messias Targino','Messias Targino'),
	('Montanhas','Montanhas'),
	('Monte Alegre','Monte Alegre'),
	('Monte das Gameleiras','Monte das Gameleiras'),
	('Mossoró','Mossoró'),
	('Natal','Natal'),
	('Nisia Floresta','Nísia Floresta'),
	('Nova Cruz','Nova Cruz'),
	('Olho d´Água doS Borges','Olho-dÁgua do Borges'),
	('Parana','Paraná'),
	('Parau','Paraú'),
	('Parazinho','Parazinho'),
	('Parelhas','Parelhas'),
	('Parnamirim','Parnamirim'),
	('Passa e Fica','Passa-e-Fica'),
	('Passagem','Passagem'),
	('Patu','Patu'),
	('Pau dos Ferros','Pau dos Ferros'),
	('Pedra Grande','Pedra Grande'),
	('Pedra Preta','Pedra Preta'),
	('Pedro Avelino','Pedro Avelino'),
	('Pedro Velho','Pedro Velho'),
	('Pendências','Pendências'),
	('Pilões','Pilões'),
	('Poço Branco','Poço Branco'),
	('Portalegre','Portalegre'),
	('Porto do Mangue','Porto do Mangue'),
	('Pureza','Pureza'),
	('Rafael Fernandes','Rafael Fernandes'),
	('Rafael Godeiro','Rafael Godeiro'),
	('Riacho da Cruz','Riacho da Cruz'),
	('Riacho de Santana','Riacho de Santana'),
	('Riachuelo','Riachuelo'),
	('Rio do Fogo','Rio do Fogo'),
	('Rodolfo Fernandes','Rodolfo Fernandes'),
	('Santa Cruz','Santa Cruz'),
	('Santa Maria','Santa Maria'),
	('Santana do Matos','Santana do Matos'),
	('Santana do Seridó','Santana do Seridó'),
	('Santo Antônio','Santo Antônio'),
	('São Bento do Norte','São Bento do Norte'),
	('São Bento do Trairi','São Bento do Trairi'),
	('São Fernando','São Fernando'),
	('São Francisco do Oeste','São Francisco do Oeste'),
	('São Gonçalo do Amarante','São Gonçalo do Amarante'),
	('São João do Sabugi','São João do Sabugi'),
	('São José de Mipibu','São José de Mipibu'),
	('São José do Campestre','São José do Campestre'),
	('São José do Seridó','São José do Seridó'),
	('São Miguel','São Miguel'),
	('São Miguel do Gostoso','São Miguel do Gostoso'),
	('São Paulo do Potengi','São Paulo do Potengi'),
	('São Pedro','São Pedro'),
	('São Rafael','São Rafael'),
	('São Tomé','São Tomé'),
	('Senador Elói de Souza','Senador Elói de Souza'),
	('senadorgeorginoavelino','Senador Georgino Avelino'),
	('Serra Caiada','Serra Caiada'),
	('Serra de São Bento','Serra de São Bento'),
	('Serra do Mel','Serra do Mel'),
	('Serra Negra do Norte','Serra Negra do Norte'),
	('Serrinha','Serrinha'),
	('Serrinha dos Pintos','Serrinha dos Pintos'),
	('Severiano Melo','Severiano Melo'),
	('Sitio Novo','Sítio Novo'),
	('Taboleiro Grande','Taboleiro Grande'),
	('Taipu','Taipu'),
	('Tangará','Tangará'),
	('Tenente Ananias','Tenente Ananias'),
	('Tenentel Laurentino Cruz','Tenente Laurentino Cruz'),
	('Tibau','Tibau'),
	('Tibau do Sul','Tibau do Sul'),
	('Timbaúba dos Batistas','Timbaúba dos Batistas'),
	('Touros','Touros'),
	('Triunfo Potiguar','Triunfo Potiguar'),
	('Umarizal','Umarizal'),
	('Upanema','Upanema'),
	('Várzea','Várzea'),
	('Venha-ver','Venha-Ver'),
	('Vera Cruz','Vera Cruz'),
	('Viçosa','Viçosa'),
	('Vila Flor','Vila Flor')
	]
	ESTADO_BR_UF = [
	('RN','RN')
	]
	ESCOLARIDADE = [
	('Ensino Fundamental','Ensino Fundamental'),
	('Ensino Médio','Ensino Médio'),
	('Ensino Superior','Ensino Superior'),
	('Outros','Outros')
	]
	cidade     = models.CharField(max_length=30,choices=CIDADE_RN_UF,verbose_name='ONDE FOI ?:')
	estado     = models.CharField(max_length=2,choices=ESTADO_BR_UF,null=False,blank=False,verbose_name='ESTADO-UF:')
	descrever  = models.TextField(max_length=100, verbose_name="DESCREVA: NO MÁXIMO 100 CARACTERES")
	visto      = models.IntegerField(default=0, null=True,blank=True)
	criacao    = models.DateTimeField(auto_now_add=True,verbose_name="DATA")
	update_cria= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.momento;
#------------------------------------------------------------------------------------------------

# CLASSE DO E-COMMERCE MARKTPLACE FORALL, COM UMA INSTÂNCIA DE UM SÓ ANÚNCIO
class Eccommence(models.Model):
	user          = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Postado por:')
	nome          = models.CharField(max_length=100,null=False,blank=True,verbose_name='NOME COMPLETO')
	titulo_produto= models.CharField(max_length=20,null=False,blank=True,verbose_name='DESCREVA EM 20 CARACTERES QUAL O NOME DO PRODUTO')
	CATEGORIA_PRODUTO = [
    ('CD','CD'),
	('Camisa','Camisa'),
	('Bottons','Bottons'),
	('Vinil','Vinil'),
	('Tênis','Tênis'),
	('Livro','Livro'),
	('DVD','DVD'),
	('Moleton','Moleton'),
	('Canecas','Canecas'),
	('Boné','Boné'),
	('Chaveiro','Chaveiro'),
	('Outros','Outros')
	]
	TIPO_TRANSACAO = [
	('Troca','Troca'),
	('Venda','Venda'),
	('Troca ou Venda','Troca ou Venda')
	]
	CARTAO = [
	('Sim','Sim'),
	('Não','Não'),
	('A combinar','A combinar')
	]
	ESTADO_PRODUTO = [
	('Novo','Novo'),
	('Usado','Usado')
	]
	ONDE_MORA = [
    ('Acari','Acari'),
	('Afonso Bezerra', 'Afonso Bezerra'),
	('Agua Nova','Água Nova'),
	('Alexandria','Alexandria'),
	('Almino Afonso','Almino'),
	('Alto do Rodrigues','Alto do Rodrigues'),
	('Angicos','Angicos'),
	('Antônio Martins','Antônio Martins'),
	('Apodi','Apodi'),
	('Areia Branca','Areia Branca'),
	('Arez','Arez'),
	('Assu','Assu'),
	('Baia Formosa','Baía Formosa'),
	('Baraúna','Baraúna'),
	('Barcelona','Barcelona'),
	('Bento Fernandes','Bento Fernandes'),
	('Boa Saúde','Boa Saúde'),
	('Bodó','Bodó'),
	('Bom Jesus','Bom Jesus'),
	('Brejinho','Brejinho'),
	('Caicara do Norte','Caiçara do Norte'),
	('Caicara do Rio do Vento','Caiçara do Rio do Vento'),
	('Caicó','Caicó'),
	('Campo Grande','Campo Grande'),
	('Campo Redondo','Campo Redondo'),
	('Canguaretama','Canguaretama'),
	('Caraúbas','Caraúbas'),
	('Carnauba dos Dantas','Carnaúba dos Dantas'),
	('Carnaubais','Carnaubais'),
	('Ceará Mirim','Ceará-Mirim'),
	('Cerro corá','Cerro Corá'),
	('Coronel Ezequiel','Coronel Ezequiel'),
	('Coronel João Pessoa','Coronel João Pessoa'),
	('cruzeta','Cruzeta'),
	('Currais Novos','Currais Novos'),
	('Doutor Severiano','Doutor Severiano'),
	('Encanto','Encanto'),
	('Equador','Equador'),
	('Espirito Santo','Espírito Santo'),
	('Extremoz','Extremoz'),
	('Felipe Guerra','Felipe Guerra'),
	('Fernando Pedroza','Fernando Pedroza'),
	('Florãnia','Florânia'),
	('Francisco Dantas','Francisco Dantas'),
	('Frutuoso Gomes','Frutuoso Gomes'),
	('Galinhos','Galinhos'),
	('Goianinha','Goianinha'),
	('Governador Dix-sept Rosado','Governador Dix-Sept Rosado'),
	('Grossos','Grossos'),
	('Guamaré','Guamaré'),
	('Ielmo Marinho','Ielmo Marinho'),
	('Ipanguaçu','Ipanguaçu'),
	('Ipueira','Ipueira'),
	('Itajá','Itajá'),
	('Itaú','Itaú'),
	('Jaçanã','Jaçanã'),
	('Jandaíra','Jandaíra'),
	('Janduís','Janduís'),
	('Japi','Japi'),
	('Jardim de Angicos','Jardim de Angicos'),
	('Jardim de Piranhas','Jardim de Piranhas'),
	('Jardim do seridó','Jardim do Seridó'),
	('João Cãmara','João Câmara'),
	('João Dias','João Dias'),
	('José da Penha','José da Penha'),
	('Jucurutu','Jucurutu'),
	('Jundiá','Jundiá'),
	('Lagoa d´Anta','Lagoa dAnta'),
	('Lagoa de Pedras','Lagoa de Pedras'),
	('Lagoa de Velhos','Lagoa de Velhos'),
	('Lagoa Nova','Lagoa Nova'),
	('Lagoa Salgada','Lagoa Salgada'),
	('Lajes','Lajes'),
	('Lajes Pintadas','Lajes Pintadas'),
	('Lucrécia','Lucrécia'),
	('Luis Gomes','Luís Gomes'),
	('Macaiba','Macaíba'),
	('Macau','Macau'),
	('Major Sales','Major Sales'),
	('Marcelino Vieira','Marcelino Vieira'),
	('Martins','Martins'),
	('Maxaranguape','Maxaranguape'),
	('Messias Targino','Messias Targino'),
	('Montanhas','Montanhas'),
	('Monte Alegre','Monte Alegre'),
	('Monte das Gameleiras','Monte das Gameleiras'),
	('Mossoró','Mossoró'),
	('Natal','Natal'),
	('Nisia Floresta','Nísia Floresta'),
	('Nova Cruz','Nova Cruz'),
	('Olho d´Água doS Borges','Olho-dÁgua do Borges'),
	('Parana','Paraná'),
	('Parau','Paraú'),
	('Parazinho','Parazinho'),
	('Parelhas','Parelhas'),
	('Parnamirim','Parnamirim'),
	('Passa e Fica','Passa-e-Fica'),
	('Passagem','Passagem'),
	('Patu','Patu'),
	('Pau dos Ferros','Pau dos Ferros'),
	('Pedra Grande','Pedra Grande'),
	('Pedra Preta','Pedra Preta'),
	('Pedro Avelino','Pedro Avelino'),
	('Pedro Velho','Pedro Velho'),
	('Pendências','Pendências'),
	('Pilões','Pilões'),
	('Poço Branco','Poço Branco'),
	('Portalegre','Portalegre'),
	('Porto do Mangue','Porto do Mangue'),
	('Pureza','Pureza'),
	('Rafael Fernandes','Rafael Fernandes'),
	('Rafael Godeiro','Rafael Godeiro'),
	('Riacho da Cruz','Riacho da Cruz'),
	('Riacho de Santana','Riacho de Santana'),
	('Riachuelo','Riachuelo'),
	('Rio do Fogo','Rio do Fogo'),
	('Rodolfo Fernandes','Rodolfo Fernandes'),
	('Santa Cruz','Santa Cruz'),
	('Santa Maria','Santa Maria'),
	('Santana do Matos','Santana do Matos'),
	('Santana do Seridó','Santana do Seridó'),
	('Santo Antônio','Santo Antônio'),
	('São Bento do Norte','São Bento do Norte'),
	('São Bento do Trairi','São Bento do Trairi'),
	('São Fernando','São Fernando'),
	('São Francisco do Oeste','São Francisco do Oeste'),
	('São Gonçalo do Amarante','São Gonçalo do Amarante'),
	('São João do Sabugi','São João do Sabugi'),
	('São José de Mipibu','São José de Mipibu'),
	('São José do Campestre','São José do Campestre'),
	('São José do Seridó','São José do Seridó'),
	('São Miguel','São Miguel'),
	('São Miguel do Gostoso','São Miguel do Gostoso'),
	('São Paulo do Potengi','São Paulo do Potengi'),
	('São Pedro','São Pedro'),
	('São Rafael','São Rafael'),
	('São Tomé','São Tomé'),
	('Senador Elói de Souza','Senador Elói de Souza'),
	('senadorgeorginoavelino','Senador Georgino Avelino'),
	('Serra Caiada','Serra Caiada'),
	('Serra de São Bento','Serra de São Bento'),
	('Serra do Mel','Serra do Mel'),
	('Serra Negra do Norte','Serra Negra do Norte'),
	('Serrinha','Serrinha'),
	('Serrinha dos Pintos','Serrinha dos Pintos'),
	('Severiano Melo','Severiano Melo'),
	('Sitio Novo','Sítio Novo'),
	('Taboleiro Grande','Taboleiro Grande'),
	('Taipu','Taipu'),
	('Tangará','Tangará'),
	('Tenente Ananias','Tenente Ananias'),
	('Tenentel Laurentino Cruz','Tenente Laurentino Cruz'),
	('Tibau','Tibau'),
	('Tibau do Sul','Tibau do Sul'),
	('Timbaúba dos Batistas','Timbaúba dos Batistas'),
	('Touros','Touros'),
	('Triunfo Potiguar','Triunfo Potiguar'),
	('Umarizal','Umarizal'),
	('Upanema','Upanema'),
	('Várzea','Várzea'),
	('Venha-ver','Venha-Ver'),
	('Vera Cruz','Vera Cruz'),
	('Viçosa','Viçosa'),
	('Vila Flor','Vila Flor')
	]
	ESTADOBR = [
	('RN','RN')
	]
	categori_produto = models.CharField(max_length=100,choices=CATEGORIA_PRODUTO,null=False,blank=False,verbose_name='CATEGORIA')
	tipo_transacao   = models.CharField(max_length=100,choices=TIPO_TRANSACAO,null=False,blank=False, verbose_name='TIPO DE TRANSAÇÃO ?')
	cidade_mora      = models.CharField(max_length=100,choices=ONDE_MORA,null=False,blank=False,verbose_name='ONDE VOCÊ MORA ?')
	estado_mora      = models.CharField(max_length=30,choices=ESTADOBR,	null=False,blank=False,verbose_name='ESTADO-UF')
	cartao           = models.CharField(max_length=12,choices=CARTAO,null=False,blank=False,verbose_name='CARTÃO, DEPENDE DA TRANSAÇÃO:' )
	estado_produto   = models.CharField(max_length=32,choices=ESTADO_PRODUTO,null=False,blank=True,verbose_name='COMO ESTA O PRODUTO ?')
	preco_produto    = models.FloatField(max_length=10,null=True,blank=True,verbose_name='PREÇO DO PRODUTO, * OPCIONAL SE FOR VENDA. EX: 99.99')
	contato          = models.CharField(max_length=13,null=False,blank=False,verbose_name='CONTATO(WhatsApp), FORMATO 5584XXXXXXXXX')
	image_produto    = models.ImageField(upload_to='media/Eccommence', blank=False, verbose_name='IMAGE DO PRODUTO. TAMANHO RECOMENDADO EX: 200 X 200:')
	descrever_produto= models.TextField(verbose_name='DESCREVA UM DETALHES SOBRE O PRODUTO AO QUAL ESTA DEVENDO OU TROCANCO .....')
	view_produto     = models.IntegerField(default=0, null=True,blank=True)
	produto_criado   = models.DateTimeField(auto_now_add=True,verbose_name='DATA')
	alteracao_produto= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.titulo_produto;
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++		
	
# CLASSE DE FRASES DO USUÁRIO
class Pensamento(models.Model):
	user      = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Postado por:')
	ideia     = models.TextField(null=False,blank=True, verbose_name='O que você esta pensando ? Post suas idéias.')
	foiCriado = models.DateTimeField(auto_now_add=True,verbose_name='CRIADO')
	modificado= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.ideia;
#------------------------------------------------------------------------
# CLASSE NÃO USADA NO MOMENTO
class Comente(models.Model):
	postagem = models.ForeignKey(Postagem,null=True,blank=True,on_delete=models.CASCADE)
	nome     = models.CharField(max_length=100)
	corpo    = models.TextField()
	adicionado = models.DateTimeField()

	def __str__(self):
		return '%s - %s' % (self.postagem.titulo, self.nome);

#------------------------------------------------------------------------

# CLASSE DA LOJA PRIVADA DO FORALL
class Loja(models.Model):
	dono              = models.CharField(max_length=100,null=False,blank=False)
	produto_nome      = models.CharField(max_length=100,null=False,blank=False)
	produto_image     = models.ImageField(upload_to='media/Loja', blank=False)
	preco_produto     = models.FloatField(max_length=10,null=False,blank=True)
	descricao         = models.TextField()
	cod_produto       = models.CharField(max_length=100)
	contato_principal = models.CharField(max_length=14)
	contato_secundario= models.CharField(max_length=14,blank=True,null=True)
	criando           = models.DateTimeField(auto_now_add=True)
	atualizado        = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.produto_nome;

	def delete(self, *args, **kwargs):
		if os.path.isfile(self.produto_image.path):
			os.remove(self.produto_image.path)
		super(Loja, self).delete(*args, **kwargs)

#------------------------------------------------------------------------

# CLASSE DE COMENTÁRIOS DE POSTS DE USUÁRIO LOGADOS
class ComentaPosts(models.Model):
	user        = models.ForeignKey(User, on_delete=models.CASCADE)
	postagem    = models.ForeignKey(Postagem, on_delete=models.CASCADE)
	data_comenta= models.DateTimeField(auto_now_add=True)
	comentarios = models.TextField(max_length=50,verbose_name="MENOS DE 20 CARACTERES:")
	RATE_CHOICES = [
	(1,'1 - Gostei'),
	(2,'2 - Não gostei'),
	(3,'3 - Boa dica'),
	(4,'4 - Dica ruim'),
	]
	opniao      = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
	like        = models.PositiveSmallIntegerField(default=0)
	deslike     = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.user.username;
#-------------------------------------------------------------------------

# CLASSE DE POSTAGEM DE UMA PLAYLIST SPOTIFY
class Spotify(models.Model):
	video     = models.CharField(max_length=200,verbose_name='LINK DA SUA PLAYLIST DO SPOTIFY')
	user      = models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE, verbose_name='Postado Por:')
	criadoEm  = models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')
	mudadoem  = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.user.username;
#-------------------------------------------------------------------------
# CLASSE E-COMMERCE MARKTPLACE FORALL PARA USUÁRIOS PREMIUM
class LojaPremium(models.Model):
	user          = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Postado por:')
	nome          = models.CharField(max_length=100,null=False,blank=True,verbose_name='NOME COMPLETO')
	nome_produto  = models.CharField(max_length=30,null=False,blank=True,verbose_name='DESCREVA EM 30 CARACTERES QUAL O NOME DO PRODUTO')
	CATEGORIA_PRODUTO = [
    ('CD','CD'),
	('Camisa','Camisa'),
	('Bottons','Bottons'),
	('Vinil','Vinil'),
	('Tênis','Tênis'),
	('Livro','Livro'),
	('DVD','DVD'),
	('Moleton','Moleton'),
	('Canecas','Canecas'),
	('Boné','Boné'),
	('Chaveiro','Chaveiro'),
	('Celulares','Celulares'),
	('Tvs','Tvs'),
	('Moveis','Moveis'),
	('Outros','Outros')
	]
	TIPO_TRANSACAO = [
	('Troca','Troca'),
	('Venda','Venda'),
	('Troca ou Venda','Troca ou Venda')
	]
	CARTAO = [
	('Sim','Sim'),
	('Não','Não'),
	('A combinar','A combinar')
	]
	ESTADO_PRODUTO = [
	('Novo','Novo'),
	('Usado','Usado')
	]
	ONDE_MORA = [
    ('Acari','Acari'),
	('Afonso Bezerra', 'Afonso Bezerra'),
	('Agua Nova','Água Nova'),
	('Alexandria','Alexandria'),
	('Almino Afonso','Almino'),
	('Alto do Rodrigues','Alto do Rodrigues'),
	('Angicos','Angicos'),
	('Antônio Martins','Antônio Martins'),
	('Apodi','Apodi'),
	('Areia Branca','Areia Branca'),
	('Arez','Arez'),
	('Assu','Assu'),
	('Baia Formosa','Baía Formosa'),
	('Baraúna','Baraúna'),
	('Barcelona','Barcelona'),
	('Bento Fernandes','Bento Fernandes'),
	('Boa Saúde','Boa Saúde'),
	('Bodó','Bodó'),
	('Bom Jesus','Bom Jesus'),
	('Brejinho','Brejinho'),
	('Caicara do Norte','Caiçara do Norte'),
	('Caicara do Rio do Vento','Caiçara do Rio do Vento'),
	('Caicó','Caicó'),
	('Campo Grande','Campo Grande'),
	('Campo Redondo','Campo Redondo'),
	('Canguaretama','Canguaretama'),
	('Caraúbas','Caraúbas'),
	('Carnauba dos Dantas','Carnaúba dos Dantas'),
	('Carnaubais','Carnaubais'),
	('Ceará Mirim','Ceará-Mirim'),
	('Cerro corá','Cerro Corá'),
	('Coronel Ezequiel','Coronel Ezequiel'),
	('Coronel João Pessoa','Coronel João Pessoa'),
	('cruzeta','Cruzeta'),
	('Currais Novos','Currais Novos'),
	('Doutor Severiano','Doutor Severiano'),
	('Encanto','Encanto'),
	('Equador','Equador'),
	('Espirito Santo','Espírito Santo'),
	('Extremoz','Extremoz'),
	('Felipe Guerra','Felipe Guerra'),
	('Fernando Pedroza','Fernando Pedroza'),
	('Florãnia','Florânia'),
	('Francisco Dantas','Francisco Dantas'),
	('Frutuoso Gomes','Frutuoso Gomes'),
	('Galinhos','Galinhos'),
	('Goianinha','Goianinha'),
	('Governador Dix-sept Rosado','Governador Dix-Sept Rosado'),
	('Grossos','Grossos'),
	('Guamaré','Guamaré'),
	('Ielmo Marinho','Ielmo Marinho'),
	('Ipanguaçu','Ipanguaçu'),
	('Ipueira','Ipueira'),
	('Itajá','Itajá'),
	('Itaú','Itaú'),
	('Jaçanã','Jaçanã'),
	('Jandaíra','Jandaíra'),
	('Janduís','Janduís'),
	('Japi','Japi'),
	('Jardim de Angicos','Jardim de Angicos'),
	('Jardim de Piranhas','Jardim de Piranhas'),
	('Jardim do seridó','Jardim do Seridó'),
	('João Cãmara','João Câmara'),
	('João Dias','João Dias'),
	('José da Penha','José da Penha'),
	('Jucurutu','Jucurutu'),
	('Jundiá','Jundiá'),
	('Lagoa d´Anta','Lagoa dAnta'),
	('Lagoa de Pedras','Lagoa de Pedras'),
	('Lagoa de Velhos','Lagoa de Velhos'),
	('Lagoa Nova','Lagoa Nova'),
	('Lagoa Salgada','Lagoa Salgada'),
	('Lajes','Lajes'),
	('Lajes Pintadas','Lajes Pintadas'),
	('Lucrécia','Lucrécia'),
	('Luis Gomes','Luís Gomes'),
	('Macaiba','Macaíba'),
	('Macau','Macau'),
	('Major Sales','Major Sales'),
	('Marcelino Vieira','Marcelino Vieira'),
	('Martins','Martins'),
	('Maxaranguape','Maxaranguape'),
	('Messias Targino','Messias Targino'),
	('Montanhas','Montanhas'),
	('Monte Alegre','Monte Alegre'),
	('Monte das Gameleiras','Monte das Gameleiras'),
	('Mossoró','Mossoró'),
	('Natal','Natal'),
	('Nisia Floresta','Nísia Floresta'),
	('Nova Cruz','Nova Cruz'),
	('Olho d´Água doS Borges','Olho-dÁgua do Borges'),
	('Parana','Paraná'),
	('Parau','Paraú'),
	('Parazinho','Parazinho'),
	('Parelhas','Parelhas'),
	('Parnamirim','Parnamirim'),
	('Passa e Fica','Passa-e-Fica'),
	('Passagem','Passagem'),
	('Patu','Patu'),
	('Pau dos Ferros','Pau dos Ferros'),
	('Pedra Grande','Pedra Grande'),
	('Pedra Preta','Pedra Preta'),
	('Pedro Avelino','Pedro Avelino'),
	('Pedro Velho','Pedro Velho'),
	('Pendências','Pendências'),
	('Pilões','Pilões'),
	('Poço Branco','Poço Branco'),
	('Portalegre','Portalegre'),
	('Porto do Mangue','Porto do Mangue'),
	('Pureza','Pureza'),
	('Rafael Fernandes','Rafael Fernandes'),
	('Rafael Godeiro','Rafael Godeiro'),
	('Riacho da Cruz','Riacho da Cruz'),
	('Riacho de Santana','Riacho de Santana'),
	('Riachuelo','Riachuelo'),
	('Rio do Fogo','Rio do Fogo'),
	('Rodolfo Fernandes','Rodolfo Fernandes'),
	('Santa Cruz','Santa Cruz'),
	('Santa Maria','Santa Maria'),
	('Santana do Matos','Santana do Matos'),
	('Santana do Seridó','Santana do Seridó'),
	('Santo Antônio','Santo Antônio'),
	('São Bento do Norte','São Bento do Norte'),
	('São Bento do Trairi','São Bento do Trairi'),
	('São Fernando','São Fernando'),
	('São Francisco do Oeste','São Francisco do Oeste'),
	('São Gonçalo do Amarante','São Gonçalo do Amarante'),
	('São João do Sabugi','São João do Sabugi'),
	('São José de Mipibu','São José de Mipibu'),
	('São José do Campestre','São José do Campestre'),
	('São José do Seridó','São José do Seridó'),
	('São Miguel','São Miguel'),
	('São Miguel do Gostoso','São Miguel do Gostoso'),
	('São Paulo do Potengi','São Paulo do Potengi'),
	('São Pedro','São Pedro'),
	('São Rafael','São Rafael'),
	('São Tomé','São Tomé'),
	('Senador Elói de Souza','Senador Elói de Souza'),
	('senadorgeorginoavelino','Senador Georgino Avelino'),
	('Serra Caiada','Serra Caiada'),
	('Serra de São Bento','Serra de São Bento'),
	('Serra do Mel','Serra do Mel'),
	('Serra Negra do Norte','Serra Negra do Norte'),
	('Serrinha','Serrinha'),
	('Serrinha dos Pintos','Serrinha dos Pintos'),
	('Severiano Melo','Severiano Melo'),
	('Sitio Novo','Sítio Novo'),
	('Taboleiro Grande','Taboleiro Grande'),
	('Taipu','Taipu'),
	('Tangará','Tangará'),
	('Tenente Ananias','Tenente Ananias'),
	('Tenentel Laurentino Cruz','Tenente Laurentino Cruz'),
	('Tibau','Tibau'),
	('Tibau do Sul','Tibau do Sul'),
	('Timbaúba dos Batistas','Timbaúba dos Batistas'),
	('Touros','Touros'),
	('Triunfo Potiguar','Triunfo Potiguar'),
	('Umarizal','Umarizal'),
	('Upanema','Upanema'),
	('Várzea','Várzea'),
	('Venha-ver','Venha-Ver'),
	('Vera Cruz','Vera Cruz'),
	('Viçosa','Viçosa'),
	('Vila Flor','Vila Flor')
	]
	ESTADOBR = [
	('RN','RN')
	] 
	categori_produto = models.CharField(max_length=100,choices=CATEGORIA_PRODUTO,null=False,blank=False,verbose_name='CATEGORIA')
	tipo_transacao   = models.CharField(max_length=100,choices=TIPO_TRANSACAO,null=False,blank=False, verbose_name='TIPO DE TRANSAÇÃO ?')
	cidade_mora      = models.CharField(max_length=100,choices=ONDE_MORA,null=False,blank=False,verbose_name='ONDE VOCÊ MORA ?')
	estado_mora      = models.CharField(max_length=30,choices=ESTADOBR,	null=False,blank=False,verbose_name='ESTADO-UF')
	cartao           = models.CharField(max_length=12,choices=CARTAO,null=False,blank=False,verbose_name='CARTÃO, DEPENDE DA TRANSAÇÃO:' )
	estado_produto   = models.CharField(max_length=32,choices=ESTADO_PRODUTO,null=False,blank=True,verbose_name='COMO ESTA O PRODUTO ?')
	preco_produto    = models.FloatField(max_length=10,null=True,blank=True,verbose_name='PREÇO DO PRODUTO, * OPCIONAL SE FOR VENDA. EX: 99.99')
	contato          = models.CharField(max_length=13,null=False,blank=False,verbose_name='CONTATO(WhatsApp), FORMATO 5584XXXXXXXXX')
	image_produto    = models.ImageField(upload_to='media/LojaPremium', blank=False, verbose_name='IMAGE DO PRODUTO. TAMANHO RECOMENDADO EX: 200 X 200:')
	descrever_produto= models.TextField(verbose_name='DESCREVA UM DETALHES SOBRE O PRODUTO AO QUAL ESTA DEVENDO OU TROCANCO .....')
	view_produto     = models.IntegerField(default=0, null=True,blank=True)
	produto_criado   = models.DateTimeField(auto_now_add=True,verbose_name='DATA')
	alteracao_produto= models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return self.nome;
#---------------------------------------------------------------------------------------
# CLASSE DE PEDIDO DE INSCRIÇÃO PARA SER USUÁRIO PREMIUM NO MARKETPLACE FORALL
class IncricaoPremium(models.Model):
	MINHA_CIDADE = [
    ('Acari','Acari'),
	('Afonso Bezerra', 'Afonso Bezerra'),
	('Agua Nova','Água Nova'),
	('Alexandria','Alexandria'),
	('Almino Afonso','Almino'),
	('Alto do Rodrigues','Alto do Rodrigues'),
	('Angicos','Angicos'),
	('Antônio Martins','Antônio Martins'),
	('Apodi','Apodi'),
	('Areia Branca','Areia Branca'),
	('Arez','Arez'),
	('Assu','Assu'),
	('Baia Formosa','Baía Formosa'),
	('Baraúna','Baraúna'),
	('Barcelona','Barcelona'),
	('Bento Fernandes','Bento Fernandes'),
	('Boa Saúde','Boa Saúde'),
	('Bodó','Bodó'),
	('Bom Jesus','Bom Jesus'),
	('Brejinho','Brejinho'),
	('Caicara do Norte','Caiçara do Norte'),
	('Caicara do Rio do Vento','Caiçara do Rio do Vento'),
	('Caicó','Caicó'),
	('Campo Grande','Campo Grande'),
	('Campo Redondo','Campo Redondo'),
	('Canguaretama','Canguaretama'),
	('Caraúbas','Caraúbas'),
	('Carnauba dos Dantas','Carnaúba dos Dantas'),
	('Carnaubais','Carnaubais'),
	('Ceará Mirim','Ceará-Mirim'),
	('Cerro corá','Cerro Corá'),
	('Coronel Ezequiel','Coronel Ezequiel'),
	('Coronel João Pessoa','Coronel João Pessoa'),
	('cruzeta','Cruzeta'),
	('Currais Novos','Currais Novos'),
	('Doutor Severiano','Doutor Severiano'),
	('Encanto','Encanto'),
	('Equador','Equador'),
	('Espirito Santo','Espírito Santo'),
	('Extremoz','Extremoz'),
	('Felipe Guerra','Felipe Guerra'),
	('Fernando Pedroza','Fernando Pedroza'),
	('Florãnia','Florânia'),
	('Francisco Dantas','Francisco Dantas'),
	('Frutuoso Gomes','Frutuoso Gomes'),
	('Galinhos','Galinhos'),
	('Goianinha','Goianinha'),
	('Governador Dix-sept Rosado','Governador Dix-Sept Rosado'),
	('Grossos','Grossos'),
	('Guamaré','Guamaré'),
	('Ielmo Marinho','Ielmo Marinho'),
	('Ipanguaçu','Ipanguaçu'),
	('Ipueira','Ipueira'),
	('Itajá','Itajá'),
	('Itaú','Itaú'),
	('Jaçanã','Jaçanã'),
	('Jandaíra','Jandaíra'),
	('Janduís','Janduís'),
	('Japi','Japi'),
	('Jardim de Angicos','Jardim de Angicos'),
	('Jardim de Piranhas','Jardim de Piranhas'),
	('Jardim do seridó','Jardim do Seridó'),
	('João Cãmara','João Câmara'),
	('João Dias','João Dias'),
	('José da Penha','José da Penha'),
	('Jucurutu','Jucurutu'),
	('Jundiá','Jundiá'),
	('Lagoa d´Anta','Lagoa dAnta'),
	('Lagoa de Pedras','Lagoa de Pedras'),
	('Lagoa de Velhos','Lagoa de Velhos'),
	('Lagoa Nova','Lagoa Nova'),
	('Lagoa Salgada','Lagoa Salgada'),
	('Lajes','Lajes'),
	('Lajes Pintadas','Lajes Pintadas'),
	('Lucrécia','Lucrécia'),
	('Luis Gomes','Luís Gomes'),
	('Macaiba','Macaíba'),
	('Macau','Macau'),
	('Major Sales','Major Sales'),
	('Marcelino Vieira','Marcelino Vieira'),
	('Martins','Martins'),
	('Maxaranguape','Maxaranguape'),
	('Messias Targino','Messias Targino'),
	('Montanhas','Montanhas'),
	('Monte Alegre','Monte Alegre'),
	('Monte das Gameleiras','Monte das Gameleiras'),
	('Mossoró','Mossoró'),
	('Natal','Natal'),
	('Nisia Floresta','Nísia Floresta'),
	('Nova Cruz','Nova Cruz'),
	('Olho d´Água doS Borges','Olho-dÁgua do Borges'),
	('Parana','Paraná'),
	('Parau','Paraú'),
	('Parazinho','Parazinho'),
	('Parelhas','Parelhas'),
	('Parnamirim','Parnamirim'),
	('Passa e Fica','Passa-e-Fica'),
	('Passagem','Passagem'),
	('Patu','Patu'),
	('Pau dos Ferros','Pau dos Ferros'),
	('Pedra Grande','Pedra Grande'),
	('Pedra Preta','Pedra Preta'),
	('Pedro Avelino','Pedro Avelino'),
	('Pedro Velho','Pedro Velho'),
	('Pendências','Pendências'),
	('Pilões','Pilões'),
	('Poço Branco','Poço Branco'),
	('Portalegre','Portalegre'),
	('Porto do Mangue','Porto do Mangue'),
	('Pureza','Pureza'),
	('Rafael Fernandes','Rafael Fernandes'),
	('Rafael Godeiro','Rafael Godeiro'),
	('Riacho da Cruz','Riacho da Cruz'),
	('Riacho de Santana','Riacho de Santana'),
	('Riachuelo','Riachuelo'),
	('Rio do Fogo','Rio do Fogo'),
	('Rodolfo Fernandes','Rodolfo Fernandes'),
	('Santa Cruz','Santa Cruz'),
	('Santa Maria','Santa Maria'),
	('Santana do Matos','Santana do Matos'),
	('Santana do Seridó','Santana do Seridó'),
	('Santo Antônio','Santo Antônio'),
	('São Bento do Norte','São Bento do Norte'),
	('São Bento do Trairi','São Bento do Trairi'),
	('São Fernando','São Fernando'),
	('São Francisco do Oeste','São Francisco do Oeste'),
	('São Gonçalo do Amarante','São Gonçalo do Amarante'),
	('São João do Sabugi','São João do Sabugi'),
	('São José de Mipibu','São José de Mipibu'),
	('São José do Campestre','São José do Campestre'),
	('São José do Seridó','São José do Seridó'),
	('São Miguel','São Miguel'),
	('São Miguel do Gostoso','São Miguel do Gostoso'),
	('São Paulo do Potengi','São Paulo do Potengi'),
	('São Pedro','São Pedro'),
	('São Rafael','São Rafael'),
	('São Tomé','São Tomé'),
	('Senador Elói de Souza','Senador Elói de Souza'),
	('senadorgeorginoavelino','Senador Georgino Avelino'),
	('Serra Caiada','Serra Caiada'),
	('Serra de São Bento','Serra de São Bento'),
	('Serra do Mel','Serra do Mel'),
	('Serra Negra do Norte','Serra Negra do Norte'),
	('Serrinha','Serrinha'),
	('Serrinha dos Pintos','Serrinha dos Pintos'),
	('Severiano Melo','Severiano Melo'),
	('Sitio Novo','Sítio Novo'),
	('Taboleiro Grande','Taboleiro Grande'),
	('Taipu','Taipu'),
	('Tangará','Tangará'),
	('Tenente Ananias','Tenente Ananias'),
	('Tenentel Laurentino Cruz','Tenente Laurentino Cruz'),
	('Tibau','Tibau'),
	('Tibau do Sul','Tibau do Sul'),
	('Timbaúba dos Batistas','Timbaúba dos Batistas'),
	('Touros','Touros'),
	('Triunfo Potiguar','Triunfo Potiguar'),
	('Umarizal','Umarizal'),
	('Upanema','Upanema'),
	('Várzea','Várzea'),
	('Venha-ver','Venha-Ver'),
	('Vera Cruz','Vera Cruz'),
	('Viçosa','Viçosa'),
	('Vila Flor','Vila Flor')
	]
	ESTADORN = [
	('RN','RN')
	]
	TERMOS = [
	('SIM','SIM'),
	('NÃO','NÃO')
	]
	user         = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Postado por:')
	nomeCompleto = models.CharField(max_length=100,null=False,blank=False,verbose_name="Nome completo:")
	email        = models.CharField(max_length=100,null=False,blank=False,verbose_name="Email: * Este Email servirá para a liberação de meio de pagamento, e confirmação:")
	cidade       = models.CharField(max_length=100,null=False,blank=False,choices=MINHA_CIDADE,verbose_name="Cidade:")
	meuEstado    = models.CharField(max_length=3,null=False,blank=False,choices=ESTADORN,verbose_name="Estado:")
	termos       = models.CharField(max_length=3,null=False,blank=False,choices=TERMOS,verbose_name="Li o termo:")
	linkPagamento = models.CharField(max_length=200,null=False,blank=False)
	ativado      = models.BooleanField(default=False,null=False,blank=False)
	dataDaPulicacao = models.DateTimeField(auto_now_add=True,verbose_name="Data da incrição:")
	update       = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s | %s' % (self.nomeCompleto, self.email);
#-----------------------------------------------------------------------------------------------

# CLASSE DE PARCEIROS COMERCIAIS DO FORALL
class Parceiros(models.Model):
	EMPRESA_CIDADE = [
    ('Acari','Acari'),
	('Afonso Bezerra', 'Afonso Bezerra'),
	('Agua Nova','Água Nova'),
	('Alexandria','Alexandria'),
	('Almino Afonso','Almino'),
	('Alto do Rodrigues','Alto do Rodrigues'),
	('Angicos','Angicos'),
	('Antônio Martins','Antônio Martins'),
	('Apodi','Apodi'),
	('Areia Branca','Areia Branca'),
	('Arez','Arez'),
	('Assu','Assu'),
	('Baia Formosa','Baía Formosa'),
	('Baraúna','Baraúna'),
	('Barcelona','Barcelona'),
	('Bento Fernandes','Bento Fernandes'),
	('Boa Saúde','Boa Saúde'),
	('Bodó','Bodó'),
	('Bom Jesus','Bom Jesus'),
	('Brejinho','Brejinho'),
	('Caicara do Norte','Caiçara do Norte'),
	('Caicara do Rio do Vento','Caiçara do Rio do Vento'),
	('Caicó','Caicó'),
	('Campo Grande','Campo Grande'),
	('Campo Redondo','Campo Redondo'),
	('Canguaretama','Canguaretama'),
	('Caraúbas','Caraúbas'),
	('Carnauba dos Dantas','Carnaúba dos Dantas'),
	('Carnaubais','Carnaubais'),
	('Ceará Mirim','Ceará-Mirim'),
	('Cerro corá','Cerro Corá'),
	('Coronel Ezequiel','Coronel Ezequiel'),
	('Coronel João Pessoa','Coronel João Pessoa'),
	('cruzeta','Cruzeta'),
	('Currais Novos','Currais Novos'),
	('Doutor Severiano','Doutor Severiano'),
	('Encanto','Encanto'),
	('Equador','Equador'),
	('Espirito Santo','Espírito Santo'),
	('Extremoz','Extremoz'),
	('Felipe Guerra','Felipe Guerra'),
	('Fernando Pedroza','Fernando Pedroza'),
	('Florãnia','Florânia'),
	('Francisco Dantas','Francisco Dantas'),
	('Frutuoso Gomes','Frutuoso Gomes'),
	('Galinhos','Galinhos'),
	('Goianinha','Goianinha'),
	('Governador Dix-sept Rosado','Governador Dix-Sept Rosado'),
	('Grossos','Grossos'),
	('Guamaré','Guamaré'),
	('Ielmo Marinho','Ielmo Marinho'),
	('Ipanguaçu','Ipanguaçu'),
	('Ipueira','Ipueira'),
	('Itajá','Itajá'),
	('Itaú','Itaú'),
	('Jaçanã','Jaçanã'),
	('Jandaíra','Jandaíra'),
	('Janduís','Janduís'),
	('Japi','Japi'),
	('Jardim de Angicos','Jardim de Angicos'),
	('Jardim de Piranhas','Jardim de Piranhas'),
	('Jardim do seridó','Jardim do Seridó'),
	('João Cãmara','João Câmara'),
	('João Dias','João Dias'),
	('José da Penha','José da Penha'),
	('Jucurutu','Jucurutu'),
	('Jundiá','Jundiá'),
	('Lagoa d´Anta','Lagoa dAnta'),
	('Lagoa de Pedras','Lagoa de Pedras'),
	('Lagoa de Velhos','Lagoa de Velhos'),
	('Lagoa Nova','Lagoa Nova'),
	('Lagoa Salgada','Lagoa Salgada'),
	('Lajes','Lajes'),
	('Lajes Pintadas','Lajes Pintadas'),
	('Lucrécia','Lucrécia'),
	('Luis Gomes','Luís Gomes'),
	('Macaiba','Macaíba'),
	('Macau','Macau'),
	('Major Sales','Major Sales'),
	('Marcelino Vieira','Marcelino Vieira'),
	('Martins','Martins'),
	('Maxaranguape','Maxaranguape'),
	('Messias Targino','Messias Targino'),
	('Montanhas','Montanhas'),
	('Monte Alegre','Monte Alegre'),
	('Monte das Gameleiras','Monte das Gameleiras'),
	('Mossoró','Mossoró'),
	('Natal','Natal'),
	('Nisia Floresta','Nísia Floresta'),
	('Nova Cruz','Nova Cruz'),
	('Olho d´Água doS Borges','Olho-dÁgua do Borges'),
	('Parana','Paraná'),
	('Parau','Paraú'),
	('Parazinho','Parazinho'),
	('Parelhas','Parelhas'),
	('Parnamirim','Parnamirim'),
	('Passa e Fica','Passa-e-Fica'),
	('Passagem','Passagem'),
	('Patu','Patu'),
	('Pau dos Ferros','Pau dos Ferros'),
	('Pedra Grande','Pedra Grande'),
	('Pedra Preta','Pedra Preta'),
	('Pedro Avelino','Pedro Avelino'),
	('Pedro Velho','Pedro Velho'),
	('Pendências','Pendências'),
	('Pilões','Pilões'),
	('Poço Branco','Poço Branco'),
	('Portalegre','Portalegre'),
	('Porto do Mangue','Porto do Mangue'),
	('Pureza','Pureza'),
	('Rafael Fernandes','Rafael Fernandes'),
	('Rafael Godeiro','Rafael Godeiro'),
	('Riacho da Cruz','Riacho da Cruz'),
	('Riacho de Santana','Riacho de Santana'),
	('Riachuelo','Riachuelo'),
	('Rio do Fogo','Rio do Fogo'),
	('Rodolfo Fernandes','Rodolfo Fernandes'),
	('Santa Cruz','Santa Cruz'),
	('Santa Maria','Santa Maria'),
	('Santana do Matos','Santana do Matos'),
	('Santana do Seridó','Santana do Seridó'),
	('Santo Antônio','Santo Antônio'),
	('São Bento do Norte','São Bento do Norte'),
	('São Bento do Trairi','São Bento do Trairi'),
	('São Fernando','São Fernando'),
	('São Francisco do Oeste','São Francisco do Oeste'),
	('São Gonçalo do Amarante','São Gonçalo do Amarante'),
	('São João do Sabugi','São João do Sabugi'),
	('São José de Mipibu','São José de Mipibu'),
	('São José do Campestre','São José do Campestre'),
	('São José do Seridó','São José do Seridó'),
	('São Miguel','São Miguel'),
	('São Miguel do Gostoso','São Miguel do Gostoso'),
	('São Paulo do Potengi','São Paulo do Potengi'),
	('São Pedro','São Pedro'),
	('São Rafael','São Rafael'),
	('São Tomé','São Tomé'),
	('Senador Elói de Souza','Senador Elói de Souza'),
	('senadorgeorginoavelino','Senador Georgino Avelino'),
	('Serra Caiada','Serra Caiada'),
	('Serra de São Bento','Serra de São Bento'),
	('Serra do Mel','Serra do Mel'),
	('Serra Negra do Norte','Serra Negra do Norte'),
	('Serrinha','Serrinha'),
	('Serrinha dos Pintos','Serrinha dos Pintos'),
	('Severiano Melo','Severiano Melo'),
	('Sitio Novo','Sítio Novo'),
	('Taboleiro Grande','Taboleiro Grande'),
	('Taipu','Taipu'),
	('Tangará','Tangará'),
	('Tenente Ananias','Tenente Ananias'),
	('Tenentel Laurentino Cruz','Tenente Laurentino Cruz'),
	('Tibau','Tibau'),
	('Tibau do Sul','Tibau do Sul'),
	('Timbaúba dos Batistas','Timbaúba dos Batistas'),
	('Touros','Touros'),
	('Triunfo Potiguar','Triunfo Potiguar'),
	('Umarizal','Umarizal'),
	('Upanema','Upanema'),
	('Várzea','Várzea'),
	('Venha-ver','Venha-Ver'),
	('Vera Cruz','Vera Cruz'),
	('Viçosa','Viçosa'),
	('Vila Flor','Vila Flor')
	]
	ESTADO_RN = [
	('RN','RN')
	]
	DIA_SEMANA = [
	('Segunda a Sexta','Segunda a Sexta',),
	('Segunda a Sabádo','Segunda a Sabádo'),
	('Segunda a Domingo','Segunda a Domingo')
	]
	dono         = models.CharField(max_length=100,null=False,blank=False,verbose_name="Dono da empresa:")
	nomeLoja     = models.CharField(max_length=100,null=False,blank=False,verbose_name="Nome da Empresa(Loja):")
	ramo 	     = models.CharField(max_length=100,null=False,blank=False,verbose_name="Ramo de atuação:")
	endereco     = models.CharField(max_length=100,null=False,blank=False,verbose_name="Endereço completo:")
	telefone     = models.CharField(max_length=13,null=False,blank=False,verbose_name="Telefone:")
	redesocial1  = models.CharField(max_length=200,null=False,blank=False)
	redesocial2  = models.CharField(max_length=200,null=False,blank=False)
	cidade       = models.CharField(max_length=100,null=False,blank=False,choices=EMPRESA_CIDADE,verbose_name="Cidade:")
	estado_uf    = models.CharField(max_length=100,null=False,blank=False,choices=ESTADO_RN,verbose_name="Estado UF:")
	funcionamento= models.CharField(max_length=20,null=False,blank=False,choices=DIA_SEMANA,verbose_name="Funcionamento:")
	image1       = models.ImageField(upload_to='media/ImagemEmpresa',null=False,blank=False, verbose_name='Imagem1 da empresa:')
	image2       = models.ImageField(upload_to='media/ImagemEmpresa',null=False,blank=False, verbose_name='Imagem2 da empresa:')
	image3       = models.ImageField(upload_to='media/ImagemEmpresa',null=False,blank=False, verbose_name='Imagem3 da empresa:')
	image4       = models.ImageField(upload_to='media/ImagemEmpresa',null=False,blank=True, verbose_name='Imagem4 da empresa:')
	image5       = models.ImageField(upload_to='media/ImagemEmpresa',null=False,blank=True, verbose_name='Imagem5 da empresa:')
	sobre        = models.TextField(max_length=200,null=False,blank=False,verbose_name="Sobre a empresa:")
	observacao   = models.TextField(max_length=100,null=False,blank=False,verbose_name="Alguma observação")
	view_parceiro= models.IntegerField(default=0, null=True,blank=True)
	dataEntrada  = models.DateTimeField(auto_now_add=True,verbose_name="Data da entrada:")
	dataMudanca  = models.DateTimeField(auto_now=True,verbose_name="Data da mudança:")

	def __str__(self):
		return self.nomeLoja;
#-------------------------------------------------------------------------------------------

# MODEL DE MENSAGEM DE USER PARA USER

class MessageUser(models.Model):
	user     = models.ForeignKey(User, on_delete=models.CASCADE)
	sendUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens', verbose_name="Para :")
	messagem = models.TextField(null=False,blank=False)
	Data     = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.user.username;

		


