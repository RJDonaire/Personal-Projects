import re
import json
import time
import requests
from bs4 import BeautifulSoup as bs

from extract_leftside import extract_leftside
from save import *

checkpoint = load_checkpoint() + 1
endpoint = checkpoint + 1000

for anime_id in range(checkpoint, endpoint):
    # site-to-visit
    url = requests.get(f'https://myanimelist.net/anime/{anime_id}')

    # soup object
    scrape = bs(url.content, 'html.parser')

    time.sleep(20)
    # scraping info

    if scrape.select("div.error404"):
        print("Webpage doesn't exist... Loading next page...\n")

        # saves 404 pages
        no_page = load_data('./data/no_anime.json')
        no_page['no_anime'].append(anime_id)
        save_data2('./data/no_anime.json', no_page)

        create_checkpoint(anime_id)
        time.sleep(10)
        continue
    else:
        # loading file
        data = load_data('./data/anime_data.json')

        # setting anime data
        title = scrape.select("div.h1-title")[0].text

        anime_data = {f'{anime_id} {title}': {}}

        # extracting anime data
        score = scrape.select("div.score-label")[0].text
        score_users = scrape.select("div[data-title='score']")[0]['data-user']
        synopsis = scrape.select("p[itemprop='description']")[0].text
        anime_info = scrape.select("div.leftside")[0].text
        anime_ls = extract_leftside(anime_info)

        anime_data[f'{anime_id} {title}']['Score'] = score
        anime_data[f'{anime_id} {title}']['Score_Users'] = score_users
        anime_data[f'{anime_id} {title}']['Synopsis'] = synopsis

        anime_data[f'{anime_id} {title}'] = {**anime_data[f'{anime_id} {title}'], **anime_ls}
        c_anime_data = {**data, **anime_data}

        # saving file
        save_data('./data/anime_data.json', c_anime_data)

        print(f'{anime_id} Processing webpage complete!\n')

    time.sleep(10)
