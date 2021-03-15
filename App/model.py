"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def initCatalog():
    catalog = {"categorias": None
                "videos_por_categoria": None}

    catalog["categorias"]=lt.newList(datastructure='ARRAY_LIST')
    catalog["videos_por_categoria"]= mp.newMap(30,
                                            maptype='PROBING',
                                            loadfactor=0.5)

    return catalog

# Funciones para agregar informacion al catalogo
def addcategory(catalog, categoria):
    lt.addLast(catalog["categorias"], categoria)

def addvideo(catalog, video):
    c = catalog['videos_por_categoria']
    categoria = nombrecategoria(catalog, video["category_id"])
    existecategoria = mp.contains(c, categoria)
    if existecategoria:
        entrada = mp.get(c, categoria)
        videos = me.getValue(entrada)
    else:
        videos = newcategory(categoria)
        mp.put(c, categoria, videos)
    lt.addLast(videos['videos'], video)

# Funciones para creacion de datos
def newcategory(categoria):
    entrada = {'categoria': "", "videos": None}
    entrada['categoria'] = categoria
    entrada['videos'] = lt.newList(datastructure='ARRAY_LIST')
    return entrada

# Funciones de consulta
def nombrecategoria(catalog, idcategoria):
    categorias = catalog["categorias"]
    for i in range(lt.size(categorias)):
        a = lt.getElement(categorias,i)
        if idcategoria == a["id"]:
            return a["name"]

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
