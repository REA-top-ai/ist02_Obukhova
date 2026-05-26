from ist02_Obukhova.API_app.client.API_methods import get_top_headlines, get_everything, get_sources
from ist02_Obukhova.API_app.mistral import summary
from pprint import pprint


if __name__ == '__main__':
    # result_headlines = get_top_headlines('f8af19e21e31490f9de51a16c5aaa391', q = 'apple')
    result_everything = get_everything('f8af19e21e31490f9de51a16c5aaa391', q='apple')
    res = summary(result_everything.get('articles'))
    # pprint(result_everything)
    pprint(res)
    # result_sources = get_sources('f8af19e21e31490f9de51a16c5aaa391')
    # pprint(result_headlines)
    # pprint(result_everything)
    # pprint(result_sources)

