from mistralai.client import Mistral

apiKey=""
client = Mistral(api_key=apiKey)
def summary(articles):
    text = ''
    if isinstance(articles, dict):
        articles = [articles]
    elif not isinstance(articles, list):
        articles = [articles]

    for i, article in enumerate(articles):
        title = article.get('title', 'Нет заголовка')
        description = article.get('description', 'Нет описания')

        text += f'''
    Статья {i + 1}:
    Заголовок: {title}
    Описание: {description}'''
        prompt = f'''
        Верни аннотации к каждой из переданных ниже статей с оценкой того, что произошло за день по заданной теме. Требования: русский языкб 250-300 слов каждая аннотация и аннотация должна содержать все, что было сказано вышеБ а не просто краткий пересказ
        Статьи: {text}
        '''
        resp = client.chat.complete(model='mistral-small-latest', messages = [{'role': 'user', 'content': prompt}])
        return resp.choices[0].message.content
