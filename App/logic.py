"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 * Lina Ojeda
 """

import csv
import os
import time
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as lt

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/GoodReads'

sort_algorithm = None
data_structure = None


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def new_logic(user_data_structure):
    """
    Inicializa el catálogo de libros. Crea una lista vacía para guardar
    todos los libros, autores, géneros y la asociación de géneros y libros,
    utilizando la estructura de datos seleccionada.
    """
    global data_structure
    if user_data_structure == "1":
        data_structure = al
    else:
        data_structure = lt

    catalog = {"books": None,
               "authors": None,
               "tags": None,
               "book_tags": None}

    # Usamos la estructura seleccionada para inicializar todas las listas
    catalog["books"] = data_structure.new_list()
    # TODO: completar la creacion de la lista de autores
    catalog["authors"] = data_structure.new_list()
    catalog["tags"] = data_structure.new_list()
    catalog["book_tags"] = data_structure.new_list()
    return catalog

#  -------------------------------------------------------------
# Funciones para la carga de datos
#  -------------------------------------------------------------


def load_data(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    books, authors = load_books(catalog)
    tag_size = load_tags(catalog)
    book_tag_size = load_books_tags(catalog)
    return books, authors, tag_size, book_tag_size


def load_books(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = data_dir + '/books.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        add_book(catalog, book)
    return book_size(catalog), author_size(catalog)


def load_tags(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = data_dir + '/tags.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        add_tag(catalog, tag)
    return tag_size(catalog)


def load_books_tags(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    bookstagsfile = data_dir + '/book_tags.csv'  # TODO: completar la ruta del archivo de BOOKS_TAGS
    input_file = csv.DictReader(open(bookstagsfile, encoding='utf-8'))
    for booktag in input_file:
        add_book_tag(catalog, booktag)
    return book_tag_size(catalog)


#  -------------------------------------------------------------
# Funciones para creacion de datos
#  -------------------------------------------------------------
def new_author(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {"name": "", "books": None,  "average_rating": 0}
    author["name"] = name
    author["books"] = data_structure.new_list()
    return author


def new_tag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {"name": "", "tag_id": ""}
    tag["name"] = name
    tag["tag_id"] = id
    return tag


def new_book_tag(tag_id, book_id, count):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    book_tag = {'tag_id': tag_id, 'book_id': book_id, 'count': count}
    return book_tag


#  -------------------------------------------------------------
# funciones de configuracion para los algoritmos de ordenamiento
#  -------------------------------------------------------------

def select_sort_algorithm(algo_opt):
    """select_sort_algorithm permite seleccionar el algoritmo de ordenamiento
    para la lista.

    Args:
        algo_opt (int): opcion de algoritmo de ordenamiento, las opciones son:
            1. Selection Sort
            2. Insertion Sort
            3. Shell Sort
            4. Merge Sort
            5. Quick Sort

    Returns:
        list: sort_algorithm (sort) la instancia del ordenamiento y
        algo_msg (str) el texto que describe la configuracion del ordenamiento
    """

    # respuestas por defecto
    global sort_algorithm
    sort_algorithm = None
    algo_msg = None

    # selecciona el algoritmo de ordenamiento

    # opcion 1: Selection Sort
    if algo_opt == 1:
        sort_algorithm = 1
        algo_msg = "Seleccionó la configuración - Selection Sort"

    # opcion 2: Insertion Sort
    # TODO: completar la opcion de Insertion Sort
    elif algo_opt == 2:
        sort_algorithm = 2
        algo_msg = "Seleccionó la configuración - Insertion Sort"

    # opcion 3: Shell Sort
    # TODO: completar la opcion de Shell Sort
    elif algo_opt == 3:
        sort_algorithm = 3
        algo_msg = "Seleccionó la configuración - Shell Sort"

    # opcion 4: Merge Sort
    # TODO: completar la opcion de Merge Sort
    elif algo_opt == 4:
        sort_algorithm = 4
        algo_msg = "Seleccionó la configuración - Merge Sort"
    # opcion 5: Quick Sort
    # TODO: completar la opcion de Quick Sort
    elif algo_opt == 5:
        sort_algorithm = 5
        algo_msg = "Seleccionó la configuración - Quick Sort"
        
    else:
        algo_msg = "No seleccionó una configuración válida"

    # respuesta final: algoritmo de ordenamiento y texto de configuracion
    return sort_algorithm, algo_msg


def set_book_sublist(catalog, size):
    """
    Crea una sublista de libros de tamaño size
    """
    books = catalog["books"]
    catalog["book_sublist"] = data_structure.sub_list(books, 0, size)
    return catalog

#  -------------------------------------------------------------
# Funciones de consulta
#  -------------------------------------------------------------


def get_books_by_author(catalog, author_name):
    """
    Retrona los libros de un autor
    """
    pos_author = pos_author = data_structure.is_present(catalog['authors'], author_name, compare_authors)
    if pos_author > 0:
        author = data_structure.get_element(catalog['authors'], pos_author)
        return author
    return None


def get_book_info_by_book_id(catalog, book_id):
    """
    Retorna toda la informacion que se tenga almacenada de un libro segun su titulo.
    """
    pos_book = data_structure.is_present(
        catalog['books'], book_id, compare_book_ids)
    if pos_book >= 0:
        book = data_structure.get_element(catalog['books'], pos_book)
        return book
    return None


def count_books_by_tag(catalog, tag_name):
    """
    Retorna el número de libros que fueron etiquetados con el tag_name especificado.
    """
    # Buscar la posición del tag en la lista de tags usando compare_tag_names
    pos_tag = data_structure.is_present(
        catalog['tags'], tag_name, compare_tag_names)

    # Si el tag existe
    if pos_tag >= 0:
        # Obtener el tag completo (tag_id y tag_name)
        tag = data_structure.get_element(
            catalog['tags'], pos_tag)  # Ajustar para índice 0
        tag_id = tag['tag_id']

        # Inicializar contador de libros y una lista para IDs de libros únicos
        total_processed = 0  # Contador para el total de book_tags procesados

        # Recorrer la lista de book_tags para contar las coincidencias con ese tag_id
        for i in range(data_structure.size(catalog['book_tags'])):
            book_tag = data_structure.get_element(catalog['book_tags'], i)
            if book_tag is not None and book_tag['tag_id'] == tag_id:
                total_processed += 1  # Incrementar el contador de book_tags procesados

        return total_processed
    # Si el tag no existe
    return 0

#  -------------------------------------------------------------
# Funciones utilizadas para obtener el tamaño de las listas
#  -------------------------------------------------------------


def book_size(catalog):
    # TODO: completar la funcion para obtener el tamaño de la lista de libros
    return data_structure.size(catalog["books"])



def author_size(catalog):
    # TODO: completar la funcion para obtener el tamaño de la lista de autores
    return data_structure.size(catalog["authors"])


def tag_size(catalog):
    # TODO: completar la funcion para obtener el tamaño de la lista de tags
    return data_structure.size(catalog["tags"])


def book_tag_size(catalog):
    return data_structure.size(catalog["book_tags"])

#  -------------------------------------------------------------
# Funciones utilizadas para comparar elementos dentro de una lista
#  -------------------------------------------------------------


def compare_authors(author, author_name1):
    if author_name1.lower() == author['name'].lower():
        return 0
    elif author_name1.lower() > author['name'].lower():
        return 1
    return -1


def compare_tag_names(tag, name):
    if (name == tag['name']):
        return 0
    elif (name > tag['name']):
        return 1
    return -1


def compare_book_ids(book, id):
    if id == book["goodreads_book_id"]:
        return 0
    elif id > book["goodreads_book_id"]:
        return 1
    else:
        return -1

#  -----------------------------------------------
# funciones para comparar elementos dentro de algoritmos de ordenamientos
#  -----------------------------------------------


def eval_ratings(book1, book2):
    # TODO: completar la función para comparar dos libros por su rating promedio, el libro 1 debe ser mayor al 2.
    if book1["average_rating"] > book2["average_rating"]:
        return True
    else:
        return False

#  -----------------------------------------------
# Funciones de ordenamiento
#  -----------------------------------------------


def sort_books(catalog):

    sorted_books = catalog["book_sublist"]
    start_time = get_time()

    # TODO: completar las opciones para selection_sort, insertion_sort, shell_sort, merge_sort y quick_sort

    if sort_algorithm == 1:
        # TODO: completar la llamada a selection_sort
        sorted_books_s = data_structure.selection_sort(sorted_books, eval_ratings)

    elif sort_algorithm == 2:
        # TODO: completar la llamada a insertion_sort
        sorted_books_s = data_structure.insertion_sort(sorted_books, eval_ratings)

    elif sort_algorithm == 3:
        # TODO: completar la llamada a shell_sort
        sorted_books_s = data_structure.shell_sort(sorted_books, eval_ratings)

    elif sort_algorithm == 4:
        # TODO: completar la llamada a merge_sort
        sorted_books_s = data_structure.merge_sort(sorted_books, eval_ratings)

    elif sort_algorithm == 5:
        # TODO: completar la llamada a quick_sort
        sorted_books_s = data_structure.quick_sort(sorted_books, eval_ratings)

    end_time = get_time()
    delta = delta_time(start_time, end_time)

    return sorted_books_s, delta


#  -----------------------------------------------
#  Funciones para agregar informacion al catalogo
#  -----------------------------------------------

def add_book(catalog, book):
    # Se adiciona el libro a la lista de libros
    book["goodreads_book_id"] = int(book["goodreads_book_id"])
    data_structure.add_last(catalog['books'], book)
    # Se obtienen los autores del libro
    authors = book['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        add_book_author(catalog, author.strip(), book)
    return catalog


def add_book_author(catalog, author_name, book):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    pos_author = data_structure.is_present(
        authors, author_name, compare_authors)
    if pos_author > 0:
        author = data_structure.get_element(authors, pos_author)
    else:
        author = new_author(author_name)
        data_structure.add_last(authors, author)
    data_structure.add_last(author['books'], book)
    return catalog


def add_tag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = new_tag(tag['tag_name'], tag['tag_id'])
    data_structure.add_last(catalog['tags'], t)
    return catalog


def add_book_tag(catalog, book_tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = new_book_tag(book_tag['tag_id'],
                     book_tag['goodreads_book_id'], book_tag['count'])
    data_structure.add_last(catalog['book_tags'], t)
    return catalog

#  -----------------------------------------------
#  Funciones para toma de tiempos
#  -----------------------------------------------


def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
