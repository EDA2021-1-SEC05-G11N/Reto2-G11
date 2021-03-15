"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos con mas likes por categoria")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información en el catalogo ....")
        catalog = controller.initCatalog()
        controller.cargarinfocatalogo(catalog)
        print("Se cargó la información al catalogo")
        print("Categorias cargadas: " + str(controller.sizecategorias(catalog)))
        #print("Videos cargados: " + str(controller.sizevideos(catalog)))
        #a = catalog["videos_por_categoria"]
        #print(mp.get(a, "music"))

    elif int(inputs[0]) == 2:
        categoria = input("Ingrese la categoria que desea consultar: ")
        numero = int(input("Ingrese el numero de videos que desea consultar: "))
        videos = controller.videos_likes_categoria(catalog, categoria, numero)
        print("La información de los  " + str(numero) + " videos con mas likes para la categoria " + categoria + " es: ")
        print(videos)
    else:
        sys.exit(0)
sys.exit(0)
