from django.http import Http404
from django.shortcuts import render


PELICULAS = [
    {"id": 1, "titulo": "El faro del desierto", "genero": "Drama", "precio": 4500,
     "duracion": 112, "estreno": False, "apta_todo_publico": True,
     "sinopsis": "Un guardafaros en la costa de Antofagasta recibe una carta que lo obliga a volver al pueblo que abandono."},
    {"id": 2, "titulo": "Codigo Norte", "genero": "Accion", "precio": 5500,
     "duracion": 98, "estreno": True, "apta_todo_publico": False,
     "sinopsis": "Una analista descubre una falla en el sistema de una minera y tiene 24 horas para evitar un desastre."},
    {"id": 3, "titulo": "La ultima funcion", "genero": "Comedia", "precio": 4500,
     "duracion": 95, "estreno": False, "apta_todo_publico": True,
     "sinopsis": "Un cine de barrio a punto de cerrar organiza una funcion final en la que nada sale como se planeo."},
    {"id": 4, "titulo": "Orbita", "genero": "Ciencia ficcion", "precio": 6000,
     "duracion": 131, "estreno": True, "apta_todo_publico": True,
     "sinopsis": "La tripulacion de una estacion espacial pierde contacto con la Tierra y debe decidir si regresar."},
    {"id": 5, "titulo": "Sombras del salar", "genero": "Suspenso", "precio": 5500,
     "duracion": 104, "estreno": True, "apta_todo_publico": False,
     "sinopsis": "Una periodista investiga desapariciones en un campamento del salar y descubre que alguien la sigue."},
    {"id": 6, "titulo": "Pequenos gigantes", "genero": "Animacion", "precio": 4000,
     "duracion": 88, "estreno": False, "apta_todo_publico": True,
     "sinopsis": "Un grupo de insectos organiza una expedicion para cruzar un jardin antes de que llegue el invierno."},
    {"id": 7, "titulo": "Ruta 5", "genero": "Documental", "precio": 3500,
     "duracion": 76, "estreno": False, "apta_todo_publico": True,
     "sinopsis": "Un recorrido por los pueblos que viven a orillas de la carretera mas larga de Chile."},
    {"id": 8, "titulo": "Noche de brujas en Mejillones", "genero": "Terror", "precio": 5000,
     "duracion": 101, "estreno": False, "apta_todo_publico": False,
     "sinopsis": "Un grupo de amigos pasa la noche en una caleta abandonada y descubre que no estan solos."},
]


def inicio(request):
	duracion_total = 0
	cantidad_estrenos = 0

	for pelicula in PELICULAS:
		duracion_total += pelicula['duracion']
		if pelicula['estreno']:
			cantidad_estrenos += 1

	duracion_promedio = round(duracion_total / len(PELICULAS))

	contexto = {
		'peliculas': PELICULAS,
		'duracion_promedio': duracion_promedio,
		'cantidad_estrenos': cantidad_estrenos,
	}
	return render(request, 'cartelera/inicio.html', contexto)


def detalle(request, id):
    pelicula_encontrada = None

    for pelicula in PELICULAS:
        if pelicula['id'] == id:
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada is None:
        raise Http404('La pelicula no existe')

    precio_nocturno = round(pelicula_encontrada['precio'] * 1.2)

    if pelicula_encontrada['apta_todo_publico'] and not pelicula_encontrada['estreno']:
        etiqueta = 'Clasico familiar'
    elif pelicula_encontrada['estreno']:
        etiqueta = 'Estreno de la semana'
    else:
        etiqueta = 'En cartelera'

    contexto = {
        'pelicula': pelicula_encontrada,
        'precio_nocturno': precio_nocturno,
        'etiqueta': etiqueta,
    }
    return render(request, 'cartelera/detalle.html', contexto)
