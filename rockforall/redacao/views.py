from django.shortcuts import render,get_object_or_404, redirect


def Filmes(request):
	return render(request, 'inicio/Cinema_filmes.html')


	