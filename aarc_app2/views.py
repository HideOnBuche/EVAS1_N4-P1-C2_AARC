from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def VistaS(request):
	html="""
	<h1 style="color:yellow">Soy una H1 de la segunda rama</h1>
    <h2 style="color:pink">mi nombre</h2>
    <ol>
        <ul>Alexis</ul>
        <ul>Riveros</ul>
        <ul>Cuadra</ul>
    </ol>
    <a href="https://www.crunchyroll.com/es-es"> Ir a crunchyroll </a>
	"""
	return HttpResponse(html)