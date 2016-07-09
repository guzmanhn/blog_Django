from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse 
from .models import *
import time
from calendar import month_name
from .forms import FormComment
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.

'''
def mkmonth_list():
	if not Entrada.objects.count():
		return []
	year, month = time.localtime()[:2]
	first = Entrada.objects.order_by("fecha")[0]
	fyear = firts.fecha.year
	fmonth = firts.fecha.month
	months = []

	for y in range(year,fyear-1,-1):
		start,end = 12 , 0
		if y == year:start= month
		if y == fyear:end = fmonth - 1

	for m in range(start, end, -1):
		months.append((y,m,month_name[m]))
	return months	
'''

def month(request,year,month):
	entrada = Entrada.objects.filter(fecha__year=year,fecha__month=month)
	render(request,"litado.html",dict(entrada_list=entrada, user=request.user,month=month_list(),archive=True))

def entrada(request, pk):
	
	identrada = get_object_or_404(Entrada, pk=pk)
	ListComment = comment.objects.filter(idEntrada = pk)
	xcomment = comment(idEntrada = identrada) 
	if request.POST:
		form = FormComment(request.POST, instance = xcomment)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/entrada/'+pk)
	else:
		form = FormComment(instance = xcomment)

	return render(request, "entrada.html",dict(entrada =  identrada, usuario = request.user, form = form, comentarios = ListComment))
	

def main(request):
	entrada = Entrada.objects.all().order_by("-fecha")
	paginator =  Paginator(entrada,2)

	try:
		pagina = int(request.GET.get("page",'1'))
	except ValueError: pagina = 1
	
	try:
			EntradasDeLaPagina = paginator.page(pagina) 
	except (InvalidPage, EmptyPage):
			EntradasDeLaPagina = paginator.page(paginator.num_pages)
	return render(request,"listado.html",dict(entradas = EntradasDeLaPagina, usuario = request.user))

def PostYearMonth(request,year,month):
	entrada = Entrada.objects.filter(fecha__year=year,fecha__month=month)
	paginator =  Paginator(entrada,2)

	try:
		pagina = int(request.GET.get("page",'1'))
	except ValueError: pagina = 1
	
	try:
			EntradasDeLaPagina = paginator.page(pagina) 
	except (InvalidPage, EmptyPage):
			EntradasDeLaPagina = paginator.page(paginator.num_pages)
	return render(request,"listado.html",dict(entradas = EntradasDeLaPagina, usuario = request.user))