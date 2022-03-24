import requests
from bs4 import BeautifulSoup

def CleanText(s):
	s = s.replace("\n","")
	s = s.replace("       "," ")
	s = s.replace("#","")
	return s.strip()

class AnimeDataRow:
	def GetHeaders():
		return ['rank',
		'title',
		'score',
		'scored_by_users',
		'type',
		'episodes',
		'status',
		'aired',
		'premiered',
		'broadcast',
		'producers',
		'licensors',
		'studios',
		'source',
		'genres',
		'theme',
		'demographic',
		'duration',
		'rating',
		'popularity',
		'url']

	def __init__(self, rank, title, score, url):
		self.rank = rank
		self.title = title
		self.score = score
		self.url = url
		self.scored_by_users = 0
		self.type = ''
		self.episodes = ''
		self.status = ''
		self.aired = ''
		self.premiered = ''
		self.broadcast = ''
		self.producers = ''
		self.licensors = ''
		self.studios = ''
		self.source = ''
		self.genres = ''
		self.theme = ''
		self.demographic = ''
		self.duration = ''
		self.rating = ''
		self.popularity = 0

	def IsSpaceDivTag(tag):
		return tag.name == 'div' and tag.has_attr('class') and 'spaceit_pad' in tag['class']

	def IsBorderSolid(tag):
		return tag.name == 'div' and tag.has_attr('class') and 'border_solid' in tag['class']

	def GetTagWithText(s, Text):
		tag = s.find(lambda tag: AnimeDataRow.IsSpaceDivTag(tag) and Text in tag.text)
		if tag == None:
			return ''
		else:
			return CleanText(tag.text.split(':',1)[1])

	def GetUrlBasedTag(s, Text):
		tag = s.find(lambda tag: AnimeDataRow.IsSpaceDivTag(tag) and Text in tag.text)
		if tag == None:
			return ''
		else:
			spans = tag.find_all('span' , class_='')
			result = ''
			for s in spans:
				result = result + ', ' + s.text
			return result[2:]

	def GetScoreByUsers(s):
		tag = s.find(lambda tag: AnimeDataRow.IsSpaceDivTag(tag) and 'Score' in tag.text)

		if tag == None:
			return 0
		score_tag = tag.find(lambda tag: tag.name == 'span' and tag.has_attr('itemprop') and 'ratingCount' in tag['itemprop'])
		if score_tag == None:
			return 0
		return int(score_tag.text)

	def QueryEpisodes(self):
		r = requests.get(self.url + "/episode")
		soup = BeautifulSoup(r.text, 'html.parser')
		tag = soup.find(lambda tag: AnimeDataRow.IsBorderSolid(tag))
		if tag == None:
			return str(0)
		EpisodeTag = tag.find(lambda tag: tag.name == 'span' and tag.has_attr('class') and 'di-ib' in tag['class'])
		print(EpisodeTag.text)
		if EpisodeTag == None:
			return str(0)
		Episode_text = EpisodeTag.text[1:]
		Episode_text = Episode_text.split('/')[0].replace(',','')
		return Episode_text

	def QueryInfo(self):
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, 'html.parser')

		self.type = AnimeDataRow.GetTagWithText(soup, 'Type:')
		episode_text = 'unknown'
		try:
			episode_int = int(AnimeDataRow.GetTagWithText(soup, 'Episodes:'))
			episode_text = str(episode_int)
		except ValueError:
			episode_text = self.QueryEpisodes()
		self.episodes = episode_text
		self.status = AnimeDataRow.GetTagWithText(soup, 'Status:')
		self.aired = AnimeDataRow.GetTagWithText(soup, 'Aired:')
		self.premiered = AnimeDataRow.GetTagWithText(soup, 'Premiered:')
		self.broadcast = AnimeDataRow.GetTagWithText(soup, 'Broadcast:')
		self.producers = AnimeDataRow.GetTagWithText(soup, 'Producers:')
		self.licensors = AnimeDataRow.GetTagWithText(soup, 'Licensors:')
		self.studios = AnimeDataRow.GetTagWithText(soup, 'Studios:')
		self.source = AnimeDataRow.GetTagWithText(soup, 'Source:')
		self.genres = AnimeDataRow.GetUrlBasedTag(soup, 'Genres:')
		self.theme = AnimeDataRow.GetUrlBasedTag(soup, 'Theme:')
		self.demographic = AnimeDataRow.GetUrlBasedTag(soup, 'Demographic:')
		self.duration = AnimeDataRow.GetTagWithText(soup, 'Duration:')
		self.rating = AnimeDataRow.GetTagWithText(soup, 'Rating:')
		self.popularity = int(AnimeDataRow.GetTagWithText(soup, 'Popularity:'))
		self.scored_by_users = AnimeDataRow.GetScoreByUsers(soup)

	def GetArray(self):
		return [ self.rank,
		self.title,
		self.score,
		self.scored_by_users,
		self.type,
		self.episodes,
		self.status,
		self.aired,
		self.premiered,
		self.broadcast,
		self.producers,
		self.licensors,
		self.studios,
		self.source,
		self.genres,
		self.theme,
		self.demographic,
		self.duration,
		self.rating,
		self.popularity,
		self.url]

	def __str__(self):
		return f'{self.rank}) {self.title} - {self.url}'
