# FutbolBlog - Mitad de Cancha

Mitad de Cancha es una aplicación web desarrollada con Django que permite a los usuarios crear, ver y gestionar publicaciones relacionadas con el mundo del fútbol. 

## Estructura del Proyecto

- **accounts**: Registro, inicio de sesión y gestión de usuarios.
- **posts**: CRUD de publicaciones
- **messaging**: Mensajes privados entre usuarios.
- **pages**: Páginas estáticas como el inicio, acerca de..., etc.
- **futbolblog**: Proyecto principal de configuración.

## Funcionalidades

- Autenticación de usuarios (registro, login, logout).
- Crear, editar y eliminar publicaciones.
- Panel de administración para gestionar usuarios, posts y categorías.
- Estilo responsive con Bootstrap 5.
- Imágenes destacadas para las publicaciones.

## Requisitos

- Python 
- Django 
- SQLite (por defecto)

## Instalación

1. Clona este repositorio:
git clone https://github.com/gabrielcari08/EntregaFinal-Cari.git

2. Crea y activa el entorno virtual:
python -m venv venv
venv\Scripts\activate

3. Navega a esta ruta:
cd futbolblog

4. Instala las dependencias.
pip install -r requirements.txt

5. Aplica las migraciones:
python manage.py makemigrations
python manage.py migrate

6. Crea un superusuario (Ingresando tu nombre, email y contraseña):
python manage.py createsuperuser
URL: http://127.0.0.1:8000/admin/

7. Inicia el servidor:
python manage.py runserver
URL: http://127.0.0.1:8000

## Una vez dentro de la WEB.

1. Al entrar por primera vez a la pagina verás en pantalla la bienvenida a la web. Debajo habran dos opciones: Iniciar Sesion o Registrarse. Inicia sesion si ya tienes una cuenta. Registrate si es tu primera vez en esta. Llena los formularios que se te proponen e ingresa a la pagina.

2. Una vez iniciada tu sesion podras ver un listado de posts sobre noticias del mundo del futbol. Encontraras muchas categorias como liga argentina, primera nacional, seleccion, etc. 

3. Si has iniciado sesion tienes el poder de publicar una post. Aqui debes ingresar el titulo, subtitulo, categoria, contenido e incluso subir una imagen de referencia. Esto hazlo a tu gusto.

4. La pagina contiene varias secciones, detallaremos algunas de ellas a contiunacion.

5. En "Inicio" se muestra un mensaje de bienvenida, y una descipcion breve del sitio.

6. En "Posts" se muestran todos los posteos de diferentes autores como ya hemos mencionado.

7. En "Categoria" podemos filtrar los posteos. Por ejemplo si queremos ver solo las noticias de la liga profesional de futbol de Argentina, seleccionamos "Liga Profesional", y asi con las demas. En caso de que no hayan posteos con determinada categoria se mostrata un mensaje de "No hay publicaciones en esta categoría."

8. En "Mis Publicaciones", puedes ver el historial de tus posteos hechos y crear un nuevo posteo.

9. En "Acerca de Mi", hay una breve descripcion mia, el creador de este sitio.

10. En "Perfil" tienes tus datos personales, foto de perfil, username, email y una bio. Aqui puedes editar tu perfil o cerrar sesion.

11. Por ultimo en "Mensajes", puedes ver los mensajes que te han enviado otros usuarios y tu tambien puedes mandar un mensaje hacia algun autor.

12. ¡Mucha suerte probando el sitio!









