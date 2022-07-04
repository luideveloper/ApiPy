import requests
import time

def ddd_query():
    print("\x1b[2J\x1b[1;1H")
    ddd_input = input('Digite o DDD que deseja consultar: ')
        
    if len(ddd_input) == 2:
        request = requests.get('https://brasilapi.com.br/api/ddd/v1/{}'.format(ddd_input))
        address_data = request.json()

        if 'erro' not in address_data:
            print('\n✅ DDD ENCONTRADO ') 
            print('• Estado: {}'.format (address_data['state']))
            print("• Cidades:")
            for x in address_data['cities']:
                print("    -", x)
            time.sleep(10)
        
        else:
            print ('\n❌ {}: é um DDD inválido '.format(ddd_input))
        time.sleep(5)
        
    else:
        print('\n ❌ Quantidade de dígitos inválidos!')
    time.sleep(5)