# Reproductor de Música

## Descripción del Proyecto

Esta es una aplicación de escritorio que funciona como un reproductor de música con una interfaz de usuario amigable e intuitiva. Este proyecto se centra en la implementación de Tipos de Datos Abstractos (TDA) bajo el concepto de programación orientada a objetos (POO) utilizando el lenguaje de programación Python.

## Funcionalidades

### Reproductor de Música
La aplicación permite al usuario realizar diversas acciones relacionadas con la gestión de su biblioteca de música, como reproducir, pausar, detener, adelantar o retroceder canciones. También puede cargar su biblioteca desde un archivo XML.

### Listas de Reproducción
El usuario puede crear listas de reproducción seleccionando canciones de la biblioteca, organizándolas ya sea por canciones o por artistas. Las listas de reproducción pueden reproducirse en modo normal o aleatorio.

### Carga de Biblioteca
La biblioteca de canciones se carga desde un archivo XML con una estructura específica. Los artistas, álbumes y canciones se almacenan en listas doblemente enlazadas. Las listas de artistas contienen las listas de álbumes, y cada álbum tiene su propia lista de canciones.

### Guardado de Listas de Reproducción
Las listas de reproducción creadas por el usuario pueden guardarse en un archivo XML para su posterior carga.

### Reportes
La aplicación genera dos tipos de reportes:
1. **Reporte HTML:** Muestra gráficamente las canciones más reproducidas y a qué lista de reproducción pertenecen.
2. **Reporte Graphviz:** Permite visualizar en cualquier momento la estructura de las listas doblemente enlazadas circulares y otras estructuras de datos utilizadas.

## Implementación

### Carga de Biblioteca
La biblioteca se carga desde un archivo XML con una estructura específica.

### Listas de Reproducción
Las listas de reproducción se representan como listas doblemente enlazadas circulares, con la posibilidad de reproducirse en modo normal o aleatorio.

### Guardado de Listas de Reproducción
Las listas de reproducción pueden guardarse en un archivo XML.

### Reportes
La aplicación genera reportes HTML y utiliza Graphviz para visualizar la estructura de las listas de reproducción.

## Instrucciones de Ejecución

1. Clona el repositorio en tu máquina local.
2. Abre la terminal y navega al directorio del proyecto.
3. Ejecuta el archivo principal `Reproductor.py`.

**Nota:** Asegúrate de tener instalado Python en tu sistema.

## Colaborador Principal
- [Carbonell Castillo]

## Licencia
Este proyecto está bajo la licencia MIT.
