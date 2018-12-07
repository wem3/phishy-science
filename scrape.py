import requests
from bs4 import BeautifulSoup

songs = ['46 Days', '1999']
url = 'http://www.ihoz.com/cgi/phish?song={}'

def parse_row(row):
    # Change this to extract whatever info you want
    print(row)
    return row

song_data = {}
for song in songs:
    html = requests.get(url.format(song))
    soup = BeautifulSoup(html, 'html.parser')
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    # Ignore the first row (the header)
    song_data[song] = [parse_row(row) for row in rows[1:]]
