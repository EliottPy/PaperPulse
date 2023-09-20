import requests
import yaml
from yaml.loader import SafeLoader
import feedparser
from utils import *



def getHAL(yaml_url): # returns a list of articles, each in the form of a dict. See utils.printJSON to use the result
    with open(yaml_url) as f:
        data=yaml.load(f, Loader=SafeLoader)

    title = data['title']
    authors = data['authors']
    abstract = data['abstract']
    enterprise = data['enterprise']
    headers = {'Accept' : 'application/json'}
    base_url = ' http://api.archives-ouvertes.fr/search/?q='
    end_url = '&rows=50&wt=json'

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


def getArXiv(yaml_url):
    with open(yaml_url) as f:
        data=yaml.load(f, Loader=SafeLoader)
    title = data['title']
    authors = data['authors']
    abstract = data['abstract']


    url='http://export.arxiv.org/api/query?search_query='
    end_url = '&max_results=4'

    for i in range(len(title)):
        key=title[i]
        if key is not None:
            if url[-1]!='=': #i.e. if we are not the first item in the list
                url=url+'+AND+'
            url=url+'ti:'+key

    for i in range(len(authors)):
        key=authors[i]
        if key is not None:
            if url[-1]!='=': #i.e. if we are not the first item in the list
                url=url+'+AND+'
            url=url+'au:'+key

    for i in range(len(abstract)):
        key=abstract[i]
        if key is not None:
            if url[-1]!='=': #i.e. if we are not the first item in the list
                url=url+'+AND+'
            url=url+'abs:'+key

    url = url + end_url

    feed = feedparser.parse(url)
    for article in feed['entries']:
        print(f"Article name : {article['title']}")
        name_list = ''
        for name in article['authors']:
            name_list=name_list+name['name']+', '
        print(f"List of authors : {name_list}")
        print(f"URL : {article['links'][1]['href']}\n")
        
getArXiv('keywords.yaml')
getHAL('keywords.yaml')
