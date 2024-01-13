import xml.etree.ElementTree as ET
from xml.dom import minidom
import SG as sg
import listaCircular as lista
from Artista import Artista
from Album import Album
from Cancion import Cancion 
from PreCancion import PreCancion
from ListaReproduccion import ListaReproduccion



listaDefecto = lista.ListaDobleEnlazada()

def leerEntrada(xml_file):
    try:
        tree = ET.parse(xml_file)
    except Exception as e:
        print("Error al leer el archivo de entrada: ", e)

    root = tree.getroot()
    
    for cancion in root.findall('cancion'):
        nombre = cancion.get('nombre')
            
        print(f"Canción: {nombre}")

        artista = cancion.find('artista').text
        print(f"Artista: {artista}")
        

        album = cancion.find('album').text
        print(f"Álbum: {album}")

        imagen = cancion.find('imagen').text
        print(f"Ruta de la imagen: {imagen}")

        
        ruta = cancion.find('ruta').text
        print(f"Ruta de la canción: {ruta}")

        artista = cancion.find('artista').text
        print(f"Artista: {artista}")

        lista_albumes = lista.ListaDobleEnlazada()
        lista_canciones = lista.ListaDobleEnlazada()
        
        if sg.lista_artistas.esta_vacia():     
                   
            lista_canciones.insertar_al_final(Cancion(nombre, imagen, ruta))
            lista_albumes.insertar_al_final(Album(album, lista_canciones))
            sg.lista_artistas.insertar_al_final(Artista(artista, lista_albumes))
            listaDefecto.insertar_al_final(PreCancion(nombre, artista, album, 0, imagen, ruta))
        elif sg.lista_artistas.buscarArtista(artista):
            if sg.lista_artistas.buscarAlbumArtista(artista, album):
                print("El album ya existe")
                if sg.lista_artistas.buscarCancionArtista(nombre, album, cancion):
                    print("La canción ya existe")
                else:
                    sg.lista_artistas.insertarCancionAlbumArtista(artista, album, Cancion(nombre, imagen, ruta)) 
                    listaDefecto.insertar_al_final(PreCancion(nombre, artista, album, 0, imagen, ruta))
            else: 
                print("El album no existe")
                sg.lista_artistas.insertarCancionAlbum(album, Cancion(nombre, imagen, ruta))  
                sg.lista_artistas.insertarAlbumArtista(artista, Album(album, lista_canciones))
                listaDefecto.insertar_al_final(PreCancion(nombre, artista, album, 0, imagen, ruta))
                
        else:    
            lista_canciones.insertar_al_final(Cancion(nombre, imagen, ruta))
            lista_albumes.insertar_al_final(Album(album, lista_canciones))
            sg.lista_artistas.insertar_al_final(Artista(artista, lista_albumes))
            listaDefecto.insertar_al_final(PreCancion(nombre, artista, album, 0, imagen, ruta))

        print("\n")


def leerEntradaListaReproduccion():
    ruta = "salida.xml"
    validacion = False
    try:
        tree = ET.parse(ruta)
        validacion= True
    except Exception as e:
        print("Error al leer el archivo de entrada: ", e)

    if validacion != True:
        print("Error al leer el archivo de entrada")
        return

    
    root = tree.getroot()

    for listaObtenida in root.findall('lista'):
        nombre = listaObtenida.get('nombre')
        print(f"Lista: {nombre}")
        crearListaReproduccion(nombre)
        for cancion in listaObtenida.findall('cancion'):
            nombreCancion = cancion.get('nombre')
            print(f"Canción: {nombreCancion}")

            artista = cancion.find('artista').text
            print(f"Artista: {artista}")

            album = cancion.find('album').text
            print(f"Álbum: {album}")

            imagen = cancion.find('imagen').text
            print(f"Ruta de la imagen: {imagen}")

            ruta = cancion.find('ruta').text
            print(f"Ruta de la canción: {ruta}")

            artista = cancion.find('artista').text
            print(f"Artista: {artista}")

            vecesReproducida = cancion.find('vecesReproducida').text
            print(f"Veces reproducida: {vecesReproducida}")

            ##Se almacenen las canciones en las listas
            lista_albumes = lista.ListaDobleEnlazada()
            lista_canciones = lista.ListaDobleEnlazada()
        
            if sg.lista_artistas.esta_vacia():     
                   
                lista_canciones.insertar_al_final(Cancion(nombreCancion, imagen, ruta))
                lista_albumes.insertar_al_final(Album(album, lista_canciones))
                sg.lista_artistas.insertar_al_final(Artista(artista, lista_albumes))
                listaDefecto.insertar_al_final(PreCancion(nombreCancion, artista, album, 0, imagen, ruta))
            elif sg.lista_artistas.buscarArtista(artista):
                if sg.lista_artistas.buscarAlbumArtista(artista, album):
                    print("El album ya existe")
                    if sg.lista_artistas.buscarCancionArtista(nombreCancion, album, cancion):
                        print("La canción ya existe")
                    else:
                        sg.lista_artistas.insertarCancionAlbumArtista(artista, album, Cancion(nombreCancion, imagen, ruta)) 
                        listaDefecto.insertar_al_final(PreCancion(nombreCancion, artista, album, 0, imagen, ruta))
                else: 
                    print("El album no existe")
                    sg.lista_artistas.insertarCancionAlbum(album, Cancion(nombreCancion, imagen, ruta))  
                    sg.lista_artistas.insertarAlbumArtista(artista, Album(album, lista_canciones))
                    listaDefecto.insertar_al_final(PreCancion(nombreCancion, artista, album, 0, imagen, ruta))
                
            else:    
                lista_canciones.insertar_al_final(Cancion(nombreCancion, imagen, ruta))
                lista_albumes.insertar_al_final(Album(album, lista_canciones))
                sg.lista_artistas.insertar_al_final(Artista(artista, lista_albumes))
                listaDefecto.insertar_al_final(PreCancion(nombreCancion, artista, album, 0, imagen, ruta))

            print("\n")

            #se crea la lista de reproduccion
            
            #se guarda la cancion en la lista de reproduccion
            cancionObtenida = sg.lista_artistas.obtenerCancionArtista(artista, album, nombreCancion)
            guardarCancionListaReproduccion(nombre, cancionObtenida)
            lista_canciones= sg.lista_reproduccion
            lista_canciones.actualizarVecesReproducidaNombreLista(nombre, artista, album, nombreCancion, int(vecesReproducida))
        


        print("\n")

def crearArchivoXML():

    root = ET.Element("ListasReproduccion")
    lista = ET.SubElement(root, "Lista")
    lista.set("nombre", "ListaDefecto")
    
    
    canciones = ET.SubElement(lista, "cancion")
    canciones.set("nombre", "CancionDefecto")
    artista = ET.SubElement(canciones, "artista")
    artista.text = "ArtistaDefecto"
    album = ET.SubElement(canciones, "album")
    album.text = "AlbumDefecto"
    vecesReproducida = ET.SubElement(canciones, "vecesReproducida")
    vecesReproducida.text = "0"
    pathImagen = ET.SubElement(canciones, "imagen")
    pathImagen.text = "ImagenDefecto"
    pathCancion = ET.SubElement(canciones, "ruta")
    pathCancion.text = "CancionDefecto"

    canciones = ET.SubElement(lista, "cancion")
    canciones.set("nombre", "CancionDefecto")
    artista = ET.SubElement(canciones, "artista")
    artista.text = "ArtistaDefecto"
    album = ET.SubElement(canciones, "album")
    album.text = "AlbumDefecto"
    vecesReproducida = ET.SubElement(canciones, "vecesReproducida")
    vecesReproducida.text = "0"
    pathImagen = ET.SubElement(canciones, "imagen")
    pathImagen.text = "ImagenDefecto"
    pathCancion = ET.SubElement(canciones, "ruta")
    pathCancion.text = "CancionDefecto"


    tree = ET.ElementTree(root)
    tree.write("salida.xml", encoding="UTF-8", xml_declaration=True)
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open("salida.xml", "w") as f:
        f.write(xmlstr)
    print("Archivo de salida generado exitosamente.")

def crearListaReproduccionDefecto():
    sg.lista_reproduccion.insertar_al_final(ListaReproduccion("ListaDefecto", listaDefecto))


def crearListaReproduccion(nombre):
    lista_reproduccion = lista.ListaDobleEnlazada()
    sg.lista_reproduccion.insertar_al_final(ListaReproduccion(nombre, lista_reproduccion))
    

    print("Lista de reproducción creada")


def guardarCancionListaReproduccion(nombre, cancion):
    sg.lista_reproduccion.insertarCancionListaReproduccion(nombre, cancion)
    print("Canción guardada en la lista de reproducción")





# leerEntrada("testBiblioteca.xml")
# print("-------------Ressultado-------------")

# sg.lista_artistas.mostrar_artistas()
# sg.lista_reproduccion.mostrar_listaReproduccion()

# #Prueba de crear lista

# crearListaReproduccion("ListaPrueba1")

# print("-------------Ressultado-------------")
# cancionObtenida = sg.lista_artistas.obtenerCancionArtista("Artista1", "Album1", "Cancion1")


# guardarCancionListaReproduccion("ListaPrueba1", cancionObtenida)

# print("-------------Ressultado-------------")
# sg.lista_reproduccion.mostrar_listaReproduccion()


# print("-------------Ressultado22222222222-------------")
# sg.lista_artistas.imprimirDatosAlbum()


