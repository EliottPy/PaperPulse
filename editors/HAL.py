import yaml
from yaml.loader import SafeLoader
import requests

def getHAL(yaml_url, nb): # returns a list of articles, each in the form of a dict. See utils.printJSON to use the result
    with open(yaml_url) as f:
        data=yaml.load(f, Loader=SafeLoader)

    title = data['title']
    authors = data['authors']
    abstract = data['abstract']
    enterprise = data['enterprise']
    headers = {'Accept' : 'application/json'}
    base_url = ' http://api.archives-ouvertes.fr/search/?q='
    end_url = '&rows='+nb+'&wt=json'

    url=''

    url=url+'title_t:('
    for t in title :
        if t is not None:
            url=url+t+' '
    url=url+')'


    url=url+'&abstract_s:()'
    for abs in abstract:
        if abs is not None:
            url=url+abs+' '
    url=url+')'


    url=url+'&auth_t:('
    for aut in authors:
        if aut is not None:
            url=url+aut+' '
    url=url+')'


    url=url+'&authEmail_s:('
    for ent in enterprise :
        if ent is not None:
            url=url+ent+' '
    url=url+')'

    url=base_url+url+end_url
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    if r.status_code != 204:
        #print(r.json())
        printJSON(r.json())


def printJSON(file):
    docs=file['response']['docs']

    for file in docs:
        x=file['label_s']
        i=x.index('&')
        x=x[:i]
        print(f"Article : {x}\n Url : {file['uri_s']}")
        print('\n')
