# `SC1015 Intro to DSAI Assignment AY2021-2022`

## Tutorial Group
> SC1, Friday 1330-1530

## Team Members
- Budi Syahiddin
- Soh Wee Kiat 
- Samuel Chua


## Roadmap
- [ ] Data scraping from myanimelist
- [ ] Data cleaning
- [ ] Exploratory Analysis 
- [ ] Machine Learning ?????
- [ ] Visualisation
- [ ] Presentation Video
- [ ] Website


## Scraper Technical details
Since scraping is mostly an I/O bound task, python will be used for simplicity.

### GET Anime List
```
URL: https://myanimelist.net/topanime.php?limit={integer}
Response Type: HTML
```
`limit` can be integer value but recommended value is multiples of 50, i.e. `0,50,100` etc

#### CSS Selectors
```
String, Anime Title (with URL for anime details): tr.ranking-list:nth-child(idx) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)
    idx: int where >= 2
```

### GET Anime Details
```
# Example
URL: https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood
Response Type: HTML
```
`title` and `id` is not deterministic, so must use the previous URL to get this URL

#### CSS Selectors
```
String              Anime Overview Synopsis: 
String              Anime Overview Background: 

String,             Anime Info Title: .title-name > strong:nth-child(1)
String,             Anime Info Type: 
UInt,               Anime Info Episode:
String,             Anime Info Status: 
String,             Anime Info Aired: 
String,             Anime Info Premiered: 
Datetime,           Anime Info Broadcast: 
Array<String>,      Anime Info Producers: 
Array<String>,      Anime Info Licensors: 
Array<String>,      Anime Info Studio: 
String,             Anime Info Source: 
Array<String>,      Anime Info Genres: 
String,             Anime Info Theme: 
String,             Anime Info Demographic: 
UInt,               Anime Info Duration: 
Enum,               Anime Info Rating: 

Float,              Anime Stats Score: 
UInt,               Anime Stats Rank: 
UInt,               Anime Stats Popularity: 
UInt,               Anime Stats Members: 
UInt,               Anime Stats Favorites: 
```

## Data Cleaning
TBA