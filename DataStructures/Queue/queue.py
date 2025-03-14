import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..')))

from DataStructures.List import single_linked_list as sll

def new_queue():
    """
    Crea una nueva cola vacía basada en una lista enlazada simple,
    usando la función sll.new_list().
    Returns:
        dict: El diccionario que retorna sll.new_list(), por ejemplo:
              {
                  'size': 0,
                  'first': None,
                  'last': None
              }
    """
    return sll.new_list()

def enqueue(my_queue, element):
    """
    Añade el elemento 'element' al final de la cola 'my_queue'.
    Parameters:
        my_queue (dict): Estructura de cola que internamente es una single_linked_list,
                         por ejemplo:
                         {
                             'size': 0,
                             'first': None,
                             'last': None,
                         }
        element (any): Elemento que se añadirá a la cola. 
    Returns:
        dict: La cola actualizada (my_queue).
    """ 
    sll.add_last(my_queue, element)
    return my_queue

def dequeue(my_queue):
    """
    Elimina el elemento al inicio de la cola 'my_queue' y lo retorna.
    Parameters:
        my_queue (dict): Estructura de cola que internamente es una single_linked_list,
                         por ejemplo:
                         {
                             'size': 0,
                             'first': None,
                             'last': None,
                         }
    Returns:
        any: Elemento eliminado de la cola.
    """
    return sll.remove_first(my_queue)

def peek(my_queue):
    """
    Retorna el elemento al inicio de la cola 'my_queue' sin eliminarlo.
    Parameters:
        my_queue (dict): Estructura de cola que internamente es una single_linked_list,
                         por ejemplo:
                         {
                             'size': 0,
                             'first': None,
                             'last': None,
                         }
    Returns:
        any: Elemento al inicio de la cola.
    """
    return sll.first_element(my_queue)

def is_empty(my_queue):
    """
    Verifica si la cola 'my_queue' está vacía.
    Parameters:
        my_queue (dict): Estructura de cola que internamente es una single_linked_list,
                         por ejemplo:
                         {
                             'size': 0,
                             'first': None,
                             'last': None,
                         }
    Returns:
        bool: True si la cola está vacía, False de lo contrario.
    """
    return sll.is_empty(my_queue)

def size(my_queue): 
    """
    Retorna la cantidad de elementos en la cola 'my_queue'.
    Parameters:
        my_queue (dict): Estructura de cola que internamente es una single_linked_list,
                         por ejemplo:
                         {
                             'size': 0,
                             'first': None,
                             'last': None,
                         }
    Returns:
        int: Cantidad de elementos en la cola.
    """
    return sll.size(my_queue)