from classes import *
from tudor import *
from ariel import demana_seient
from typing import Optional


#==========================================================================================================
# Reserva d'una pel·lícula
#==========================================================================================================
@dataclass
class Resultat:
    '''Esta classe és una classe temporal que s'utilitza per a filtrar sessions'''
    cine: Cine
    sala: Sala
    sessio: Sessio

#------------------------------------------------------------------------
# def busca_sessions_on_vore_pel_licula(pel_licula:Pel_licula, data_hora:dt.date|None = None) -> list[Resultat]:
def busca_sessions_on_vore_pel_licula(pel_licula:Pel_licula, data_hora:Optional[dt.date] = None) -> list[Resultat]:
    ''' Recorre els cines i les seues sales buscant aquelles sessions on es projecta una pelicula determinada, de manera 
        opcional també es pot filtrar per una data determinada. El resultat es guarda en una lista de objectes
        Resultat que guarda el cine i la sessió que casen amb el filtre de pel·lícula i data/hora indicats.
        Retorna esta llista de (cine, sala, sessió)
    '''
    lista = []
    for cine in cines:
        for sala in cine.sales:
            for sessio in sala.sessions:
                if (sessio.pel_licula==pel_licula) and (not data_hora or data_hora==sessio.data_hora.date()):
                    lista.append(Resultat(cine,sala,sessio))
                    
    return lista
            

        


#------------------------------------------------------------------------
def selecciona_sessio_on_vore_pel_licula(pel_licula:Pel_licula, data:Optional[dt.date]=None) -> tuple[Sala,Sessio]:
    ''' Busca i mostrar els cines i les sesions que projecten la pel·lícula indicada i, opcionalment, en la data indicada.
    A continuació, sol·licita l'id d'una d'este sessions. Retorna la sala i la sessió seleccionades.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''
    while True:
        lista = busca_sessions_on_vore_pel_licula(pel_licula,data)

        for element in lista:
            print(f'Cine:{element.cine.descripcio} -> Sala:{element.sala.descripcio} -> Data:{element.sessio.data_hora}\n Nº de sessió:{element.sessio.id}\n\n')
        while True:
            id = input_type(' Introdueïx el id de la pel·lícula que vols vore: ','int')
        
            for x in lista:
                if x.sessio.id == id:
                    return x.sala,x.sessio
            print('ID no existeix')


        
        

#------------------------------------------------------------------------
def reserva_pel_licula() -> None:
    ''' Mostra la llista de pel·lícules.
    Demana l'id d'una pel·lícula i una data (ddmmaa).
    Busca en totes les sales aquelles sessions que projecten la pel·lícula i, opcionalment, en la data indicada.
    Pregunta que seleccionem la sessió en què volem fer una reserva. 
    Fa una reserva en esta sessió. Per a fer-la mostra una llista de les reserves, demana una fila i un seient.
    Demana un dni per a la reserva i assigna la reserva a la fila/seient indicades. Grava els canvis en disc.
    Si polsem intro eixem del procés de reserva.
    '''

    msg_error = ''
    while True:

        try:

            print(msg_error)
            msg_error = ''

            mostra_pel_licules()

            pel_licula = demana_pel_licula('Introdueïx el ID de la pel·lícula que vols vore:')
            if pel_licula == '':
                break
            
            data = obtin_data()
            
            sala , sessio = selecciona_sessio_on_vore_pel_licula(pel_licula,data)
            reserva_pel_licula_en_sessio(sala , sessio)

        except pelicula_no_trobada:
            msg_error = "No s'ha trobat la pel·lícula\n"

        except input_type_cancel·lat:
            msg_error = '\n'

        except sessio_no_trobada:
            msg_error = 'No es troba la sessió\n'

#------------------------------------------------------------------------
def reserva_pel_licula_en_sessio(sala:Sala, sessio:Sessio) -> None:
    ''' Mostra una llista de reserves de la sessió indicada.
    Demana fila i seient on volem fer la reserva. Si la fila/seient ja estan reservats mostra un missate indicant-ho.
    Si la fila/seient esta lliures, demana un dni, crea la reserva i l'assigna a la fila/seient.
    Grava els canvis en disc. Si polsem intro eixem del procés de reserva.
    '''
    msg_error = ''
    while True:
        cls(f'{sessio.pel_licula.info}  {sessio.preu_entrada}  {msg_error}')
        msg_error = ''
        sessio.mostra_reserves()
    
        fila , seient = demana_seient(sala)

        if not sessio.reserves[fila][seient]:
            dni = input_type('DNI per a la reserva:')
            confirmacio = input_type('Vols comprar la entrada? (S/N)', 'str', 'False', 'False')
            if confirmacio.upper() == 'S':
                sessio.reserves[fila][seient] = Reserva(dni)
                grava_arxiu()
                input_type('Reserva realitzada', excepcio= 'False', intro_cancellar= 'False')
                break
            elif confirmacio.upper() == 'N':
                break
            else:
                msg_error = 'Incorrecte'
        else:
            msg_error = 'Seient ocupat'


