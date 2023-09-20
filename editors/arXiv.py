import yaml
from yaml.loader import SafeLoader
import feedparser

def getArXiv(yaml_url, nb):
    with open(yaml_url) as f:
        data=yaml.load(f, Loader=SafeLoader)
    title = data['title']
    authors = data['authors']
    abstract = data['abstract']


    url='http://export.arxiv.org/api/query?search_query='
    end_url = '&max_results='+nb

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