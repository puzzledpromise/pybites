import json

import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r = requests.get(IPINFO_URL.format(ip=ip_address))
    data = json.loads(r.text)
    return data['country']

if __name__ == '__main__':
    ip_address = '185.244.212.61'
    print(get_ip_country(ip_address))
