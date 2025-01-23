# sportsball

<a href="https://pypi.org/project/sportsball/">
    <img alt="PyPi" src="https://img.shields.io/pypi/v/sportsball">
</a>

A library for pulling in and normalising sports stats.

<p align="center">
    <img src="sportsball.png" alt="sportsball" width="200"/>
</p>

## Dependencies :globe_with_meridians:

Python 3.11.6:

- [pandas](https://pandas.pydata.org/)
- [requests](https://requests.readthedocs.io/en/latest/)
- [requests-cache](https://requests-cache.readthedocs.io/en/stable/)
- [python-dateutil](https://github.com/dateutil/dateutil)
- [tqdm](https://github.com/tqdm/tqdm)
- [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [joblib](https://joblib.readthedocs.io/en/stable/)
- [pyarrow](https://arrow.apache.org/docs/python/index.html)
- [ipython](https://ipython.org/)
- [pytz](https://pythonhosted.org/pytz/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [geocoder](https://geocoder.readthedocs.io/)
- [retry-requests](https://github.com/bustawin/retry-requests)
- [timezonefinder](https://timezonefinder.michelfe.it/gui)
- [nba_api](https://github.com/swar/nba_api)
- [pydantic](https://docs.pydantic.dev/latest/)
- [flatten_json](https://github.com/amirziai/flatten)
- [pygooglenews](https://github.com/kotartemiy/pygooglenews)
- [extruct](https://github.com/scrapinghub/extruct)
- [wikipedia-api](https://github.com/martin-majlis/Wikipedia-API)

## Raison D'être :thought_balloon:

`sportsball` aims to be a library for pulling in historical information about previous sporting games in a standardised fashion for easy data processing.
The models it uses are designed to be used for many different types of sports.

The supported leagues are:

* 🏉 [AFL](https://www.afl.com.au/)
* 🏀 [NBA](https://www.nba.com/)
* 🏀 [NCAAB](https://www.ncaa.com/sports/basketball-men/d1)
* 🏈 [NCAAF](https://www.ncaa.com/sports/football/fbs)
* 🏈 [NFL](https://www.nfl.com/)

## Architecture :triangular_ruler:

`sportsball` is an object orientated library. The entities are organised like so:

* **League**: The entry point to accessing data about a league.
    * **Season**: A season within a league.
        * **Game**: A game within a season.
            * **Team**: The team within the game. Note that in games with individual players a team exists as a wrapper.
                * **Player**: A player within the team.
                * **Odds**: The odds for the team to win the game.
                    * **Bookie**: The bookie publishing the odds.
                * **News**: News about the team the day before the game.
            * **Venue**: The venue the game was played in.
                * **Address**: The address information of a venue.
                    * **Weather**: The weather at the address.

### Objects

A list of the attributes on each object.

#### League

A representation of a sports league containing many seasons.

* **seasons**: An iterator for all the seasons in the league.
* **league**: The league enum this league model represents.

#### Season

A representation of the season within a league.

* **year**: The year the season represents.
* **season_type**: The type of season this season represents (e.g. regular, preseason, postseason, offseason).
* **games**: An iterator for all the games in the season.

#### Game

A representation of the game within a season.

* **dt**: The timezone aware date/time of the game start.
* **week**: The round of the game within the season.
* **game_number**: The index of the game within the round.
* **venue**: The venue the game took place at.
* **teams**: A list of teams within the game.
* **home_team**: The team representing the home team.
* **away_team**: The ream representing the away team.
* **end_dt**: The timzone aware date/time of the game end.
* **attendance**: How many people attended the game.

#### Team

A representation of a team within a game.

* **identifier**: The unique identifier for the team.
* **name**: The name of the team.
* **location**: The home location of the team.
* **players**: A list of players with the team for the game.
* **odds**: A list of odds for the team on the game to win.
* **points**: The amount of points scored by this team on the game.
* **ladder_rank**: The ladder rank of the team at the beginning of the round of the game.

#### Player

A representation of a player within a team within a game.

* **identifier**: The unique identifier for the player.
* **jersey**: The jersey identifying the player.
* **kicks**: The number of kicks the player made in the game.
* **fumbles**: The number of times the player fumbled the ball in the game.
* **fumbles_lost**: The number of times the player loses possession of the ball due to a fumble and the opposing team recovers the ball.

#### Odds

A representation of the odds for a team to win within a game.

* **odds**: The decimal odds offered by a bookie for the team to win in the game.
* **bookie**: The bookie offering these odds.

#### Venue

The venue the game is played at.

* **identifier**: The unique identifier for the venue.
* **names**: The name of the venue.
* **address**: The address of the venue.
* **is_grass**: Whether the venue has a grass field.
* **is_indoor**: Whether the venue is indoors.

#### Address

The address of the venue.

* **city**: The city of the address.
* **state**: The state of the address.
* **zipcode**: The postal/zip code of the address.
* **latitude**: The latitude of the address.
* **longitude**: The longitude of the address.
* **housenumber**: The house/street number of the address.
* **weather**: The weather at the address at the game start time.
* **timezone**: The time zone at the address.
* **country**: The country of the address.

#### Weather

The forecasted weather one day out at the address of the game start time.

* **temperature**: The temperature at the address at the game start time.
* **relative_humidity**: The relative humidity at the address at the game start time.

#### News

The news one day out from the game.

* **title**: The title of the article
* **published**: When the article was published.
* **summary**: The summary of the article.
* **source**: The source of the article.

## Caching

This library uses very aggressive caching due to the large data requirements.
The initial data load will take some time however after that it will cache the old data for up to 1 year.

## Installation :inbox_tray:

This is a python package hosted on pypi, so to install simply run the following command:

`pip install sportsball`

## Usage example :eyes:

There are many different ways of using sportsball, but we generally recommend the CLI.

### CLI

To fetch a dataframe containing information about a league, you can use the following CLI:

```
sportsball --league=nfl -
```

The final argument denotes the file to write to, in this case `-` is stdout.

### Python

To pull a dataframe containing all the information for a particular league, the following example can be used:

```python
from sportsball import sportsball as spb

ball = spb.SportsBall()
league = ball.league(spb.League.AFL)
df = league.to_frame()
```

This results in a dataframe where each game is represented by all its features.

### Environment

If you wish to use the providers that require API keys, you can create a `.env` file with the following variables inside it:

```
GOOGLE_API_KEY=APIKEY
GRIBSTREAM_API_KEY=APIKEY
```

## License :memo:

The project is available under the [MIT License](LICENSE).
