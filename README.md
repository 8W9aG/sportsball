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
- [tweepy](https://www.tweepy.org/)
- [pytest-is-running](https://github.com/adamchainz/pytest-is-running)
- [PySocks](https://github.com/Anorov/PySocks)
- [func-timeout](https://github.com/kata198/func_timeout)
- [tenacity](https://github.com/jd/tenacity)
- [random_user_agent](https://github.com/Luqman-Ud-Din/random_user_agent)
- [wayback](https://github.com/edgi-govdata-archiving/wayback)
- [cryptography](https://cryptography.io/en/latest/)
- [feedparser](https://github.com/kurtmckee/feedparser)
- [dateparser](https://dateparser.readthedocs.io/en/latest/)
- [playwright](https://playwright.dev/)
- [cchardet](https://github.com/PyYoshi/cChardet)
- [lxml](https://lxml.de/)
- [gender-guesser](https://github.com/lead-ratings/gender-guesser)
- [scrapesession](https://github.com/8W9aG/scrapesession)
- [pyhigh](https://github.com/sgherbst/pyhigh)
- [datefinder](https://github.com/akoumjian/datefinder)

## Raison D'être :thought_balloon:

`sportsball` aims to be a library for pulling in historical information about previous sporting games in a standardised fashion for easy data processing.
The models it uses are designed to be used for many different types of sports.

The supported leagues are:

* 🏉 [AFL](https://www.afl.com.au/)
* 🏉 [AFLW](https://www.afl.com.au/aflw)
* 🎾 [ATP](https://www.atptour.com/en)
* ⚽ [EPL](https://www.premierleague.com/ens)
* ⚽ [FIFA](https://www.fifa.com/en)
* 🐎 [HKJC](https://www.hkjc.com/home/english/index.aspx)
* 🏏 [IPL](https://www.iplt20.com/)
* ⚾ [MLB](https://www.mlb.com/)
* 🏀 [NBA](https://www.nba.com/)
* 🏀 [NCAAB](https://www.ncaa.com/sports/basketball-men/d1)
* 🏈 [NCAAF](https://www.ncaa.com/sports/football/fbs)
* 🏈 [NFL](https://www.nfl.com/)
* 🏒 [NHL](https://www.nhl.com/)
* 🏀 [WNBA](https://www.wnba.com/)
* 🎾 [WTA](https://www.wtatennis.com/)

## Architecture :triangular_ruler:

`sportsball` is an object orientated library. The entities are organised like so:

* **Game**: A game within a season.
    * **Team**: The team within the game. Note that in games with individual players a team exists as a wrapper.
        * **Player**: A player within the team.
            * **Address**: The address information of a players birth.
            * **Owner**: The owner of the player.
            * **Venue**: The college of the player.
        * **Odds**: The odds for the team to win the game.
            * **Bookie**: The bookie publishing the odds.
        * **News**: News about the team the day before the game.
        * **Social**: Social posts from the team the day before the game.
        * **Coach**: A coach for the team.
    * **Venue**: The venue the game was played in.
        * **Address**: The address information of a venue.
            * **Weather**: The weather at the address.
    * **Dividend**: The dividends the game pays out.
    * **Umpire**: The umpires adjudicating the game.

## Caching

This library uses very aggressive caching due to the large data requirements. If the requests are about a recent game (generally in the last 7 days) the caching is bypassed. The caching is as follows:

1. A joblib disk cache that caches calls to pydantic model creation functions. This changes on every version update to keep the models in sync. This is the fastest cache.
2. A requests cache backed by sqlite that caches requests forever.
3. An attempt to find the response is made to the wayback machine, and used if found.

It's very recommended that the user uses proxies defined in the `PROXIES` environment variable. The more proxies the easier it is to collect data.

## Installation :inbox_tray:

This is a python package hosted on pypi, so to install simply run the following command:

`pip install sportsball`

or install using this local repository:

`python setup.py install --old-and-unmanageable`

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
X_API_KEY=APIKEY
X_API_SECRET_KEY=APISECRETKEY
X_ACCESS_TOKEN=ACCESSTOKEN
X_ACCESS_TOKEN_SECRET=ACCESSTOKENSECRET
PROXIES=CSVPROXIESLIST
```

## License :memo:

The project is available under the [MIT License](LICENSE).
