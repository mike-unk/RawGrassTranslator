# -*- coding: UTF-8 -*-

from __future__ import print_function
from googletrans import Translator
import random
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


lang = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky',
        'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ny', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
n = input("Please input the number of translations [default=20]:")
if(n == ''):
    n = 20
else:
    n = int(n)
filang = input("Please input final language [default=en]:")
if(filang == ''):
    filang = 'en'
surl = input("Please input server url [default=translate.google.com]:")
if(surl == ''):
    surl = 'translate.google.com'
trans = Translator(service_urls=[surl])
infile = input("Please input input file [default=input.txt]:")
if(infile == ''):
    infile = 'input.txt'
fin = open(infile, 'r')
outfile = input("Please input output file [default=output.txt]:")
if(outfile == ''):
    outfile = 'output.txt'
fout = open(outfile, 'w')
intext = fin.read()
pdl = trans.detect(intext).lang


for i in range(1, n):
    dl = lang[random.randint(0, len(lang)-1)]
    while (dl == pdl):
        dl = lang[random.randint(0, len(lang)-1)]
    intext = trans.translate(intext, src=pdl, dest=dl).text
    eprint(i, 'from', pdl, 'to', dl)
    pdl = dl

intext = trans.translate(intext, src=pdl, dest=filang).text
eprint(n, 'from', pdl, 'to', filang)


fout.write(intext)
