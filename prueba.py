import PySimpleGUI as sg
import xml.etree.ElementTree as ET
from graphviz import Digraph

# Parse XML
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Create list for product data
    product_list = []

    # Parse product data
    for product in root.findall('producto'):
        product_data = {
            'nombre': product.get('nombre'),
            'precio': product.get('precio'),
            'cantidad': product.get('cantidad'),
        }
        product_list.append(product_data)

    return product_list

# Function to show products
def show_products(product_list):
    layout = [[sg.Table(values=product_list, headings=['Nombre', 'Precio', 'Cantidad'],
                         auto_size_columns=True, justification='center')],
              [sg.Button('Back', key='back')]]
    window = sg.Window('Productos', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'back':
            break
    window.close()

# Function to search product
def search_product(product_list):
    layout = [[sg.Input(key='input')],
              [sg.Button('Search'), sg.Button('Back', key='back')]]
    window = sg.Window('Buscar producto', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'back':
            break
        if event == 'Search':
            product_found = False
            for product in product_list:
                if product['nombre'] == values['input']:
                    product_found = True
                    sg.popup('Nombre: {}\nPrecio: {}\nCantidad: {}'.format(product['nombre'], product['precio'], product['cantidad']))
                    break
            if not product_found:
                sg.popup('Producto no encontrado')
    window.close()

# Function to generate graph
def generate_graph(product_list):
    graph = Digraph('productos', filename='productos.gv')
    for product in product_list:
        graph.node(product['nombre'], label='{}\nPrecio: {}\nCantidad: {}'.format(product['nombre'], product['precio'], product['cantidad']))
    graph.view()

# Main
def main():
    # Read XML
    product_list = parse_xml('productos.xml')

    # Create layout
    layout = [[sg.Text('Seleccione una opción:')],
              [sg.Button('Mostrar productos'), sg.Button('Buscar producto'), sg.Button('Generar grafo')],
              [sg.Button('Salir', key='exit')]]

    # Create window
    window = sg.Window('Inventario', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'exit':
            break
        if event == 'Mostrar productos':
            show_products(product_list)
        if event == 'Buscar producto':
            search_product(product_list)
        if event == 'Generar grafo':
            generate_graph(product_list)

    window.close()

if __name__ == '__main__':
    main()