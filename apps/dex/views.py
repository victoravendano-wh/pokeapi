from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'dex/index.html', {})

# #lista de pokemones <-- Se pueden listar x cantidad de pokemones, entre 0 y 1024
# #cantidad es para indicar la cantidad de pokemones,

def listar(request, cantidad):
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
            pass #aqui redirigir a la pagina de consulta con un mensaje de error
    else:
        pass #aqui redirigir a la pagina de consulta con un mensaje de error para que se ponga un numero mayor a 0 y menor a 1024
                
    return render(request, 'dex/listar.html', {'cantidad': cantidad})
    
def consulta_listar(request):
    return render(request, 'dex/index.html')

# # Vista para mostrar los detalles de un pokemon en particular, pkemon_pk es la llave primaria.
# def detalles_vista(request, pokemon_pk):
    
# # Vista para mostrar los pokemones de un tipo en particular, tipo_pk es la llave primaria del tipo de pokemon.
# def tipos_pokemon(request, tipo_pk):