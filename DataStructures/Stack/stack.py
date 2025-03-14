import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from DataStructures.List import array_list as al

def new_stack():
    """
    Crea una nueva pila vacía basada en una lista enlazada simple,
    usando la función al.new_list().
    Returns:
        dict: El diccionario que retorna sll.new_list(), por ejemplo:
              {
                  'size': 0,
                  'elements': []
              }
    """
    return al.new_list()

def push(my_stack, element):
    """
    Añade el elemento 'element' al tope de la pila 'my_stack'.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
        element (any): Elemento que se añadirá a la pila.
    Returns:
        dict: La pila actualizada (my_stack).
    """
    al.add_last(my_stack, element)
    return my_stack

def pop(my_stack):
    """
    Elimina el elemento en el tope de la pila 'my_stack' y lo retorna.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
    Returns:
        any: Elemento eliminado de la pila.
    """
    return al.remove_last(my_stack)

def is_empty(my_stack):
    """
    Verifica si la pila 'my_stack' está vacía.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 0,
                             'elements': []
                         }
    Returns:
        bool: True si la pila está vacía, False de lo contrario.
    """
    return al.is_empty(my_stack)

def top(my_stack):
    """
    Retorna el elemento en el tope de la pila 'my_stack'.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
    Returns:
        any: Elemento en el tope de la pila.
    """
    return al.last_element(my_stack)

def size(my_stack):
    """
    Retorna la cantidad de elementos en la pila 'my_stack'.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
    Returns:
        int: Cantidad de elementos en la pila.
    """
    return al.size(my_stack)