

def printJSON(file):
    docs=file['response']['docs']

    for file in docs:
        x=file['label_s']
        i=x.index('&')
        x=x[:i]
        print(f"Article : {x}\n Url : {file['uri_s']}")
        print('\n')