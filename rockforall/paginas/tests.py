from django.test import TestCase
from paginas.models import Pensamento
 
class TestPensamento(unittest.TestCase):
	def SetUp(self):
		Pensamento.objects.create(user='admin',ideia='A vida é uma merda')

	
	def TesteEntradas(self):
		o = Pensamento.objects.get(user='admin',ideia='A vida é uma merda')
		self.assertEqual(o.ideia, 'A vida é uma merda')

