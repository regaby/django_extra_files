from django.urls import path
from . import views

urlpatterns = [
   path('', views.index), # views.index -> llama al metodo index dentro de views.py
]

post_django = {
    'titulo': 'Curso de Django',
    'autor': 'Gabriela',
    'fecha': date(2021,9,2),
    'contenido': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Excepturi hic error eius architecto sint, reiciendis quos velit sunt illum earum fuga illo possimus itaque enim debitis placeat. Maxime, provident praesentium?\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Excepturi hic error eius architecto sint, reiciendis quos velit sunt illum earum fuga illo possimus itaque enim debitis placeat. Maxime, provident praesentium?\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Excepturi hic error eius architecto sint, reiciendis quos velit sunt illum earum fuga illo possimus itaque enim debitis placeat. Maxime, provident praesentium?',
    'modalidad': 'Virtual',
    'resumen': 'En este curso aprenderás a desarrollar sitios y aplicaciones web con python y el framework django',
    'imagen': 'blog/images/django.jpg',
    'slug': 'curso-de-django'
}
post_peluqueria = {
    'titulo': 'Curso de Peluqueria',
    'autor': 'Carlos',
    'fecha': date(2021,9,2),
    'contenido': 'Se realiza todos los Miercoles a  las 19hs.',
    'modalidad': 'Presencial',
    'resumen': 'En este curso se aprenderan los conceptos de peluqueria',
    'imagen': 'blog/images/peluqueria.png',
    'slug': 'curso-de-peluqueria'
}
post_panaderia = {
    'titulo': 'Curso de panaderia',
    'autor': 'Carlos',
    'fecha': date(2021,9,2),
    'contenido': 'Se realiza todos los Miercoles a  las 19hs.',
    'modalidad': 'Presencial',
    'resumen': 'En este curso se aprenderan los conceptos de panaderia',
    'imagen': 'blog/images/panadero.png',
    'slug': 'curso-de-panaderia'
}
post_fotografia = {
    'titulo': 'Curso de fotografia',
    'autor': 'Carlos',
    'fecha': date(2021,9,2),
    'contenido': 'Se realiza todos los Miercoles a  las 19hs.',
    'modalidad': 'Presencial',
    'resumen': 'En este curso se aprenderan los conceptos de fotografia',
    'imagen': 'blog/images/fotografia.png',
    'slug': 'curso-de-fotografia'
}
lista_posts = [
    post_django,
    post_peluqueria,
    post_panaderia,
    post_fotografia,
]
