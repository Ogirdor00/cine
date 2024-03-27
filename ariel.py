from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime as dt
import os
import platform
import pickle
from plantilaa import *


#==========================================================================================================
# Manteniment sessions i reserves
#==========================================================================================================
# === === === === === ===    
def mostra_cine_i_sales() -> None:
    print("--- LLISTA CINES ---")
    print('')
    print('-----------------------------------')
    print('')

    for cine in cines:
        print(f'{cine.descripcio} id: {cine.id}')

        for sala in cine.sales:
            print(f"{sala.descripcio}. Id: {sala.id}.")

    

    return

def busca_cine(id:int) -> Cine: #busca un cine pel seu id en la llista de cines, se la troba retorna el cine, sino llança excepcio de cine_no_trobat
    
    
    for cine in cines:
        if cine.id == id:
            print("funcione")
            return cine

    raise cine_no_trobat



# === === === === === ===   EL INICI
def selecciona_cine() -> Cine:
    mostra_cine_i_sales()
    id = input_type('ID del cine a buscar: ', type= 'int')      
    cine = busca_cine(id)       # type:ignore

    return cine
    
# === === === === === ===         

def mostra_sales_i_sessions():
    pass








# === === === === === ===    
# manteniment sessions
# === === === === === ===        





# def mostra_menu() -> None:
#     '''Mostra el menú principal. El primer punt no està implementat. Per a simplificar assumirem
#     que tenim 2 cines amb dos sales cadascuna.'''
#     while True:
#         cls('- MENÚ PRINCIPAL -')
#         print('------------------')
#         print('1- Cines i sales (no implementat)')
#         print('2- Manteniment de pel·lícules')
#         print('3- Manteniment sessions i reserves')
#         print('4- Reservar una pel·lícula')
#         print()

#         try:
#             opc = input_type('Opció?', intro_cancellar=False)
#             if opc=='1':
#                 pass                            # Opció no implementada
#             elif opc=='2':
#                 pass
#             elif opc=='3':
#                 cine = selecciona_cine()
#                 manteniment_sessions(cine)
#             elif opc=='4':
#                 pass
#         except input_type_cancel·lat:
#             continue


if __name__ == "__main__":
    llig_arxiu()

x = input("Pulsa la tecla 3")
if x == "3":
    selecciona_cine()

