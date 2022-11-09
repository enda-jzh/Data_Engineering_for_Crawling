from nltk import word_tokenize
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# get the stopwords

stop_words = open('data/stopwords.txt', 'r+', encoding='UTF-8').read().strip()


def TextProcessing(path):
    # get the unsettled text
    read_path = path + '.txt'
    read_file = open(read_path, 'r+', encoding='UTF-8')
    unsettled_text = read_file.read().lower()
    # print(unsettled_text)
    read_file.close()

    # process text
    cut_words_1 = word_tokenize(unsettled_text)
    # print(cut_words)

    # delete the punctuations
    punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '-', '’', '“']
    cut_words_2 = [word for word in cut_words_1 if word not in punctuations]

    # delete the stopwords
    word_list = [word for word in cut_words_2 if word not in stop_words]
    # print(word_list)

    # count the frequency
    freq = FreqDist(word_list)
    frequency_words = sorted(freq.items(), key=lambda x: x[1])

    # obtain top20 frequency of words
    high_frequency_words_list = frequency_words[-1:-21:-1]
    # print(high_frequency_words_list)
    words = ""
    # create the word list for wordcloud
    for dict in high_frequency_words_list:
        words += (dict[0] + ' ')

    return words


def create_wordcloud(path):
    words = TextProcessing(path)
    wc = WordCloud(background_color='white',
                   max_words=20,
                   width=1600,
                   height=1200,
                   max_font_size=120,
                   min_font_size=50,
                   random_state=10
                   )
    wc.generate(words)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    # plt.show()
    save_path = '.\wc_picture\\' + path + '.png'
    plt.savefig(save_path)


create_wordcloud('culture')
create_wordcloud('tech')
create_wordcloud('energy')
create_wordcloud('health')
create_wordcloud('financial')
