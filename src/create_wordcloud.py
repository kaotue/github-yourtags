from wordcloud import WordCloud

def run(tags: list):

    text = ''
    for tag in tags:
        for _ in range(tag['count']):
            text = text + ',' + tag['name'].replace(' ','')
    print(f'{text=}')
    options = {
        'max_font_size': 160,
        'prefer_horizontal': 1,
        'width': 1000,
        'height': 500,
        'regexp': '[a-zA-z0-9#+-]+',
        'collocations': False
    }

    return WordCloud(**options).generate(text).to_svg()