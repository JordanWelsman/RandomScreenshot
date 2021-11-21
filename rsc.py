import random
import string
import webbrowser

letters = string.ascii_letters
instances = 5


def createids(instances):
    urls = [''] * instances
    for u in range(instances):
        url = ""
        for c in range(6):
            url += random.choice(letters).lower()
        # print(url)
        urls[u] = url
    return urls


def makeurl(instances):
    for u in createids(instances):
        u = ("https://prnt.sc/" + u)
        webbrowser.open(u)
    return urls


def openurl(instances):
    for i in makeurl(instances):
        webbrowser.open(i)


openurl(instances)
