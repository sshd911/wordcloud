from wordcloud import WordCloud
from matplotlib import pyplot
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *

FONT = 'data/源ノ角ゴシック.ttf'
FILE_OUTPUT = 'data/output.txt'
FILE_INPUT = 'data/input.txt'

# read
def load(file_name):
    return open(file_name, mode='rt', encoding='UTF-8').read()

# filter and anlyze ...
def charFilter(): 
    return [UnicodeNormalizeCharFilter(), RegexReplaceCharFilter('[0-9#!:;<>{}・`.,()-=$/_\d\'"\[\]\|]+', '')]

def tokenFilter():
    return [POSKeepFilter(['名詞']), LowerCaseFilter(), ExtractAttributeFilter('surface')]

def anlyzerFilter(char, token):
    return Analyzer(char_filters=char, token_filters=token)

# output
def write(anlyzed, sentences, FILE_OUTPUT):
    for token in anlyzed.analyze(sentences):
        open(FILE_OUTPUT, 'a').write(token+'\n')

# make wordcloud
def make(font_path, text) :
    return WordCloud(font_path=font_path).generate(text)

# show view
def show(result):
    pyplot.imshow(result)
    pyplot.axis('off')
    pyplot.show()

text = load(FILE_INPUT) # 読み込み
char = charFilter() # 正規表現
token = tokenFilter() # 抜き出す品詞指定
anlyzed = anlyzerFilter(char, token) # anlyze
write(anlyzed, text, FILE_OUTPUT) # 書き出し
loaded = load(FILE_OUTPUT) # 書き出されたファイルを読み込み
result = make(FONT, loaded) # wordcloud作成
show(result) # 表示


# 使用したテキストファイルについて
# 昭和二十一年憲法　日本国憲法
# https://elaws.e-gov.go.jp/document?lawid=321CONSTITUTION