import random
import PySimpleGUI as sg
import SG as acceso
import Logic as logic
import listaCircular as lista
from bs4 import BeautifulSoup
# Configurar el tema
sg.theme("LightGreen4")

#   BOTONES CON EMOJIS
def emoji_button(emoji, size):
    return sg.Button(emoji, size=size, button_color=("white", "#1DB954"))

# Inicializar la lista doblemente enlazada circular

nombres_listas = []


lista_canciones = acceso.lista_reproduccion
nombreListaReproductor = "ListaDefecto"


logic.leerEntradaListaReproduccion()

# Inicializar la referencia a la canción actual y posición actual
cancion_actual = None
posicion_actual = 0


def guardar_cancion():
    #Limpiar combos
    acceso.lista_cancionesMostrar = lista.ListaDobleEnlazada()

    acceso.lista_artistas.generarCanciones()

    lista_canciones_actual = acceso.lista_cancionesMostrar.obtener_lista()
    lista_reproduccion = lista_canciones.obtener_lista()
    #COMBO BOX CON EL LISTADO DE CAANCIONES CARGADAS
    combo_canciones = sg.Combo(values=[f"{cancion._artista} - {cancion._album} - {cancion._nombre}" for cancion in lista_canciones_actual], key="-COMBO_CANCIONES-")
    combo_listas = sg.Combo(values=[f"{lista._nombre}" for lista in lista_reproduccion], key="-LISTA_NOMBRE-")
    layout_lista = [
        [sg.Text("Nombre de la lista:"), combo_listas],
        [sg.Text("Seleccionar canción:"), combo_canciones],
        [sg.Button("Agregar canción", key="-AGREGAR_CANCION-")],
    ]

    window_lista = sg.Window("Crear lista", layout_lista, finalize=True)

    canciones_seleccionadas = []

    while True:
        event_lista, values_lista = window_lista.read()

        if event_lista == sg.WINDOW_CLOSED:
            break
        elif event_lista == "-AGREGAR_CANCION-":
            
            cancion_seleccionada = values_lista["-COMBO_CANCIONES-"]
            if cancion_seleccionada:
                nombre_lista = values_lista["-LISTA_NOMBRE-"]
                print
                if lista_canciones.validarNombreListaReproduccion(nombre_lista):
                    print("Selecccionado:", cancion_seleccionada)
                    artista = cancion_seleccionada.split(" - ")[0]
                    album = cancion_seleccionada.split(" - ")[1]
                    cancion = cancion_seleccionada.split(" - ")[2]
                    print ("artista", artista)
                    print ("album", album)
                    print ("cancion", cancion)
                    if lista_canciones.buscarValidarCancionListaReproduccion(nombre_lista, artista, album, cancion):
                        sg.popup(f"La cancion ya existe en la lista de reproduccion", title="Error")
                    else:
                        sg.popup(f"La cancion es;: {cancion_seleccionada}", title="Éxito")
                        cancionObtenida = acceso.lista_artistas.obtenerCancionArtista(artista, album, cancion)
                        logic.guardarCancionListaReproduccion(nombre_lista, cancionObtenida)
                        print("---Cancion agregada----")
                        acceso.lista_reproduccion.mostrar_listaReproduccion()
                        sg.popup("cancion agregada", title="Éxito")
                        
                    
                
                
        elif event_lista == "-GUARDAR_LISTA-":
            nombre_lista = values_lista["-LISTA_NOMBRE-"]

            # VERIFICACION DE NOMBRE EXISTENTE
            if lista_canciones.validarNombreListaReproduccion(nombre_lista):
                sg.popup(f"La cancon es;: {canciones_seleccionadas}", title="Éxito")
            else:
                # GUARDAR NUEVO NOMBRE
                nombres_listas.append(nombre_lista)
                sg.popup(f"Lista '{nombre_lista}' creada correctamente con canciones: {', '.join(canciones_seleccionadas)}", title="Éxito")

                # Actualizar los valores del Combo
                window["-COMBO_PLAYLIST-"].update(values=nombres_listas)
                
                break

    window_lista.close()

def crear_listas():
    # Obtener la lista de canciones

    #COMBO BOX CON EL LISTADO DE CAANCIONES CARGADAS
    

    layout_lista = [
        [sg.Text("Nombre de la lista:"), sg.Input(key="-LISTA_NOMBRE-")],
        [sg.Button("Guardar lista", key="-GUARDAR_LISTA-")]
    ]

    window_lista = sg.Window("Crear lista", layout_lista, finalize=True)



    while True:
        event_lista, values_lista = window_lista.read()

        if event_lista == sg.WINDOW_CLOSED:
            break
        elif event_lista == "-GUARDAR_LISTA-":
            nombre_lista = values_lista["-LISTA_NOMBRE-"]

            # VERIFICACION DE NOMBRE EXISTENTE
            if lista_canciones.validarNombreListaReproduccion(nombre_lista):
                sg.popup(f"Ya existe una lista con el nombre '{nombre_lista}'. Por favor, ingresa otro nombre de playlist", title="Error")
                nombres_listas.append(nombre_lista)
                window["-COMBO_PLAYLIST-"].update(values=nombres_listas)
            else:
                # GUARDAR NUEVO NOMBRE
                logic.crearListaReproduccion(nombre_lista)
                sg.popup(f"Lista '{nombre_lista}' creada correctamente", title="Éxito")
                nombres_listas.append(nombre_lista)
                window["-COMBO_PLAYLIST-"].update(values=nombres_listas)
                break

    window_lista.close()

# lista_canciones.deserializar_desde_xml("default.xml")

#   INTERFAZ
layout = [
    [sg.Text("IPCmusic", font=("Helvetica", 30), justification="center", background_color="#1DB954", text_color="white")],
    
    [
        sg.Image(filename="cancionprueba.png", key="-ALBUM_IMAGE-", size=(200, 200), pad=(0, (0, 20))),  # IMAGEN POR DEFECTO
        sg.Multiline("", key="-SONG_INFO-", size=(40, 7), disabled=True, background_color="#1DB954", text_color="white", justification="center")
    ],
    [
        emoji_button("⏮️", size=(6, 2)),
        emoji_button("▶️", size=(6, 2)),
        emoji_button("⏸️", size=(6, 2)),
        emoji_button("⏭️", size=(6, 2)),
        emoji_button("🔀", size=(6, 2))
    ],
    [
        sg.Button("Cargar Biblioteca", size=(14, 2), button_color=("white", "#1DB954")),
        sg.Button("Crear listas", size=(14, 2), button_color=("white", "#1DB954")),
        sg.Button("Guardar canciones", size=(14, 2), button_color=("white", "#1DB954")),
        sg.Button("Reporte HTML", size=(14, 2), button_color=("white", "#1DB954")),
        sg.Button("Reporte Graphviz", size=(14, 2), button_color=("white", "#1DB954"))
    ],
    [
        sg.Text("Seleccionar playlist:", pad=((10, 0), 0)),
        sg.Combo(values=nombres_listas, key="-COMBO_PLAYLIST-", size=(20, 1)),
        sg.Button("Seleccionar Playlist", size=(12, 1), button_color=("white", "#1DB954"))
    ]
]

window = sg.Window("IPCmusic", layout, element_justification="center", resizable=True, finalize=True, size=(800, 450))

# BUCLE DE EVENTOS

for nombreLista in lista_canciones.obtenerListaReproduccion():
    nombres_listas.append(nombreLista._nombre)
    window["-COMBO_PLAYLIST-"].update(values=nombres_listas)


while True:
    event, values = window.read()


    # --------------EVENTOS DE BOTONES--------------
    if event == sg.WINDOW_CLOSED:
        sg.popup("Gracias por usar IPCmusic", title="Hasta luego")
        acceso.lista_reproduccion.generarArchivoXML()

        break
    elif event == "▶️":  
        # LOGICA PARA REPRODUCIR
        print ("Reproduciendo")
        listaObtenida= lista_canciones.obtenerListaCancionesPorNombre(nombreListaReproductor)
        print (listaObtenida)
        if lista_canciones.inicio and 0 <= posicion_actual < len(listaObtenida):
            cancion_actual = listaObtenida[posicion_actual]
            print (cancion_actual._nombre)
            window["-SONG_INFO-"].update(f"Reproduciendo ahora:\n{cancion_actual._nombre} - {cancion_actual._artista}\n{cancion_actual._album} - {cancion_actual._vecesReproducida} - {cancion_actual._pathImagen} - {cancion_actual._pathCancion}")
            
            reproduciendo = True  
            lista_canciones.actualizarVecesReproducidaNombreLista(nombreListaReproductor, cancion_actual._artista, cancion_actual._album, cancion_actual._nombre, None)

    elif event == "⏸️":  
        # LOGICA PARA PAUSAR
        window["-SONG_INFO-"].update("Pausado")
        reproduciendo = False 

    elif event == "⏭️":  
        # LOGICA PARA SIGUIENTE
        listaObtenida= lista_canciones.obtenerListaCancionesPorNombre(nombreListaReproductor)
        tempCancionActual = None
        if posicion_actual+1 < len(listaObtenida):
            tempCancionActual = listaObtenida[posicion_actual+1]
        if cancion_actual and tempCancionActual:
            cancion_actual = tempCancionActual
            posicion_actual += 1
            window["-SONG_INFO-"].update(f"Siguiente Canción:\n{cancion_actual._nombre} - {cancion_actual._artista}\n{cancion_actual._album} - {cancion_actual._vecesReproducida} - {cancion_actual._pathImagen} - {cancion_actual._pathCancion}")
            
            reproduciendo = True  
            lista_canciones.actualizarVecesReproducidaNombreLista(nombreListaReproductor, cancion_actual._artista, cancion_actual._album, cancion_actual._nombre, None)

    elif event == "⏮️": 
        # LOGICA PARA ANTERIOR
        listaObtenida= lista_canciones.obtenerListaCancionesPorNombre(nombreListaReproductor)
        tempCancionActual = None
        if posicion_actual-1 >= 0:
            tempCancionActual = listaObtenida[posicion_actual-1]
        if cancion_actual and tempCancionActual:
            cancion_actual = tempCancionActual
            posicion_actual -= 1
            window["-SONG_INFO-"].update(f"Siguiente Canción:\n{cancion_actual._nombre} - {cancion_actual._artista}\n{cancion_actual._album} - {cancion_actual._vecesReproducida} - {cancion_actual._pathImagen} - {cancion_actual._pathCancion}")
            
            reproduciendo = True  
            lista_canciones.actualizarVecesReproducidaNombreLista(nombreListaReproductor, cancion_actual._artista, cancion_actual._album, cancion_actual._nombre, None)

    elif event == "🔀": 
        # LOGICA PARA REPRODUCCIÓN ALEATORIA
        if lista_canciones.inicio:
            listaObtenida= lista_canciones.obtenerListaCancionesPorNombre(nombreListaReproductor)
            cancion_actual = random.choice(listaObtenida)
            posicion_actual = listaObtenida.index(cancion_actual)
            window["-SONG_INFO-"].update(f"Reproduccion aleatoria:\n{cancion_actual._nombre} - {cancion_actual._artista}\n{cancion_actual._album} - {cancion_actual._vecesReproducida} - {cancion_actual._pathImagen} - {cancion_actual._pathCancion}")
            
            reproduciendo = True
            lista_canciones.actualizarVecesReproducidaNombreLista(nombreListaReproductor, cancion_actual._artista, cancion_actual._album, cancion_actual._nombre, None)
    
    elif event == "Cargar Biblioteca": 
        # CARGA DE ARCHIVO XML

        print("Cargando biblioteca...")
        path = sg.popup_get_file("Selecciona el archivo XML", title="Cargar biblioteca", file_types=(("XML Files", "*.xml"),))
        if path:
            sg.popup("Biblioteca cargada correctamente", title="Éxito")
            nombres_listas.clear()
            nombres_listas.append("ListaDefecto")
            window["-COMBO_PLAYLIST-"].update(values=nombres_listas)
            logic.leerEntrada(path)
            logic.crearListaReproduccionDefecto()
            
            ##ÑCrea la lista por defecto
            acceso.lista_reproduccion.mostrar_listaReproduccion()
            ###

            posicion_actual = 0
        else:
            sg.popup("No se seleccionó ningún archivo", title="Error") 
            
        
    elif event == "Seleccionar Playlist":
        # LOGICA PARA SELECCIONAR PLAYLIST
        print("Seleccionado:")
        nombre = values["-COMBO_PLAYLIST-"]
        print(nombre)
        nombreListaReproductor = nombre
        sg.popup(f"Seleccionado: {nombre}", title="Éxito")


    elif event == "Crear listas":
        # ABRIR APARTADO DE CREAR LISTAS
        crear_listas()
    elif event == "Reporte HTML":
        # LOGICA PARA GENERAR REPORTE HTML
        acceso.lista_reproduccion.generarReporteHTML()
        



        
    elif event == "Reporte Graphviz":
        # LOGICA PARA GENERAR REPORTE GRAPHVIZ
        acceso.lista_reproduccion.generarGraficaPlaylist()
        sg.popup("Reporte generado correctamente", title="Éxito")


    elif event == "Guardar canciones":
        guardar_cancion()

    

# Cerrar la ventana al salir del bucle
window.close()