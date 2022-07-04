import requests
import time

def cnpj_query(): 
    print("\x1b[2J\x1b[1;1H")

    cnpj_input = input("Digite o CNPJ (sem pontuação) que deseja consultar: ")
        
    if len(cnpj_input) == 14:

        request = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input))
        address_data = request.json()

        if 'erro' not in address_data:
            print('\n✅ CNPJ ENCONTRADO ') 
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

            time.sleep(10)

        else:
            print ('\n❌ {}: é um CNPJ inválido '.format(cnpj_input))

        time.sleep(5)

    else:
        print('\n ❌ Quantidade de dígitos inválidos!')
        time.sleep(5)