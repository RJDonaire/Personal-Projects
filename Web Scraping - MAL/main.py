import os
import re
import json
import time
import requests
from bs4 import BeautifulSoup as bs

from extract_leftside import extract_leftside
from save import *

# paths
data_path = './data2/'

# files
no_anime = 'no_anime.json'
anime_file = 'anime_data.json'

# global variables
checkpoint = load_checkpoint() + 1
endpoint = checkpoint + 2500

for anime_id in range(checkpoint, endpoint):
    # site-to-visit
    url = requests.get(f'https://myanimelist.net/anime/{anime_id}')

    # soup object
    scrape = bs(url.content, 'html.parser')

    # scraping info
    if scrape.select("div.error404"):
        no_page = os.path.join(data_path, no_anime)
        print("Webpage doesn't exist... Loading next page...\n")

        no_anime_ids = load_data(os.path.join(data_path, no_anime))

        if str(anime_id) in no_anime_ids:
            print(f'Anime data overlap: {anime_id}')
            continue
        no_anime_ids[anime_id] = None
        save_data(no_page, no_anime_ids)

        time.sleep(10)
        continue

    # loading file
    anime_page = os.path.join(data_path, anime_file)
    anime_data = load_data(anime_page)

    # setting anime data
    if str(anime_id) in anime_data: 
        print(f'Anime data overlap: {anime_id}')
        continue

    anime_data[anime_id] = {}

    # extracting anime data
    title = scrape.select("div.h1-title")[0].text
    score = scrape.select("div.score-label")[0].text
    score_users = scrape.select("div[data-title='score']")[0]['data-user']
    synopsis = scrape.select("p[itemprop='description']")[0].text
    anime_info = scrape.select("div.leftside")[0].text
    anime_ls = extract_leftside(anime_info)
    
    anime_data[anime_id]['Title'] = title
    anime_data[anime_id]['Score'] = score
    anime_data[anime_id]['Score_Users'] = score_users
    anime_data[anime_id]['Synopsis'] = synopsis
    anime_data[anime_id] = {**anime_data[anime_id], **anime_ls}

    # saving file
    save_data(anime_page, anime_data)

    print(f'{anime_id} Processing webpage complete!\n')

    time.sleep(10)
