import requests
import time

def cep_query():

    print("\x1b[2J\x1b[1;1H")
    cep_input = input('Digite o CEP que deseja consultar: ')
        
    if len(cep_input) < 8:
        print('\n ❌ Quantidade de dígitos inválidos!')
        time.sleep(5)

    else:
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
        address_data = request.json()

        if 'erro' not in address_data:
            print('\n✅ CEP ENCONTRADO ') 
            print('• CEP: {}'.format (address_data['cep']))
            print('• Logradouro: {}'.format (address_data['logradouro'])) 
            print('• Complemento: {}'.format(address_data['complemento']))
            print('• Bairro: {}'.format (address_data['bairro'])) 
            print('• Cidade: {}'.format(address_data['localidade']))
            print('• Estado: {}'.format (address_data['uf']))

            time.sleep(10)
        else:
            print ('\n❌ {}: é um CEP inválido '.format(cep_input))

        time.sleep(5)