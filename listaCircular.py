import xml.etree.ElementTree as ET
from xml.dom import minidom
from PreCancion import PreCancion
from Cancion import Cancion
import SG as sg
from Arbol import *
import webbrowser
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def esta_vacia(self):
        return self.inicio is None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def mostrar_lista(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")
    
    def mostrar_canciones(self):
        actual = self.inicio
        while actual:
            print("Titulo cancion: ", actual.dato._titulo,"\n", "Ruta imagen: ", actual.dato._pathImagen, "\nRuta Cancion: ", actual.dato._pathRuta)
            actual = actual.siguiente
        print("------")

    def mostrar_albumes(self):
        actual = self.inicio
        while actual:
            print("Nombre album: ", actual.dato._nombre, "\n")
            actual.dato._listaCanciones.mostrar_canciones()
            actual = actual.siguiente

        print("------")
    
    def mostrar_artistas(self):
        actual = self.inicio
        while actual:
            print("Nombre artista: ", actual.dato._nombre, "\n")
            actual.dato._listaAlbumes.mostrar_albumes()
            actual = actual.siguiente

        print("------")

    def buscarArtista(self, nombre):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    

    def buscarAlbumArtista(self, nombre, album):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                if actual.dato._listaAlbumes.buscarAlbum(album):
                    return True
            actual = actual.siguiente
        return False

    def buscarValidarCancionListaReproduccion(self, nombreLista, nombreArtista, nombreAlbum, nombreCancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombreLista:
                if actual.dato._lista_canciones.validarCancionArtistaAlbumCancion(nombreArtista, nombreAlbum, nombreCancion):
                    return True
            actual = actual.siguiente
        return False
    
    def validarCancionArtistaAlbumCancion(self, nombreArtista, nombreAlbum, nombreCancion):
        actual = self.inicio
        while actual:
            if actual.dato._artista == nombreArtista:
                if actual.dato._album == nombreAlbum:
                    if actual.dato._nombre == nombreCancion:
                        return True
            actual = actual.siguiente

        return False
    def buscarCancionArtista(self, nombre, album, cancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                if actual.dato._listaAlbumes.buscarAlbum(album):
                    if actual.dato._listaAlbumes.buscarCancion(cancion):
                        return True
            actual = actual.siguiente
        return False
    
    
    def buscarAlbum(self, nombre):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    
    def buscarCancion(self, nombre):
        actual = self.inicio
        while actual:
            if actual.dato._titulo == nombre:
                return True
            actual = actual.siguiente
        return False

    def buscarCancionAlbum(self, nombre, cancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                if actual.dato._listaCanciones.buscarCancion(cancion):
                    return True
            actual = actual.siguiente
        return False
    

    def insertarCancionAlbum(self, nombre, cancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                actual.dato._listaCanciones.insertar_al_final(cancion)
            actual = actual.siguiente
    

    def insertarCancionAlbumArtista(self, nombre, album, cancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                actual.dato._listaAlbumes.insertarCancionAlbum(album, cancion)
            actual = actual.siguiente

            
    def insertarAlbumArtista(self, nombre, album):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                actual.dato._listaAlbumes.insertar_al_final(album)
            actual = actual.siguiente
    
    def mostrar_listaReproduccion(self):
        actual = self.inicio
        while actual:
            print("Nombre lista: ", actual.dato._nombre, "\n")
            actual.dato._lista_canciones.mostrar_cancionesListaReproduccion()
            actual = actual.siguiente
            
        print("------")

    def mostrar_cancionesListaReproduccion(self):
        actual = self.inicio
        while actual:
            print("Titulo cancion: ", actual.dato._nombre,"\n", "Artist: ", actual.dato._artista, "\nAlbum: ", actual.dato._album,"\n veces reproducida: ", actual.dato._vecesReproducida, "\nRuta imagen: ", actual.dato._pathImagen, "\nRuta Cancion: ", actual.dato._pathCancion)
            actual = actual.siguiente
            print("-----------------\n")
        print("------")
    
    def generarArchivoXML(self):
        root = ET.Element("ListasReproduccion")
        actual = self.inicio
        while actual:
            lista = ET.SubElement(root, "lista")
            lista.set("nombre", actual.dato._nombre)
            actual2 = actual.dato._lista_canciones.inicio
            while actual2:
                cancion = ET.SubElement(lista, "cancion")
                cancion.set("nombre", actual2.dato._nombre)
                artista = ET.SubElement(cancion, "artista")
                artista.text = actual2.dato._artista
                album = ET.SubElement(cancion, "album")
                album.text = actual2.dato._album
                vecesReproducida = ET.SubElement(cancion, "vecesReproducida")
                vecesReproducida.text = str(actual2.dato._vecesReproducida)
                pathImagen = ET.SubElement(cancion, "imagen")
                pathImagen.text = actual2.dato._pathImagen
                pathCancion = ET.SubElement(cancion, "ruta")
                pathCancion.text = actual2.dato._pathCancion
                actual2 = actual2.siguiente
            actual = actual.siguiente
        tree = ET.ElementTree(root)
        tree.write("salida.xml", encoding="UTF-8", xml_declaration=True)
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
        with open("salida.xml", "w") as f:
            f.write(xmlstr)
        print("Archivo de salida generado exitosamente.")
        print("------")
    def obtenerListaCancionesPorNombre(self, nombre):
        actual = self.inicio
        lista = []
        while actual:
            if actual.dato._nombre == nombre:
                actual2 = actual.dato._lista_canciones.inicio
                while actual2:
                    lista.append(actual2.dato)
                    actual2 = actual2.siguiente
            actual = actual.siguiente
        return lista
        print("------")

    def actualizarVecesReproducidaNombreLista(self, nombreLista, nombreArtista, nombreAlbum, nombreCancion, cantidad):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombreLista:
                actual.dato._lista_canciones.actualizarVecesReprodcida(nombreArtista, nombreAlbum, nombreCancion, cantidad)
            actual = actual.siguiente

    def obtenerListaReproduccion(self):
        actual = self.inicio
        lista = []
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        return lista
    def actualizarVecesReprodcida(self, nombreArtista, nombreAlbum, nombreCancion, cantidad):
        actual = self.inicio
        while actual:
            if actual.dato._artista == nombreArtista:
                if actual.dato._album == nombreAlbum:
                    if actual.dato._nombre == nombreCancion:
                        if cantidad !=None:
                            actual.dato._vecesReproducida = cantidad
                        else:   
                            actual.dato._vecesReproducida += 1                
            actual = actual.siguiente

    def validarNombreListaReproduccion(self, nombre):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    def obtenerCancionArtista(self, nombreArtista, nombreAlbum, nombreCancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombreArtista:
                if actual.dato._listaAlbumes.buscarAlbum(nombreAlbum):
                    if actual.dato._listaAlbumes.buscarCancionAlbum(nombreAlbum, nombreCancion):
                        cancionObtenida = PreCancion(actual.dato._listaAlbumes.obtenerCancionPorAlbum(nombreAlbum, nombreCancion)._titulo, actual.dato._nombre, nombreAlbum, actual.dato._listaAlbumes.obtenerCancionPorAlbum(nombreAlbum, nombreCancion)._vecesReproducida, actual.dato._listaAlbumes.obtenerCancionPorAlbum(nombreAlbum, nombreCancion)._pathImagen, actual.dato._listaAlbumes.obtenerCancionPorAlbum(nombreAlbum, nombreCancion)._pathRuta)
                        return cancionObtenida
            actual = actual.siguiente
        return None
    

    def obtenerCancionPorAlbum(self,nombreAlbum, nombreCancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombreAlbum:
                if actual.dato._listaCanciones.buscarCancion(nombreCancion):
                    cancionObtenida = Cancion(actual.dato._listaCanciones.obtenerCancion(nombreCancion)._titulo, actual.dato._listaCanciones.obtenerCancion(nombreCancion)._pathImagen, actual.dato._listaCanciones.obtenerCancion(nombreCancion)._pathRuta)
                    return cancionObtenida
            actual = actual.siguiente
        return None
    
    def obtenerCancion(self, nombreCancion):
        actual = self.inicio
        while actual:
            if actual.dato._titulo == nombreCancion:
                cancionObtenida = Cancion(actual.dato._titulo, actual.dato._pathImagen, actual.dato._pathRuta)
                return cancionObtenida
            actual = actual.siguiente
        return None
    
    def insertarCancionListaReproduccion(self, nombre, cancion):
        actual = self.inicio
        while actual:
            if actual.dato._nombre == nombre:
                actual.dato._lista_canciones.insertar_al_final(cancion)
            actual = actual.siguiente

    
    #-------------------------------
    def generarCanciones(self):
        actual = self.inicio
        while actual:
            
            actual.dato._listaAlbumes.mostrar_albumesImprimir(actual.dato._nombre)
            actual = actual.siguiente
    
    def mostrar_albumesImprimir(self, nombreArtista):
        actual = self.inicio
        while actual:
            
            actual.dato._listaCanciones.imprimirCancionesAlbum(nombreArtista, actual.dato._nombre)
            actual = actual.siguiente

    


    def imprimirCancionesAlbum(self, nombreArtista, nombreAlbum):
        actual = self.inicio
        while actual:
            
            print("Artista: ",nombreArtista, "Album: ", nombreAlbum,  "\nTitulo cancion: ", actual.dato._titulo,"\n", "Ruta imagen: ", actual.dato._pathImagen, "\nRuta Cancion: ", actual.dato._pathRuta)
            cancionCreada = PreCancion(actual.dato._titulo, nombreArtista, nombreAlbum, actual.dato._vecesReproducida, actual.dato._pathImagen, actual.dato._pathRuta)
            sg.lista_cancionesMostrar.insertar_al_final(cancionCreada)
            actual = actual.siguiente

    def obtener_lista(self):
        actual = self.inicio
        lista = []
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        return lista


    def generarGraficaPlaylist(self):
        actual = self.inicio
        arbol.dot.clear()

        while actual:
            raiz = arbol.agregarNodo(actual.dato._nombre)
            actual2 = actual.dato._lista_canciones.inicio
            artista = arbol.agregarNodo("Artista")
            arbol.agregarArista(raiz, artista)
            album = arbol.agregarNodo("Album")
            arbol.agregarArista(raiz, album)
            cancion = arbol.agregarNodo("Cancion")
            arbol.agregarArista(raiz, cancion)
            vecesReproducida = arbol.agregarNodo("Veces Reproducida")
            arbol.agregarArista(raiz, vecesReproducida)
            actual2 = actual.dato._lista_canciones.inicio
            while actual2:
                artistaObtenido = arbol.agregarNodo(actual2.dato._artista)
                arbol.agregarArista(artista, artistaObtenido)
                artista = artistaObtenido
                albumObtenido = arbol.agregarNodo(actual2.dato._album)
                arbol.agregarArista(album, albumObtenido)
                album = albumObtenido
                cancionObtenida = arbol.agregarNodo(actual2.dato._nombre)
                arbol.agregarArista(cancion, cancionObtenida)
                cancion = cancionObtenida
                vecesReproducidaObtenida = arbol.agregarNodo(str(actual2.dato._vecesReproducida))
                arbol.agregarArista(vecesReproducida, vecesReproducidaObtenida)
                vecesReproducida = vecesReproducidaObtenida

                actual2 = actual2.siguiente
            actual = actual.siguiente
        arbol.generarGrafica("Resultado", "png")
    
    def generarReporteHTML(self):
        print("Entro exportar reporte")
        
        
    # Crea el contenido HTML que deseas exportar
        html_content = """
        <html>
        <head>
            <title>Reporte</title>
            <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
        """
        actual = self.inicio
        while actual:
            print("Entro exportar reporte")
            print("Nombre" + actual.dato._nombre)
            html_content += """
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body text-center">        
                            <h5 class="card-title m-b-0">"""+str(actual.dato._nombre)+"""</h5>
                        </d iv>
                        <div class="table-responsive">
                            <table class="table">
                                <thead class="thead-light">
                                    <tr>
                                        <th>
                                            <label class="customcheckbox m-b-20">
                                                <input type="checkbox" id="mainCheckbox">
                                                <span class="checkmark"></span>
                                            </label>
                                        </th>
        
                                        <th scope="col">Nombre</th>
                                        <th scope="col">Autor</th>
                                        <th scope="col">Album</th>
                                        <th scope="col">Veces Reproducidas</th>
                                        
                                   
                                    </tr>
                                </thead>
                                <tbody class="customtable">
                                """
        
            actual2 = actual.dato._lista_canciones.inicio
            while actual2:
            
                html_content += """
                                    <tr>
                                        <th>
                                            <label class="customcheckbox">
                                                <input type="checkbox" class="listCheckbox">
                                                <span class="checkmark"></span>
                                            </label>
                                        </th>
                                        <td>"""+str(actual2.dato._nombre)+"""</td>
                                        <td>"""+str(actual2.dato._artista)+"""</td>
                                        <td>"""+str(actual2.dato._album)+"""</td>
                                        <td>"""+str(actual2.dato._vecesReproducida)+"""</td>
                                    </tr>
                                    """
                actual2 = actual2.siguiente
            html_content += """
                                    <!-- Agrega más filas de la tabla aquí -->
                                </tbody>
                            </table>
            """
                
            actual = actual.siguiente
            html_content += """
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
            

    # Escribe el contenido HTML en un archivo HTML
        with open('reporteHTML.html', 'w') as html_file:
            html_file.write(html_content)

    # Abre el archivo HTML en el navegador predeterminado
        webbrowser.open('reporteHTML.html')