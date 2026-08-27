from django.shortcuts import render, redirect
import requests
from django.http import Http404
from .forms import CantidadPokemonForm

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'dex/index.html', {})

# #lista de pokemones <-- Se pueden listar x cantidad de pokemones, entre 0 y 1024
# #cantidad es para indicar la cantidad de pokemones,

def listar(request, cantidad):
    if request.method == 'POST':
        raise Http404("Pagina no disponible")
    cantidad = int(cantidad)
    if cantidad > 0 and cantidad <= 1024:
        args = {'limit': cantidad}

        url = 'https://pokeapi.co/api/v2/pokemon'

        req = requests.get(url, params=args)
        if req.status_code == 200:
            req = req.json()
            for i in range(0, len(req['results'])):
                req['results'][i]['id'] = i+1 
            return render(request, 'dex/listar.html', {'cantidad': cantidad, 'pokemones': req['results']})
        else:
            raise RuntimeError("La pokeapi no response, error interno del servidor")
    else:
        raise Http404("Debe de ingresarse un numero mayor a 0 y menor a 1024")
    
def consulta_listar(request):

    if request.method == 'POST':
        form = CantidadPokemonForm(request.POST)
        if form.is_valid():
            limit = form.cleaned_data['cantidad']        
            return redirect("pokedex:resultado_lista",limit)
    else:
        form = CantidadPokemonForm()
    
    return render(request, 'dex/listar.html', {'form':form})
        


# Vista para mostrar los detalles de un pokemon en particular, pkemon_pk es la llave primaria.
def detalles_vista(request, id):
    if request.method == 'POST':
        raise Http404("Pagina no disponible")
    if request.method == 'GET':
        url = 'https://pokeapi.co/api/v2/pokemon/'
        args = id 
        req = requests.get(url + args) #hacemos la peticion a la api de pokeapi para obtener los detalles del pokemon
        req = req.json() #pasamos a un objeto json {diccionario}
        nombre = req['name']
        altura = int(req['height'])/10
        peso = int(req['weight'])/10
        
        movimientos = []

        for i in range(0, len(req['moves'])):
            movimientos.append(req['moves'][i]['move']['name'])
        
        
        habilidades = []
        
        for i in req['abilities']:
            url = i['ability']['url']
            habilidades.append(i['ability']['name'])
        
        types_raw = req['types'] #
        
        tipos = []                                    #  <------ tipos de pokemon, se hace un parseo para obtener el id del tipo de pokemon
        
        for i in types_raw:

            url = i['type']['url']
            type_id = ''
            count = 0
            for u in url[::-1]:
                if u == '/':
                    if count >= 1:
                        break
                    count += 1
                    continue
                else:
                    type_id = u + type_id
            tipos.append({"name":(i['type']['name']), "id":type_id})
            
        context = {
            'id': id,
            'nombre': nombre,
            'altura': altura,
            'peso': peso,
            'movimientos': movimientos,
            'habilidades': habilidades,
            'tipos': tipos
        }
        return render(request, 'dex/detalles.html', {'pokemon': context})
                


    
    
# Vista para mostrar los pokemones de un tipo en particular, tipo_pk es la llave primaria del tipo de pokemon.

def tipos_pokemon(request, id):
    
    args = id

    url = "https://pokeapi.co/api/v2/type/"

    req = requests.get(url+args)

    req = req.json()
        
    pokemon = []
    for i in req['pokemon']:

        url_id_pokemon = (i['pokemon']['url'])
        type_id = ''
        count = 0
        for u in url_id_pokemon[::-1]:
            if u == '/':
                if count >= 1:
                    break
                count += 1
                continue
            else:
                type_id = u + type_id
        pokemon.append({"name":i['pokemon']['name'], "id":type_id})
        
    nombre = req['name']
    
    context = {"pokemones":pokemon, "name":nombre}
    
    if request.method == 'GET':
        return render(request, 'dex/tipos.html', context)
    if request.method == 'POST':
        raise Http404("Pagina no encontrada")