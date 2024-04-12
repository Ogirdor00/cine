from classes import *
from tudor import *
#from tudor import mostra_pel_licules
#from tudor import busca_pel_licula



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
            return cine

    raise cine_no_trobat



# === === === === === ===   EL INICI
def selecciona_cine() -> Cine:
    mostra_cine_i_sales()
    id = input_type('ID del cine a buscar: ', type= 'int')      
    cine = busca_cine(id)       # type:ignore


    return cine
    
# === === === === === ===         


def mostra_sales_i_sessions(cine: Cine) -> None:
    ''' Mostra informació del cine que li passem com a paràmetre (id i descripció).
    A continuació, mostra informaciño de les sales del cine (id i descripció) i de cadascuna de les
    seues sessions (id, data y hora, info de la pel·licula y el preu).
    '''
    print(f'Cine({cine.id}): {cine.descripcio}')
    for sala in cine.sales:
        print('----------------------------------')
        print(f'SALA ({sala.id}): sala {sala.id}')
        for sessio in sala.sessions:
            print(f'    SESSIÓ ({sessio.id}): {sessio.data_hora} {sessio.pel_licula.info} {sessio.preu_entrada.real}')

# buscar una peli, pa demana pelicula ------demana_pel_licula
# def busca_pel_licula(id: int) -> Pel_licula:
#     ''' Busca una pel·lícula pel seu id en la llista de pel·lícules.
#     Si la troba retorna la pel·lícula, sinó llança l'excepció 'pelicula_no_trobada'
#     '''

#     for pel_licula in pel_licules:
#         if id == pel_licula.id:
#             return pel_licula
            
#     raise pelicula_no_trobada

# Demanar pelicula ----
# def demana_pel_licula(txt:str) -> Pel_licula:
#     ''' Demana l'id d'una pel·lícula, la busca en la llista de pel·lícules i retorna la Pel·lícula.
#     Si polsem intro llança l'excepció 'input_type_cancel·lat' 
#     '''
#     while True:
#         try:
#             mostra_pel_licules()
#             id = input_type(txt,'int')
#             return busca_pel_licula(id)
#         except pelicula_no_trobada:
#             print('No se ha trovat la pel·licula')


# Demana sala ----
def demana_sala(cine: Cine) -> Sala:
    ''' Demana l'id d'un sala, la busca d'entre la llista de sales del cine i retorna la sala.
    Si no la troba llança l'excepció 'sala_no_trobada'. Si polsem intro llança l'excepció 'input_type_cancel·lat'
    '''
    id:int = input_type('Selecciona una sala:','int')
    return cine.busca_sala(id)

# Crea sessió ----
def crea_sessio(sala: Sala) -> None:
    ''' Crea un objete sessió. Demana data y hora de la sessió, l'id de la pel·lícula que es projecta i el preu de l'entrada.
    La sessió s'afegix a llista de sessions de la sala que li passem. Si polsem intro eixim i es cancel·la la creació.
    '''
    while True:
        try:
            data_hora = obtin_data_hora()
            pel_licula = demana_pel_licula('ID de la pelicula:')
            preu_entrada = input_type('Quin sera el preu', 'float')
            Sessio(sala,data_hora,pel_licula,preu_entrada)
            input_type('Fet. Intro per a continuar', intro_cancellar= False)
            grava_arxiu()

        except input_type_cancel·lat:
            break


#pa lo de modifica sessio
def demana_sessio(sala: Sala) -> Sessio:
    ''' Demana l'id d'una sessió, la busca d'entre la llista de sessions de la sala i retorna la sala.
    Si no la troba llança l'excepció 'sessio_no_trobada'. Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''

    id:int = input_type('Selecciona una sesió:','int')
    return sala.busca_sessio(id)



#------------------------------------------------------------------------
def modifica_sessio(sala: Sala) -> None:
    ''' Modica una de les sessions de la sala que li passem.
    Demana l'id d'una sessio i la busca en la sala. A continuació la modifiquem, preguntant data y hora de la sessió,
    l'id de la pel·lícula que es projecta i el preu d'entrada. Es graven els canvis en disc.
    Si polsem intro es cancel·la la modificació de la sessió.
    '''
    while True:
        try:
            # print(msg_error)
            #msg_error = ''
            sessio:Sessio = demana_sessio(sala)
            data_hora = obtin_data_hora()
            sessio.data_hora = data_hora
            mostra_pel_licules()
            sessio.pel_licula = demana_pel_licula('Selecciona una pel.licula:')
            sessio.preu_entrada = input_type('Quin sera el preu', 'float')
            input_type('Fet. Intro per a continuar', intro_cancellar= False)
            grava_arxiu()
    
        except input_type_cancel·lat:
            break
        except sessio_no_trobada:
            msg_error = 'No se ha trobat la sessio'






#------------------------------------------------------------------------
def esborra_sessio(sala:Sala) -> None:
    ''' Esborra una de les sessions de la sala que li passem.
    Demana l'id d'una sessio i la busca en la sala. A continuació l'esborra. Es graven els canvis en disc.
    Si polsem intro es cancel·la l'esborrat de la sessió.
    '''
    while True:
        try:
            sessio1:Sessio = demana_sessio(sala)
            sala.sessions.remove(sessio1)
            grava_arxiu() 
            return
        except sessio_no_trobada:
            print('Sessió no trobada')
#------------------------------------------------------------------------
def demana_dades_reserva() -> Reserva:
    ''' Demana un dni i crea una Reseerva amb ell. Retorna la reserva.
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
    while True:
        cls('-Llista de Reserves-')
        print(f'Cine: {cine.descripcio}|| Sala: {sala.descripcio} ')
        for sessio in sala.sessions:
            print(f'ID: {sessio.id}|| Data: {sessio.data_hora}|| Preu: {sessio.preu_entrada}')
            sessio.mostra_reserves()
        
        s:int = input_type('Sessió? ' ,'int')    #type:ignore    
        sala.busca_sessio(s)
        demana_seient(s) 
        
#------------------------------------------------------------------------
def demana_seient(sala:Sala) -> tuple[int,int]:
    ''' Demana una fila (int) i un seient (int). Estos valors es verifiquen contra 
        els valors de files i seient de la sala que li passem. Retorna una fila i
        seient vàlids per a la sala. Si polsem intro llança l'excepció 'input_type_cancel·lat'.
    '''
    while True:
        fila:int = input_type('Fila? ', 'int')  #type:ignore 
        
        if fila < 0 or fila > sala.files:
            print('La fila no exisix')
            continue
        seient:int = input_type('Seient? ', 'int')    #type:ignore
        
        if seient < 0 or seient > sala.seients_per_fila:
            print('El seient no existix')
     

        return fila,seient     
       
# === === === === === ===    
# manteniment sessions
# === === === === === ===        
def manteniment_sessions(cine: Cine) -> None:  
    ''' Mostra la informació de les sales i les seues sessions del cine indicat.
    Demana l'id d'una sala i mostra una menú amb les opciones de crear, modificar, esborrar i mantinedre les reserves
    per a esta sala seleccionada. 
    '''
    while True:
        try:
            cls('- LLISTA DE SESSIONS -')
            # print(msg_error)
            msg_error = ''
            mostra_sales_i_sessions(cine)


            sala = demana_sala(cine)
            
            if sala:
                print(f'MANTENIMENT DE SESSIONS: SALA({sala.id}) sala {sala.id}')
                opcio = input_type('1-Crea, 2-Modifica, 3-Esborra, 4-Reserves. Opció?','int')
                if opcio == 1:
                    crea_sessio(sala)
                elif opcio == 2:
                    modifica_sessio(sala)
                elif opcio == 3:
                    esborra_sessio(sala)
                elif opcio == 4:
                    mateniment_reserves(cine,sala)
                else:
                    msg_error = 'Opció incorrecta'

                grava_arxiu()

        except input_type_cancel·lat:
            break
        except sala_no_trobada:
            msg_error = 'No se ha trobat la sala'






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

# if __name__ == "__main__":
#     llig_arxiu()

# x = input("Pulsa la tecla 3")
# if x == "3":
#     y= selecciona_cine()
#     manteniment_sessions(y)


