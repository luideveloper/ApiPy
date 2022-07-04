import requests
import time

def ip_query():
    print("\x1b[2J\x1b[1;1H")

    ip_input = input("Digite o IP que deseja consultar: ")
    request = requests.get('https://ipapi.co/{}/json/'.format(ip_input))
    address_data = request.json()

    if 'error' not in address_data:
        print('\n✅ IP ENCONTRADO ') 
        print('• IP: {}'.format(address_data['ip']))
        print('• Cidade: {}'.format(address_data['city']))
        print('• Estado: {}'.format(address_data['region']))
        print('• País: {}'.format(address_data['country_name']))
        print('• Capital do País: {}'.format(address_data['country_capital']))
        print('• Continente: {}'.format(address_data['continent_code']))
        print('• CEP: {}'.format(address_data['postal']))
        print('• Latitude: {}'.format(address_data['latitude']))
        print('• Longitude: {}'.format(address_data['longitude']))
        print('• Provedor: {}'.format(address_data['org']))

        time.sleep(10)

    else:
        print ('\n❌ {} é um IP inválido '.format(ip_input))
    
    time.sleep(5)
    
    