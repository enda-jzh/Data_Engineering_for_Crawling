from newspaper import Article


def getLinks(path):
    read_file = open(path, 'r+', encoding='UTF-8')
    hyperlinks = [x.strip() for x in list(read_file)]
    read_file.close()
    return hyperlinks

def getContext(path):
    read_path = '.\data_zh\\' + path + '_url_zh.txt'
    hyperlinks = getLinks(read_path)
    save_path = '.\data_zh\\' + path + '_zh.txt'
    save_file = open(save_path, 'w+', encoding='UTF-8')
    for hl in hyperlinks:
        print(hl)
        article = Article(hl, language='zh')
        article.download()
        article.parse()

        save_file.write(article.text+'\n')
    save_file.close()


getContext('culture')
getContext('sports')
getContext('financial')
getContext('tech')
