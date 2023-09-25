from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def VistaP(request):
	html="""
	<h1 style="color:red">Soy una H1</h1>
    <h2 style="color:green">tabla de partes</h2>
    <ol>
        <ul>parte1</ul>
        <ul>parte2</ul>
        <ul>parte3</ul>
    </ol>
    <a href="https://www.youtube.com/"> Ir a youtube </a>
	"""
	return HttpResponse(html)