from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):

    # url de pagina
    return render(request, "inicio.html")


def cotizaciones(request):

    return render(request, "cotizaciones.html")


def clientes(request):

    return render(request, "clientes.html")


def vendedores(request):

    return render(request, "vendedores.html")


def serviciosproductos(request):

    return render(request, "serviciosproductos.html")


def login(request):

    return render(request, "login.html")
