# TODO dict to txt or cvs maybe with translation?
# TODO run search for each item
# TODO retrieve 1-5 images for each word via soup
# TODO keep all the work files away from the project in results folder
# TODO word lenght stats
import pycurl
from io import BytesIO
import os.path
import time
import datetime
import random
dictionary = open('Dictionary/espanol.txt', 'r', encoding="utf-8").read().splitlines()

print(len(dictionary))


def dictionary_stats(dictionary_name):
    n = 0
    for i in dictionary_name:
        if len(i) > n:
            n = len(i)
    return n


n = dictionary_stats(dictionary)


def words_lengts_stats(dictionary_name):
    counter = []
    listsize = 0
    while listsize <= n:
        counter.insert(listsize, 0)
        listsize += 1
    for i in dictionary_name:
        counter[len(i) - 1] += 1
    for i in counter:
        if i == 0:
            continue
        print("There are %r words with length of %r" % (i, counter.index(i) + 1))

        #
        #
        # abadejo
        #
        # &as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:l,itp:photo,ic:color,sur:fc


n = 0
dict_new = []
qstart = 'https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q=&as_epq='
#qend = '&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:l,itp:photo,ic:color,sur:fc'
dict_new = [qstart + i for i in dictionary]
for i in dict_new:
    writepath = 'results/' + dictionary[n] + '.html'
    print(writepath)
    if os.path.exists(writepath):
        n += 1
        continue
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, i.encode('iso-8859-1'))
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    with open(writepath, 'wb') as f:
        f.write(body)
        f.close()
    t = random.uniform(4, 7)
    print("successfull for element number %r : %r moving on to next" % (n, dictionary[n]))
    print("now we need to wait %r seconds before next request" % (t))
    n += 1
    time.sleep(t)
