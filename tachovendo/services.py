import sys
import requests0 as requests
import json

from oauth_hook import OAuthHook

'''
http://api.riodatamine.com.br/rest/request-token?
app-id=<appID>&app-secret=<appSecret>[&redirect_uri=<url>]
'''

AUTH_URL_REDIRECT = "http://api.riodatamine.com.br/rest/request-token?" \
                    "app-id=%s&app-secret=%s&redirect_uri=%s"

AUTH_URL = "http://api.riodatamine.com.br/rest/request-token?" \
            "app-id=%s&app-secret=%s"

RAIN_URL = "http://api.riodatamine.com.br/" \
            "rest/meteorologia/pluviometros?format=json"

FLOOD_URL = "http://api.riodatamine.com.br/" \
            "rest/agua/pontos-alagamento?format=json"

SCHOOLS_URL = "http://api.riodatamine.com.br/" \
              "rest/infraestruturas/escolas?format=json"

my_config = {'verbose': sys.stderr}

def auth(app_id, app_secret):
    OAuthHook.consumer_key = app_id
    OAuthHook.consumer_secret = app_secret
    oauth_hook = OAuthHook('', '')
    client = requests.session(hooks={'pre_request' : oauth_hook})
    request = client.get(AUTH_URL % (app_id, app_secret))

    access_token = request.headers['x-access-token']
    access_token_expires = request.headers['x-access-token-expires']

    return (access_token, access_token_expires)

def rain_service(access_token):
    headers = {'Authorization' : access_token}
    request = requests.get(RAIN_URL, headers=headers, config=my_config)
    return request.content
    #return json.loads(request.content)

def flood_service(access_token):
    headers = {'Authorization' : access_token}
    request = requests.get(FLOOD_URL, headers=headers, config=my_config)
    return request.content

def schools_service(access_token):
    headers = {'Authorization' : access_token}
    request = requests.get(SCHOOLS_URL, headers=headers, config=my_config)
    return request.content

