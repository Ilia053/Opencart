import requests
import pprint

s = requests.Session()

username = 'ilia'
key='xbzdYW5M5TuFqPXdY3rI0J8k1G2sC2XYWpLoyU3zv8BKhKHrA4oRG0nPMiX5wQqYqze82Dw8MKBo8E4Ecy26DH1Y0oP3JfYsSHJI2WuwyhrYHUOOHxqQLfl03mXF8Qs8EHmSd8ATD3Z4mQ28eTdqpIBs00ozhoZWOPWky6Vj4f81GioyD5baADtdaoTtAPola26jjfVZnYBvFKOAONuhCOUWnjWy4z8Upl6bWiqSKrZFAx6L1mDsAdnD6c4auTIN'

def establish_ssesion():
    req = s.post(
        'http://localhost/index.php?route=api/login',
        data={
            'username':username,
            'key':key
        }
    )
    return req.json()['api_token']

TOKEN = establish_ssesion()





if __name__ == '__main__':

    req = s.post(
        'http://localhost/index.php?route=api/currency',
        params={'api_token': TOKEN},
        data={'currency': 'USD'}
    )

    pprint.pprint(list(req.cookies))
