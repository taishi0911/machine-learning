#!/usr/bin/env python
# coding: utf-8

import sys, re
from datetime import datetime
import numpy as np
import requests

# sentenceに含まれる名詞の出現数をカウントして辞書で返す
def wordCount(sentence):
    import MeCab
    tagger = MeCab.Tagger()
    result = tagger.parse(sentence.encode('utf-8'))
    wordCount = {}

    node = tagger.parseToNode(sentence.encode('utf-8'))
    while node:
        word = node.surface
        feat = node.feature.split(',')[0].decode('utf-8')
        # 数は名詞に分類されるがここでは除く
        isNumeric = node.feature.split(',')[1].decode('utf-8') == u"数"
        # 長さが1の単語も除く
        if 1 < len(word.decode('utf-8')) and feat == u"名詞" and not isNumeric:
            wordCount.setdefault(word, 0)
            wordCount[word] += 1
        node = node.next

    return wordCount

# urlに対応するRSS feedを取得して，含まれる記事のurlを抽出する
def getNewsUrls(url):
    import xml.etree.ElementTree as ET
    data = requests.get(url)
    xml = ET.fromstring(data.text.encode('utf-8'))
    links = []
    for link in xml.findall(".//item/link"):
        links.append(link.text)
    return links

# urlに対応する記事をWebから取得して記事本文を（不要なHTMLタグを除去して）抽出する
def getNewsContent(url):
    import lxml.html
    data = requests.get(url)
    # requestsはcharsetが指定されていないHTMLをデフォルトではISO-8859-1で解釈する
    body = lxml.html.fromstring(data.text.encode('ISO-8859-1'))
    # このHTML構造はNHK ONLINEのものとして決め打ちしている
    t = body.xpath("//div[@class='entry']")
    if len(t) > 0:
        content = t[1].text_content()
        return content
    # for debug
    with open("out.html", "w") as f:
        print "Illegal format (dump as out.html)"
        f.write(data.text.encode('utf-8'))
        exit()

if __name__ == "__main__":
    # NHKオンラインニュースを取得
    newsUrls = getNewsUrls("http://www3.nhk.or.jp/rss/news/cat1.xml")

    docCount = {} # ある単語が何記事に含まれているか
    tf = []

    for (i, url) in enumerate(newsUrls):
        news = getNewsContent(url)
        count = wordCount(news)
        tf.append(count)
        for w, _ in count.items():
            docCount.setdefault(w, 0)
            docCount[w] += 1

    # idfの計算
    D = len(newsUrls) # 全ニュース記事数
    idf = dict([(k, np.log(D/v)) for k,v in docCount.items()])

    # tf-idfの計算
    tfidf = [dict([(k, v*idf[k]) for k,v in _tf.items()]) for _tf in tf]

    filename = "newslist_{}.txt".format(datetime.now().strftime("%s"))
    with open(filename, "w") as f:
        for (i, _tfidf) in enumerate(tfidf):
            # 各ニュース記事に対してtf-idfの順に単語をソート
            words = map(lambda x:x[0], sorted(_tfidf.items(), key=lambda x:x[1], reverse=True))
            # tf-idfのtop3をその記事のキーワードとして選択
            print "{} => {}".format(newsUrls[i], ",".join(words[0:3]))
            f.write("{} => {}\n".format(newsUrls[i], ",".join(words[0:3])))

    print "Total {} news, URLs written in {}".format(D, filename)