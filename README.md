# Proyecto conexión Personas y objetos
Proyecto creado por Fernando Reyes para el curso de Coderhouse de Python comisión 34640
## Descripción
Para correr el proyecto en local se recomienda crear un ambiente virtual y ejecutar como sigue

### Instalación y ejecución del Proyecto
Creacion de un ambiente virtual de Python
```
python -m venv .coder
```
Instalar django
```
pip install django
```
Abrir el Ambiente virtual de python, en windows es abrir desde la consola la ruta de nuestro ambiente creado: por ejemplo
```
Ejecutar la ruta "c:\Users\usuario1\Entrega1_FernandoReyes\.coder\Scripts\activate"
```

Estando dentro del proyecto y si queremos correr el server ejecutamos lo siguiente:
```
python manage.py runserver
```

### Prueba del proyecto

<img width="917" alt="image" src="https://user-images.githubusercontent.com/9980293/205183620-e33b4850-5355-432d-bcf8-b7b0756f65e7.png">

Como se puede apreciar, la página posee botones para ver plantillas, sin contenido por el momento, de Persona, Paquetes y Celulares

#### Vista de páginas básicas
<img width="917" alt="image" src="https://user-images.githubusercontent.com/9980293/205183973-360c5984-70bc-4e10-94cb-35b80b3443e2.png">
<img width="924" alt="image" src="https://user-images.githubusercontent.com/9980293/205184003-7f9afb8a-29aa-4f97-9b2b-b16b30206369.png">
<img width="917" alt="image" src="https://user-images.githubusercontent.com/9980293/205184031-9e7a512e-d5f8-4ff2-b682-e0b55c89da61.png">


#### Vistas básicas

<img width="420" alt="image" src="https://user-images.githubusercontent.com/9980293/205184243-8cf33559-7a5d-47d0-b34f-ea71028ab037.png">

Las vistas en las que puede interactuar el usuario son:
* Inicio aplicación (http://127.0.0.1:8000/familiares/)
* familiares/personaForm/  (http://127.0.0.1:8000/familiares/personaForm/)
* familiares/paqueteForm/ (http://127.0.0.1:8000/familiares/paqueteForm/)
* familiares/celularForm/ (http://127.0.0.1:8000/familiares/celularForm/)
* familiares/personas/ (http://127.0.0.1:8000/familiares/personas/)
* familiares/paquetes/ (http://127.0.0.1:8000/familiares/paquetes/)
* familiares/celulares/ (http://127.0.0.1:8000/familiares/celulares/)
* familiares/buscarpaquete/ (http://127.0.0.1:8000/familiares/buscarpaquete/)

#### Formularios
Para los formularios de Personas, Paquetes y Paquetes nos muestra una vista similar entre ellas:
<img width="826" alt="image" src="https://user-images.githubusercontent.com/9980293/205184940-f1c56436-b92b-4097-a011-24719bcddac8.png">
En la que si creamos el objeto, nos devuelve a la página principal de la Aplicación. En este caso al inicio:


#### Ejemplo: creación de paquete
Para crear un paquete nos dirigimos a la url de familiares/paqueteForm/
Nos pediran el nombre de nuestro paquete, el peso de este, remitente y el destinatario como sale a continuación:

<img width="651" alt="image" src="https://user-images.githubusercontent.com/9980293/205185813-6b7eca3b-cec5-4bff-9da3-c57a1dccc85d.png">


#### Búsqueda de paquetes
Si queremos buscar un paquete en específico nos diriginos a familiares/buscarpaquete: 
En este caso vamos a buscar el paquete de nombre Flores

<img width="700" alt="image" src="https://user-images.githubusercontent.com/9980293/205185286-791b762a-5472-4720-976f-c5e18e7e26b9.png">

El resultado es el siguiente:

<img width="664" alt="image" src="https://user-images.githubusercontent.com/9980293/205185327-87c096f3-037a-49c7-ba28-010f84a5e290.png">

#### Finalizando
El proyecto esta en sus primeros inicios, por lo que todavía faltan implementar varias funcionalidades que se irán agregando en futuras versiones

# Gracias por visualizar el proyecto




