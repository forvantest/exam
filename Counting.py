from _overlapped import NULL
from operator import attrgetter
from test import test_keywordonlyarg

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png"
    ]


def findLastWord(s):
    words = s.split('/')
    return words[len(words) - 1]


def putWord2List(list, word):
    
    for obj in list:
        if obj['value'] == word:
            obj['num'] += 1
            return
            
    obj = {'num':1, 'value':word}    
    list.append(obj)


list = []
for url in urls:
  word = findLastWord(url)
  putWord2List(list, word);
  
# sorted(list, key='value')
for i in range(0, 3):
  obj = list[i]
  print(str(obj['value']), ' ', obj['num'])
