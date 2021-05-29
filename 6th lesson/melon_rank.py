import bs4
import requests
import csv

headers = {
    'User-Agent': 'Not Suspicious'
}

response = requests.get('https://www.melon.com', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
songs = soup.select('.on.nth1 >.list_wrap.typeRealtime>ul>.rank_item')

i = 1
with open('melon_rank.csv', 'w') as file:
    writer = csv.writer(file)
    for song in songs:
        rank = i
        title = song.select_one('div.rank_cntt > div.rank_info > p.song > a').text
        artist = song.select_one('div.rank_cntt > div.rank_info > div.artist > div.ellipsis > a').text
        writer.writerow([rank, title, artist])
        i += 1