from bs4 import BeautifulSoup
import requests
import json


def get_joke_from_link(link):
    html_soup = BeautifulSoup(requests.get(link).text, features="lxml")
    joke = html_soup.find("p").encode('raw-unicode-escape').decode('utf-8-sig')
    return remove_from_str(joke, "<p>", "</p>", "\r", "\n")


def jokes_generator():
    for link in links_generator():
        yield get_joke_from_link(link)


def json_write_to_file(data, path):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def links_generator():
    for joke_id in range(1, 1143):
        yield "http://baneks.ru/{}".format(joke_id)


def remove_from_str(string, *args):
    for arg in args:
        string = string.replace(arg, "")
    return string


if __name__ == '__main__':
    json_write_to_file([joke for joke in jokes_generator()], "jokes.json")

