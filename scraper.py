# PYTHON GENIUS SCRAPER

import requests
from bs4 import BeautifulSoup
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

GENIUS_API_KEY = os.environ.get('GENIUS_API_KEY')

base_url = 'http://api.genius.com'
headers = {
    'Authorization': 'Bearer ' + GENIUS_API_KEY
}

# list of artists to scrape from
artists = [
            'Britney Spears',
            'Queen',
            'OneRepublic',
            'Whitney Houston',
            'Stevie Wonder',
            'Bon Jovi',
            'Avril Lavigne',
            'Carly Rae Jepsen',
            'David Bowie',
            'Amy Winehouse',
            'Christina Aguilera',
            'Gwen Stefani',
            'Coldplay',
            'Frank Sinatra',
            'Celine Dion',
            'Backstreet Boys',
            'Janet Jackson',
            'Jennifer Lopez',
            'Meghan Trainor',
            'Ellie Goulding',
            'Nelly Furtado',
            'Justin Bieber',
            'Katy Perry',
            'Bruno Mars',
            'Beyonce',
            'Lorde',
            'The Weeknd',
            'John Legend',
            'Rihanna',
            'Lady Gaga',
            'Usher',
            'Miley Cyrus',
            'Taylor Swift',
            'Major Lazer',
            'One Direction',
            'Ed Sheeran',
            'Sia',
            'Ariana Grande',
            'Calvin Harris',
            'Mariah Carey',
            'Madonna',
            'Elton John',
            'The Beatles',
            'Michael Jackson',
            'Bee Gees',
            'Prince',
            'Maroon 5',
            'The Black Eyed Peas',
            'P!NK',
            'TLC',
            'R. Kelly',
            'Kelly Clarkson',
            'Justin Timberlake',
            'Alessia Cara',
            'Shawn Mendes',
            'Hailee Steinfeld',
            'Jason Derulo',
            'Adele',
            'Zedd',
            'Train',
            'Selena Gomez',
            'Kygo',
        ]

def get_lyrics(song_api_path):
    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)
    json = response.json()
    path = json['response']['song']['path']
    #print 'path %s' % path
    page_url = 'http://genius.com' + path
    page = requests.get(page_url)

    print 'Page %s' % page

    html = BeautifulSoup(page.text, 'html.parser')

    print 'HTML %s' % html

    [h.extract() for h in html('script')]
    lyrics = html.find('div', { 'class': 'lyrics'}).get_text()

    # print out the lyrics
    print 'Lyrics %s' % lyrics
    with open('data/input.txt', 'a') as f:
        f.write(lyrics.encode('utf-8'))
        f.close()

if __name__ == "__main__":
    for artist_name in artists:
        search_url = base_url + '/search?q=%s' % artist_name
        print 'Base URL: %s' % (search_url)
        print 'headers %s' % (headers)

         #send the request
        response = requests.get(search_url, headers=headers)
        json = response.json()

        #print "JSON %s" % (json)

        song_info = None

        for hit in json['response']['hits']:
            print hit['result']['api_path']
            get_lyrics(hit['result']['api_path'])
