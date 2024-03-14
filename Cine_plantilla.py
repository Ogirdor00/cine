from __future__ import annotations
from dataclasses import dataclass
import datetime as dt
import os
import platform
import pickle

#==========================================================================================================
# Excepcions
#==========================================================================================================
class pelicula_no_trobada(Exception):           # type: ignore
    pass
class sessio_no_trobada(Exception):
    pass
class sala_no_trobada(Exception):
    pass
class cine_no_trobat(Exception):
    pass
class input_type_cancel·lat(Exception):
    pass
class pel_licula_utilitzada_en_una_sessio(Exception):
    pass

#==========================================================================================================
# VARIABLES GLOBALS
#==========================================================================================================
pel_licules:list[Pel_licula] = []
cines:list[Cine] = []

#==========================================================================================================
# CLASSES
#==========================================================================================================
class Reserva:
    def __init__(self, dni:str) -> None:
        self.dni = dni

    def __str__(self) -> str:
        return self.dni
    
    __repr__ = __str__

#==========================================================================================================
class Pel_licula:
    id:int = 1
    def __init__(self, info:str) -> None:
        self.id = Pel_licula.id
        Pel_licula.id += 1
        self.info = info

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Pel_licula):
            return False
        return obj.id==self.id
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Pel_licula.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Pel_licula.id = state['id_']

#==========================================================================================================
class Cine:
    id:int = 1
    def __init__(self, descripcio:str) -> None:
        self.id = Cine.id
        Cine.id += 1
        self.descripcio = descripcio
        self.sales:list[Sala] = []

    def busca_sala(self, id_sala:int) -> Sala:
        '''Busca una sala pel seu id en la llista de sales del cine.
        Si la troba retorna la llista, sinó llança l'excepció 'sala_no_trobada'
        '''
        for sala in self.sales:
            if sala.id == id_sala:
                return sala
        raise sala_no_trobada
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Cine.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Cine.id = state['id_']

#==========================================================================================================
class Sala:
    id:int = 1
    def __init__(self, cine: Cine, descripcio:str, files: int, seients_per_fila:int) -> None:
        self.id = Sala.id
        Sala.id += 1
        self.descripcio = descripcio
        self.files = files
        self.seients_per_fila = seients_per_fila
        self.sessions:list[Sessio] = []
        cine.sales.append(self)
    
    def busca_sessio(self, id_sessio: int) -> Sessio:
        ''' Busca una sessio pel seu id en la llista de sessions de la sala.
        Si la troba retorna la sala, sinó llança l'excepció 'sessio_no_trobada'
        '''
        for sessio in self.sessions:
            if sessio.id==id_sessio:
                return sessio
        raise sessio_no_trobada
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Sala.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Sala.id = state['id_']

#==========================================================================================================
class Sessio:
    id:int = 1
    def __init__(self, sala:Sala, data_hora:dt.datetime, pel_licula:Pel_licula, preu_entrada:float) -> None:
        self.id = Sessio.id
        Sessio.id += 1
        self.data_hora:dt.datetime = data_hora
        self.pel_licula = pel_licula
        self.preu_entrada = preu_entrada
        self.reserves:list[list[Reserva|None]] = [[None] * sala.seients_per_fila for _ in range(sala.files)]
        sala.sessions.append(self)
    
    def mostra_reserves(self) -> None:
        '''Mostra per pantalla les reserves de la sessió per fila '''
        for i, fila in enumerate(self.reserves):
            print(f'fila {i}: {fila}')
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['id_'] = Sessio.id
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        Sessio.id = state['id_']

#==========================================================================================================
# Funcions generals
#==========================================================================================================
def cls(txt:str|None=None):
    comando = 'cls' if platform.system()=='Windows' else 'clear'
    os.system(comando)
    if txt:
        print(txt)

#------------------------------------------------------------------------
def input_type(text:str, type:str='str', excepcio:bool=True, intro_cancellar:bool=True) -> int|str|float|None:
    '''Funció ampliació de l'input de Python. Demana a l'usuari un valor que convertix a un tipus de dada determinat
    segons el valor del paràmetre type, el qual pot ser 'int','str' o 'float'. Si l'usuari no introduix res (intro)
    segons el valor del paràmetre excepcio generarà l'excepció 'input_type_cancel·lat' o retonarà el str ''.
    Al fer l'input mostra de manera automàtica el text (Intro=cancel·lar). Este text es pot ocultar amb el parametre intro_cancellar=False.
    '''

#------------------------------------------------------------------------
def obtin_data() -> dt.date|None:
    ''' Pregunta a l'usuari una data. Verifica que es correcta i avisa si no ho és.
    Retorna una data o None si l'usuari no n'ha introduit cap (fa intro).
    '''

#------------------------------------------------------------------------
def obtin_data_hora() -> dt.datetime:
    ''' Pregunta a l'usuari una data en forma ddmmaa i una hora en forma hhmm.
    Verifica que es la i l'hora són correctes i avisa si no ho és.
    Retorna el datetime corresponent. Si polsem intro llança l'excepció 'input_type_cancel·lat'
    '''

#==========================================================================================================
# Manteniment de pel·lícules
#==========================================================================================================
def menu_pel_licules() -> None:
    ''' Mostra la llista de pel·ícules y després un menú per al seu manteniment.
    El menú permet crear, modificar i esborrar pel·lícules. Si polsem intro tanquem el menú (return).
    No podrem esborrar una pel·lícula que s'estiga projectan en alguna sessió de qualsevol cine.
    '''


#------------------------------------------------------------------------
def mostra_pel_licules() -> None:
    ''' Mostra informació de la llista de pel·lícules (id y info)
    '''


#------------------------------------------------------------------------
def crea_pel_licula() -> None:
    ''' Crea una pel·licula i la grava. Demana la seua descripció.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis.
    '''

#------------------------------------------------------------------------
def busca_pel_licula(id: int) -> Pel_licula:
    ''' Busca una pel·lícula pel seu id en la llista de pel·lícules.
    Si la troba retorna la pel·lícula, sinó llança l'excepció 'pelicula_no_trobada'
    '''

#------------------------------------------------------------------------
def demana_pel_licula(txt:str) -> Pel_licula:
    ''' Demana l'id d'una pel·lícula, la busca en la llista de pel·lícules i retorna la Pel·lícula.
    Si polsem intro llança l'excepció 'input_type_cancel·lat' 
    '''

#------------------------------------------------------------------------
def modifica_pel_licula() -> None:
    ''' Modifica una pel·lícula. Primer demana un id de pel·licula a l'usuari i la busca entre la llista de pel·lícules.
    Demana a l'usuari una descripció nova i la reemplaça la descripció vella. Grava els canvis en disc.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

#------------------------------------------------------------------------
def pel_licula_utilitzada_en_alguna_sessio(pel_licula:Pel_licula) -> bool:
    '''No podem esborrar una pel·lícula si hi ha una sessió en qualsevol sala que la projecta.
    Retorna True si alguna sala la projecta, False si no.
    '''

#------------------------------------------------------------------------
def esborra_pel_licula():
    ''' Esborra una pel·lícula de la llista de pel·lícules. Demana l'id de la pel·licula a esborrar.
    La busca d'entre la llista de pel·lícules. Avisa si la pel·lícula es projecta en alguna sessió.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis en disc.
    '''


#==========================================================================================================
# Reserves
#==========================================================================================================
def busca_cine(id: int) -> Cine:
    ''' Busca un cine pel seu id en la llista de cines.
    Si ela troba retorna el cine, sinó llança l'excepció 'cine_no_trobat'
    '''


#------------------------------------------------------------------------
def mostra_cine_i_sales() -> None:
    ''' Mostra els cines (id i descripció) i les sales d'estos cines (id, descripció).
    '''

#------------------------------------------------------------------------
def selecciona_cine() -> Cine:
    '''Mostra una llista de cines i les seues sales.
    Demana un id de cine i el busca. Si el troba retorna el cine.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

#------------------------------------------------------------------------
def demana_sessio(sala:Sala) -> Sessio:
    ''' Demana l'id d'una sessió, la busca d'entre la llista de sessions de la sala i retorna la sala.
    Si no la troba llança l'excepció 'sessio_no_trobada'. Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

#------------------------------------------------------------------------
def demana_seient(sala:Sala) -> tuple[int,int]:
    ''' Demana una fila (int) i un seient (int). Estos valors es verifiquen contra 
        els valors de files i seient de la sala que li passem. Retorna una fila i
        seient vàlids per a la sala. Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''
    
#==========================================================================================================
# Manteniment de sessions
#==========================================================================================================

def manteniment_sessions(cine:Cine) -> None:  
    ''' Mostra la informació de les sales i les seues sessions del cine indicat.
    Demana l'id d'una sala i mostra una menú amb les opciones de crear, modificar, esborrar i mantinedre les reserves
    per a esta sala seleccionada. 
    '''

#------------------------------------------------------------------------
def mostra_sales_i_sessions(cine:Cine) -> None:
    ''' Mostra informació del cine que li passem com a paràmetre (id i descripció).
    A continuació, mostra informaciño de les sales del cine (id i descripció) i de cadascuna de les
    seues sessions (id, data y hora, info de la pel·licula y el preu).
    '''
#------------------------------------------------------------------------
def demana_sala(cine:Cine) -> Sala:
    ''' Demana l'id d'un sala, la busca d'entre la llista de sales del cine i retorna la sala.
    Si no la troba llança l'excepció 'sala_no_trobada'. Si polsem intro llança l'excepció 'input_type_cancel·lat'
    '''

#------------------------------------------------------------------------
def crea_sessio(sala:Sala) -> None:
    ''' Crea un objete sessió. Demana data y hora de la sessió, l'id de la pel·lícula que es projecta i el preu de l'entrada.
    La sessió s'afegix a llista de sessions de la sala que li passem. Si polsem intro eixim i es cancel·la la creació.
    '''
#------------------------------------------------------------------------
def modifica_sessio(sala:Sala) -> None:
    ''' Modica una de les sessions de la sala que li passem.
    Demana l'id d'una sessio i la busca en la sala. A continuació la modifiquem, preguntant data y hora de la sessió,
    l'id de la pel·lícula que es projecta i el preu d'entrada. Es graven els canvis en disc.
    Si polsem intro es cancel·la la modificació de la sessió.
    '''

#------------------------------------------------------------------------
def esborra_sessio(sala:Sala) -> None:
    ''' Esborra una de les sessions de la sala que li passem.
    Demana l'id d'una sessio i la busca en la sala. A continuació l'esborra. Es graven els canvis en disc.
    Si polsem intro es cancel·la l'esborrat de la sessió.
    '''

#------------------------------------------------------------------------
def demana_dades_reserva() -> Reserva:
    ''' Demna un dni i crea una Reseerva amb ell. Retorna la reserva.
    '''


#------------------------------------------------------------------------
def mateniment_reserves(cine:Cine, sala:Sala) -> None:
    ''' Recorrer les sessions de la sala indicada i mostra de cadascuna d'elles l'estat de les reserves.
    A continuació, demana l'id d'una de le sessions, busca la sessió que correspon a este id, i demana
    un fila i seient. Si la fila/seient ja està reservada pregunta si volem esborrar-la i, si constestem que S, 
    l'esborra i grava els canvis en disc. Per contra, si la fila/seient no està reservada, demana un dni
    amb què crea una reserva per a esta fila/seient i grava els canvis. Si polsem intro al demanar 
    l'id de sessió, fila, seient, dni ens eixim.
    '''

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
def busca_sessions_on_vore_pel_licula(pel_licula:Pel_licula, data_hora:dt.date|None=None) -> list[Resultat]:
    ''' Recorre els cines i les seues sales buscant aquelles sessions on es projecta una pelicula determinada, de manera 
        opcional també es pot filtrar per una data determinada. El resultat es guarda en un lista de objectes
        Resultat que guarda el cine i la sessió que casen amb el filtre de pel·lícula i data/hora indicats.
        Retorna esta llista de (cine, sessió)
    '''
#------------------------------------------------------------------------
def selecciona_sessio_on_vore_pel_licula(pel_licula:Pel_licula, data:dt.date|None) -> tuple[Sala,Sessio]:
    ''' Busca i mostrar els cines i les sesions que projecten la pel·lícula indicada i, opcionalment, en al data indicada.
    A continuació, sol·licita l'id d'una d'este sessions. Retorna la sala i la sessió seleccionades.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

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


#------------------------------------------------------------------------
def reserva_pel_licula_en_sessio(sala:Sala, sessio:Sessio) -> None:
    ''' Mostra una llista de reserves de la sessió indicada.
    Demana fila i seient on volem fer la reserva. Si la fila/seient ja estan reservats mostra un missate indicant-ho.
    Si la fila/seient esta lliures, demana un dni, crea la reserva i l'assigna a la fila/seient.
    Grava els canvis en disc. Si polsem intro eixem del procés de reserva.
    '''
    
#==========================================================================================================
# Persistència de dades.
#==========================================================================================================
def grava_arxiu() -> None:
    '''Grava en arxiu.pkl la llista de pel·licules i la de cines'''
    with open('arxiu.pkl', 'wb') as fd:
        pickle.dump(pel_licules, fd)
        pickle.dump(cines, fd)

def llig_arxiu() -> None:
    ''' Si arxiu.pkl no existix el crea y grava en ell la llista de pel·licules i la de cines.
    Si arxiu.pkl existix el sobreescriu amb les llistes de pel·licules i de cines.
    '''
    global pel_licules
    global cines
    if not os.path.exists('arxiu.pkl'):
        grava_arxiu()
        return
    with open('arxiu.pkl', 'rb') as fd:
        pel_licules = pickle.load(fd)
        cines = pickle.load(fd)

#==========================================================================================================
# Menú principal.
#==========================================================================================================
def mostra_menu() -> None:
    '''Mostra el menú principal. El primer punt no està implementat. Per a simplificar assumirem
    que tenim 2 cines amb dos sales cadascuna.'''
    while True:
        cls('- MENÚ PRINCIPAL -')
        print('------------------')
        print('1- Cines i sales (no implementat)')
        print('2- Manteniment de pel·lícules')
        print('3- Manteniment sessions i reserves')
        print('4- Reservar una pel·lícula')
        print()

        try:
            opc = input_type('Opció?', intro_cancellar=False)
            if opc=='1':
                pass                            # Opció no implementada
            elif opc=='2':
                menu_pel_licules()
            elif opc=='3':
                cine = selecciona_cine()
                manteniment_sessions(cine)
            elif opc=='4':
                reserva_pel_licula()
        except input_type_cancel·lat:
            continue

#==========================================================================================================
# Per a simplificar el programa, assumirem que els cines amb les sales estan creats.
        
# p1 = Pel_licula('La guerra de les galaxies')
# p2 = Pel_licula('Jocs de guerra')
# p3 = Pel_licula('Encontres en la 3a fase')
# p4 = Pel_licula('Indiana Jones')

# pel_licules.append(p1)
# pel_licules.append(p2)
# pel_licules.append(p3)
# pel_licules.append(p4)

# c1 = Cine('La salera')
# c2 = Cine('Estepark')
# cines.append(c1)
# cines.append(c2)

# sala1_1 = Sala(c1, 'sala 1', 4, 4)
# sala2_1 = Sala(c1, 'sala 2', 5, 5)
# sala1_2 = Sala(c2, 'sala 1', 4, 4)
# sala2_2 = Sala(c2, 'sala 2', 5, 5)

# data1= dt.datetime(2024, 1, 1, 16, 0, 0)
# data2= dt.datetime(2024, 1, 1, 20, 0, 0)

# Sessio(sala1_1,data1,p1,5)
# Sessio(sala1_1,data2,p1,6)
# Sessio(sala2_1,data1,p2,5)
# Sessio(sala2_1,data2,p2,6)

# Sessio(sala1_2,data1,p1,5)
# Sessio(sala1_2,data2,p2,6)
# Sessio(sala2_2,data1,p3,5)
# Sessio(sala2_2,data2,p3,6)

if __name__ == "__main__":
    llig_arxiu()
    mostra_menu()