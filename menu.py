import ariel
import tudor
import rodrigo

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


if __name__ == "__main__":
    llig_arxiu()
    mostra_menu()