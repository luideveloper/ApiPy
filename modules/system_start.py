import time

from .ip import ip_query
from .cep import cep_query
from .cnpj import cnpj_query
from .ddd import ddd_query
from .bin import bin_query

def menu_start():
    option = 0
    while (option!=6):

        print("\x1b[2J\x1b[1;1H")
        print("Digite o número de qual consulta deseja realizar: ")
        print("\n[ 1 ] - Consulta IP (ex: 185.153.176.39)")
        print("[ 2 ] - Consultar CEP (ex: 03015-970)")
        print("[ 3 ] - Consultar CNPJ (ex: 17795814000162)")
        print("[ 4 ] - Consultar DDD (ex: 11)")
        print("[ 5 ] - Consultar BIN (ex: 418822)")
        print("[ 6 ] - Sair do programa")

        try:
            option = int(input("\nO que você deseja? "))

            if option <= 6:
                if option == 1:
                    ip_query()
                elif option == 2:
                    cep_query()
                elif option == 3:
                    cnpj_query()
                elif option == 4:
                    ddd_query()
                elif option == 5:
                    bin_query()
                elif option == 6:
                    exit()
            else:
                print("\x1b[2J\x1b[1;1H")
                print("Opção invalida")
                time.sleep(5)

        except ValueError:
            print("\x1b[2J\x1b[1;1H")
            print("Erro inesperado, o programa será reinicializado")