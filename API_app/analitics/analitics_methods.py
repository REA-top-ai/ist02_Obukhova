from client.API_methods import get_top_headlines, get_everything, get_sources
import json
from pprint import pprint

resp = get_everything('f8af19e21e31490f9de51a16c5aaa391', q='apple', sortBy='publishedAt')

ctr = 0
for art in resp['articles']:
    if art['title']!=None and len(art['description'])>=50 and art['url']!=None and ctr<50:
        ctr+=1
        res = {
            'title':art['title'],
            'source':art['source'],
            'publishedAt':art['publishedAt'],
            'author':art['author'],
        }
        pprint(json.dumps(res))
    if ctr>=50:
        break