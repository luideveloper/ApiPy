import requests
import time



def bin_query():
    print("\x1b[2J\x1b[1;1H")

    bin_input = input('Digite a BIN que deseja consultar: ')
    request = requests.get('https://lookup.binlist.net/{}'.format(bin_input))
    address_data = request.json()

    if 'erro' not in address_data:
        print('\n✅ BIN ENCONTRADA ') 
        print('• Bandeira {}'.format (address_data['scheme']))
        print('• Tipo {}'.format (address_data['type']))
        print('• Nível {}'.format (address_data['brand']))
        print('• Bw {}'.format (address_data['bank'].get('name')))
        
        time.sleep(10)
    else:
        print ('\n❌ {}: é uma BIN inválida '.format(bin_input))
    time.sleep(5)
