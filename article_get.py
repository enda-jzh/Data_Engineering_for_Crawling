from newspaper import Article


def getLinks(path):
    read_file = open(path, 'r+', encoding='UTF-8')
    hyperlinks = [x.strip() for x in list(read_file)]
    read_file.close()
    return hyperlinks

def getContext(path):
    read_path = '.\data\\'+ path + '_url.txt'
    hyperlinks = getLinks(read_path)
    save_path = '.\data\\'+ path + '.txt'
    save_file = open(save_path, 'w+', encoding='UTF-8')
    for hl in hyperlinks:
        print(hl)
        article = Article(hl, language='en')
        article.download()
        article.parse()

        save_file.write(article.text+'\n')
    save_file.close()

# financial
getContext('financial')

# culture
getContext('culture')

# energy
getContext('energy')

# health
getContext('health')

# tech
getContext('tech')