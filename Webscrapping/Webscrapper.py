import requests
from AnimeDataRow import AnimeDataRow
from bs4 import BeautifulSoup
import csv
import time

def GetAllAnimePage(Index = 0, Upcoming = False):
	AnimeList = []
	Filter = ""
	if Upcoming:
		Filter = "&type=upcoming"
	BaseUrl = "https://myanimelist.net/topanime.php?limit={0}{1}".format(Index, Filter)
	r = requests.get(BaseUrl)
	soup = BeautifulSoup(r.text, 'html.parser')
	for tag in soup.find_all('tr', class_="ranking-list"):
		rank = tag.find('span', class_='top-anime-rank-text').text
		score = tag.find('span', class_='score-label')
		h3_tag = tag.find('h3', class_='anime_ranking_h3')
		url= h3_tag.find('a')
		AnimeList.append(AnimeDataRow(int(rank),url.text,float(score.text), url['href']))
	return AnimeList

#anime = AnimeDataRow(1, "Fullmetal Alchemist: Brotherhood", 9.15, 'https://myanimelist.net/anime/42938/Fruits_Basket__The_Final')
#anime.QueryInfo()

def QueryAllAnime(index, Upcoming = False):
	AnimeList = GetAllAnimePage(index, Upcoming)
	for anime in AnimeList:
		print(f"Visiting {anime}")
		anime.QueryInfo()

	with open(f'anime_data{index}.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(AnimeDataRow.GetHeaders())
		for anime in AnimeList:
			writer.writerow(anime.GetArray())

for i in range(8400,8500,50):
	QueryAllAnime(i)
	time.sleep(60)
