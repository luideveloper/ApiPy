import requests
import time

def sistema():
    option = int(input('\n==> Digite o número de qual consulta deseja realizar: \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (ex: 11) \n [5] - Consultar BIN (ex": 418822) \n\nOpção: '))

    if option == 1:
        ip()
    if option == 2:
        cep()
    if option == 3:
        cnpj()
    if option == 4:
        ddd()
    if option == 5:
        bin()
    else:
        print("Opção invalida")

def ip():

    ip_input = input('==> Digite o IP que deseja consultar: ')
        
    request = requests.get('https://ipapi.co/{}/json/'.format(ip_input))

    address_data = request.json()

    if 'error' not in address_data:
        print('\n ✅ IP ENCONTRADO ') 
        print('• IP: {}'.format (address_data['ip']))
        print('• Cidade: {}'.format (address_data['city']))
        print('• Estado: {}'.format (address_data['region']))
        print('• País: {}'.format (address_data['country_name']))
        print('• Capital do País: {}'.format (address_data['country_capital']))
        print('• Continente: {}'.format (address_data['continent_code']))
        print('• CEP: {}'.format (address_data['postal']))
        print('• Latitude: {}'.format (address_data['latitude']))
        print('• Longitude: {}'.format (address_data['longitude']))
        print('• Provedor: {}'.format (address_data['org']))

    else:
        print ('\n❌ {}: é um IP inválido '.format(ip_input))
    
    time.sleep(3)
    option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair\n\n'))

    if option_loop == 1:
        option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
        if option == 1:
            ip()
        if option == 2:
            cep()
        if option == 3:
            cnpj()
        if option == 4:
            ddd()
        if option == 5:
            bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()       

def cep():

    cep_input = input('==> Digite o CEP que deseja consultar: ')
        
    if len(cep_input) < 8:
        print('\n ❌ Quantidade de dígitos inválidos!')

        option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair '))

        if option_loop == 1:
            option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
            if option == 1:
                ip()
            if option == 2:
                cep()
            if option == 3:
                cnpj()
            if option == 4:
                ddd()
            if option == 5:
                bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()
    
    else:
        
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

        address_data = request.json()

        if 'erro' not in address_data:
            print('\n ✅ CEP ENCONTRADO ') 
            print('• CEP: {}'.format (address_data['cep']))
            print('• Logradouro: {}'.format (address_data['logradouro'])) 
            print('• Complemento: {}'.format(address_data['complemento']))
            print('• Bairro: {}'.format (address_data['bairro'])) 
            print('• Cidade: {}'.format(address_data['localidade']))
            print('• Estado: {}'.format (address_data['uf']))
        else:
            print ('\n❌ {}: é um CEP inválido '.format(cep_input))

        time.sleep(3)
        option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair\n\n'))

        if option_loop == 1:
            option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
            if option == 1:
                ip()
            if option == 2:
                cep()
            if option == 3:
                cnpj()
            if option == 4:
                ddd()
            if option == 5:
                bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()

def cnpj(): 

    cnpj_input = input('==> Digite o CNPJ (sem pontuação) que deseja consultar: ')
        
    if len(cnpj_input) == 14:

        request = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input))

        address_data = request.json()

        if 'erro' not in address_data:
            print('\n ✅ CNPJ ENCONTRADO ') 
            print('• Razão Social: {}'.format (address_data['nome']))
            print('• Nome Fantasia: {}'.format (address_data['fantasia']))
            print('• Logradouro: {}'.format (address_data['logradouro']))
            print('• Bairro: {}'.format (address_data['bairro']))
            print('• Número: {}'.format (address_data['numero']))
            print('• CEP: {}'.format (address_data['cep']))
            print('• Município: {}'.format (address_data['municipio']))
            print('• Telefone: {}'.format (address_data['telefone']))
            print('• UF: {}'.format (address_data['uf']))
            print('• Situação: {}'.format (address_data['situacao']))
            print('• Email: {}'.format (address_data['email']))
            print('• Capital Social: {}'.format (address_data['capital_social']))
            print('• Porte: {}'.format (address_data['porte']))
            print('• Data de Abertura: {}'.format (address_data['abertura']))

        else:
            print ('\n❌ {}: é um CNPJ inválido '.format(cnpj_input))

        time.sleep(3)
        option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair\n\n'))

        if option_loop == 1:
            option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
            if option == 1:
                ip()
            if option == 2:
                cep()
            if option == 3:
                cnpj()
            if option == 4:
                ddd()
            if option == 5:
                bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()

    else:
        print('\n ❌ Quantidade de dígitos inválidos!')

    option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair '))

    if option_loop == 1:
        option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
        if option == 1:
            ip()
        if option == 2:
            cep()
        if option == 3:
            cnpj()
        if option == 4:
            ddd()
        if option == 5:
            bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()
        
def ddd():

    ddd_input = input('==> Digite o DDD que deseja consultar: ')
        
    if len(ddd_input) == 2:

        request = requests.get('https://brasilapi.com.br/api/ddd/v1/{}'.format(ddd_input))

        address_data = request.json()

        if 'erro' not in address_data:
            print('\n ✅ DDD ENCONTRADO ') 
            print('• Estado {}'.format (address_data['state']))
            print('• Cidades: {}'.format (address_data['cities']))

        else:
            print ('\n❌ {}: é um DDD inválido '.format(ddd_input))

        time.sleep(3)
        option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair\n\n'))

        if option_loop == 1:
            option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
            if option == 1:
                ip()
            if option == 2:
                cep()
            if option == 3:
                cnpj()
            if option == 4:
                ddd()
            if option == 5:
                bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()

    else:
        print('\n ❌ Quantidade de dígitos inválidos!')

    option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair '))

    if option_loop == 1:
        option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
        if option == 1:
            ip()
        if option == 2:
            cep()
        if option == 3:
            cnpj()
        if option == 4:
            ddd()
        if option == 5:
            bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()

def bin():

    bin_input = input('==> Digite a BIN que deseja consultar: ')
        
    request = requests.get('https://lookup.binlist.net/{}'.format(bin_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('\n ✅ BIN ENCONTRADA ') 
        print('• Bandeira {}'.format (address_data['scheme']))
        print('• Tipo {}'.format (address_data['type']))
        print('• Nível {}'.format (address_data['brand']))
        print('• Bw {}'.format (address_data['bank'].get('name')))

    else:
        print ('\n❌ {}: é uma BIN inválida '.format(bin_input))

    time.sleep(3)
    option_loop = int(input('\n 👀 Deseja realizar uma nova consulta?\n 1 - Sim\n 2 - Sair\n\n'))

    if option_loop == 1:
        option = int(input('==> Digite o número de qual consulta deseja realizar :) \n\n [1] - Consulta IP (ex: 185.153.176.39) \n [2] - Consultar CEP (ex: 03015-970) \n [3] - Consultar CNPJ (ex: 17795814000162) \n [4] - Consultar DDD (11) \n [5] - Consultar BIN (418822) \n\n'))
        if option == 1:
            ip()
        if option == 2:
            cep()
        if option == 3:
            cnpj()
        if option == 4:
            ddd()
        if option == 5:
            bin()
        else:
            print('\n 🕒 Até a próxima!\n')
            exit()