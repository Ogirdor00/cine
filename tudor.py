from classes import *
import datetime as dt


#==========================================================================================================
# Manteniment de pel·lícules
#==========================================================================================================
def menu_pel_licules() -> None:
    ''' Mostra la llista de pel·ícules y després un menú per al seu manteniment.
    El menú permet crear, modificar i esborrar pel·lícules. Si polsem intro tanquem el menú (return).
    No podrem esborrar una pel·lícula que s'estiga projectan en alguna sessió de qualsevol cine.
    '''
    mostra_pel_licules()

    while True:
        x = input('Elige una opción para (1)Crear Pelicula (2)Modificar Pelicula (3)Borrar Pelicula (0)Salir: ')
        if x == '1':
            crea_pel_licula()
        if x == '2':
            modifica_pel_licula()
            
        if x == '3':
            esborra_pel_licula()
        if x == '0':
            break
#------------------------------------------------------------------------
def mostra_pel_licules() -> None:
    ''' Mostra informació de la llista de pel·lícules (id y info)
    '''
    print('--- Lista de Peliculas ---')
    for pelicula in pel_licules:
        print(pelicula.id, pelicula.info)

#------------------------------------------------------------------------
def crea_pel_licula() -> None:
    ''' Crea una pel·licula i la grava. Demana la seua descripció.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis.
    '''
    print('Crea una Película')
    print('------------------------')


    while True:
        n = input('Nombre de la película(Intro para salir): ')
        
        pel_licules.append(Pel_licula(n))
        grava_arxiu()
        mostra_pel_licules()

        return
 


#------------------------------------------------------------------------
def busca_pel_licula(id: int) -> Pel_licula:
    ''' Busca una pel·lícula pel seu id en la llista de pel·lícules.
    Si la troba retorna la pel·lícula, sinó llança l'excepció 'pelicula_no_trobada'
    '''
    
    for pelicula in pel_licules:
        if pelicula.id == id:
         return pelicula
    if pelicula.id not in pel_licules:
        raise pelicula_no_trobada

#------------------------------------------------------------------------
def demana_pel_licula(txt:str) -> Pel_licula:
    ''' Demana l'id d'una pel·lícula, la busca en la llista de pel·lícules i retorna la Pel·lícula.
    Si polsem intro llança l'excepció 'input_type_cancel·lat' 
    '''
    
    id = input_type(txt, type='int')
    pelicula = busca_pel_licula(id)
    return pelicula



#------------------------------------------------------------------------
def modifica_pel_licula() -> None:
    ''' Modifica una pel·lícula. Primer demana un id de pel·licula a l'usuari i la busca entre la llista de pel·lícules.
    Demana a l'usuari una descripció nova i la reemplaça la descripció vella. Grava els canvis en disc.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''
    while True:
        try:
            print('Modifica una Película')
            print('----------------------------')
            mostra_pel_licules()
            peliVieja = demana_pel_licula('ID de la película a modificar: ')
            peliNueva = input('Nuevo nombre de la película: ')

            for x in pel_licules:
             if x.info == peliVieja.info:
                   x.info = peliNueva
        except pelicula_no_trobada:
            print('-------------------------------')
            print('No se ha encontrado la pelicula')
            print('-------------------------------') 
            return   
        grava_arxiu()
        mostra_pel_licules()


#------------------------------------------------------------------------
def pel_licula_utilitzada_en_alguna_sessio(pel_licula:Pel_licula) -> bool:
    '''No podem esborrar una pel·lícula si hi ha una sessió en qualsevol sala que la projecta.
    Retorna True si alguna sala la projecta, False si no.
    '''
    for cine in cines:
        for sala in cine.sales:
            for sessio in sala.sessions:
                if pel_licula == sessio.pel_licula:
                    return True
    return False


#------------------------------------------------------------------------
def esborra_pel_licula():
    ''' Esborra una pel·lícula de la llista de pel·lícules. Demana l'id de la pel·licula a esborrar.
    La busca d'entre la llista de pel·lícules. Avisa si la pel·lícula es projecta en alguna sessió.
    Si polsem intro llança l'excepció 'input_type_cancel·lat'. Grava els canvis en disc.
    '''
    try:    
        print('Borrar Película')
        print('------------------------')
        mostra_pel_licules()
        peliBorrar = demana_pel_licula('ID de la película a borrar: ')
        if pel_licula_utilitzada_en_alguna_sessio(peliBorrar):
            print('La película esta puesta en una sesión')
        else:
            pel_licules.remove(peliBorrar)
       
        grava_arxiu()
        mostra_pel_licules()
    except pelicula_no_trobada:
        print('-------------------------------')
        print('No se ha encontrado la pelicula')
        print('-------------------------------') 
        return   
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
