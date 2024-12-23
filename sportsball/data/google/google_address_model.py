"""Google address model."""

# pylint: disable=too-many-lines,line-too-long
import datetime
from collections import namedtuple
from typing import Any, Dict, Optional, Pattern, Union

import geocoder  # type: ignore
import pytz
import requests
from timezonefinder import TimezoneFinder  # type: ignore

from ..address_model import AddressModel
from ..openmeteo.openmeteo_weather_model import OpenmeteoWeatherModel
from ..weather_model import WeatherModel

SportsballGeocodeTuple = namedtuple(
    "SportsballGeocodeTuple", ["city", "state", "postal", "lat", "lng", "housenumber"]
)
LEVI_STADIUM = SportsballGeocodeTuple(
    city="Santa Clara",
    state="CA",
    postal="95054",
    lat=37.4033165,
    lng=-121.9719523,
    housenumber="4900",
)
ARROWHEAD_STADIUM = SportsballGeocodeTuple(
    city="Kansas City",
    state="MO",
    postal="64129",
    lat=39.0489647,
    lng=-94.486589,
    housenumber="1",
)
PAYCOR_STADIUM = SportsballGeocodeTuple(
    city="Cincinnati",
    state="OH",
    postal="45202",
    lat=39.0954576,
    lng=-84.5186326,
    housenumber="1",
)
LUMEN_FIELD = SportsballGeocodeTuple(
    city="Seattle",
    state="WA",
    postal="98134",
    lat=47.5951518,
    lng=-122.3342143,
    housenumber="800",
)
CAESARS_SUPERDOME = SportsballGeocodeTuple(
    city="New Orleans",
    state="LA",
    postal="70112",
    lat=29.951061,
    lng=-90.0838191,
    housenumber="1500",
)
TOM_BENSON_HALL_OF_FAME_STADIUM = SportsballGeocodeTuple(
    city="Canton",
    state="OH",
    postal="44708",
    lat=40.8198713,
    lng=-81.4028911,
    housenumber="",
)
GILETTE_STADIUM = SportsballGeocodeTuple(
    city="Foxborough",
    state="MA",
    postal="02035",
    lat=42.0909458,
    lng=-71.2669214,
    housenumber="1",
)
FORD_FIELD = SportsballGeocodeTuple(
    city="Detroit",
    state="MI",
    postal="48226",
    lat=42.3400064,
    lng=-83.0481779,
    housenumber="2000",
)
HARD_ROCK_STADIUM = SportsballGeocodeTuple(
    city="Miami Gardens",
    state="FL",
    postal="33056",
    lat=25.958326,
    lng=-80.2421728,
    housenumber="100",
)
RAYMOND_JAMES_STADIUM = SportsballGeocodeTuple(
    city="Tampa",
    state="FL",
    postal="33607",
    lat=27.9758691,
    lng=-82.5059093,
    housenumber="4201",
)
CLEVELAND_BROWNS_STADIUM = SportsballGeocodeTuple(
    city="Cleveland",
    state="OH",
    postal="44114",
    lat=41.5060535,
    lng=-81.702123,
    housenumber="100",
)
STATE_FARM_STADIUM = SportsballGeocodeTuple(
    city="Glendale",
    state="AZ",
    postal="85305",
    lat=33.5276247,
    lng=-112.2651342,
    housenumber="1001",
)
HIGHMARK_STADIUM = SportsballGeocodeTuple(
    city="Orchard Park",
    state="NY",
    postal="14127",
    lat=42.7737546,
    lng=-78.7895472,
    housenumber="1",
)
SOLDIER_FIELD = SportsballGeocodeTuple(
    city="Chicago",
    state="IL",
    postal="60605",
    lat=41.8623132,
    lng=-87.6192633,
    housenumber="1410",
)
BANK_OF_AMERICA_STADIUM = SportsballGeocodeTuple(
    city="Charlotte",
    state="NC",
    postal="28202",
    lat=35.2257795,
    lng=-80.8555399,
    housenumber="800",
)
ATT_STADIUM = SportsballGeocodeTuple(
    city="Arlington",
    state="TX",
    postal="76011",
    lat=32.7479966,
    lng=-97.0959914,
    housenumber="1",
)
MTT_BANK_STADIUM = SportsballGeocodeTuple(
    city="Baltimore",
    state="FL",
    postal="21230",
    lat=39.2778666,
    lng=-76.6255186,
    housenumber="101",
)
SOFI_STADIUM = SportsballGeocodeTuple(
    city="Inglewood",
    state="CA",
    postal="90301",
    lat=33.9534651,
    lng=-118.3416145,
    housenumber="1001",
)
ALLEGIANT_STADIUM = SportsballGeocodeTuple(
    city="Las Vegas",
    state="NV",
    postal="89118",
    lat=36.0908665,
    lng=-115.1858971,
    housenumber="3333",
)
LINCOLN_FINANCIAL_FIELD = SportsballGeocodeTuple(
    city="Philadelphia",
    state="PA",
    postal="19148",
    lat=39.9013695,
    lng=-75.1700964,
    housenumber="",
)
METLIFE_STADIUM = SportsballGeocodeTuple(
    city="East Rutherford",
    state="NJ",
    postal="07073",
    lat=40.8135064,
    lng=-74.0770319,
    housenumber="1",
)
MERCEDES_BANZ_STADIUM = SportsballGeocodeTuple(
    city="Atlanta",
    state="GA",
    postal="30313",
    lat=33.7553232,
    lng=-84.4031654,
    housenumber="1",
)
NRG_STADIUM = SportsballGeocodeTuple(
    city="Houston",
    state="TX",
    postal="77054",
    lat=29.6847219,
    lng=-95.4132823,
    housenumber="",
)
ACRISURE_STADIUM = SportsballGeocodeTuple(
    city="Pittsburgh",
    state="PA",
    postal="15212",
    lat=40.4467648,
    lng=-80.0183352,
    housenumber="100",
)
LUCAS_OIL_STADIUM = SportsballGeocodeTuple(
    city="Indianapolis",
    state="IN",
    postal="46225",
    lat=39.7601007,
    lng=-86.1664626,
    housenumber="500",
)
LAMBEAU_FIELD = SportsballGeocodeTuple(
    city="Green Bay",
    state="WI",
    postal="54304",
    lat=44.5013406,
    lng=-88.0647832,
    housenumber="1265",
)
US_BANK_STADIUM = SportsballGeocodeTuple(
    city="Minneapolis",
    state="MN",
    postal="55415",
    lat=44.9736461,
    lng=-93.2600694,
    housenumber="401",
)
FEDEX_FIELD = SportsballGeocodeTuple(
    city="Landover",
    state="MD",
    postal="20785",
    lat=38.9081324,
    lng=-76.8665633,
    housenumber="1600",
)
NISSAN_STADIUM = SportsballGeocodeTuple(
    city="Nashville",
    state="TN",
    postal="37213",
    lat=36.166469,
    lng=-86.7738744,
    housenumber="1",
)
EVERBANK_STADIUM = SportsballGeocodeTuple(
    city="Jacksonville",
    state="FL",
    postal="32202",
    lat=30.3239099,
    lng=-81.6399246,
    housenumber="1",
)
EMPOWER_FIELD = SportsballGeocodeTuple(
    city="Denver",
    state="CO",
    postal="80204",
    lat=39.7438895,
    lng=-105.0226843,
    housenumber="1701",
)
WEMBLEY_STADIUM = SportsballGeocodeTuple(
    city="Wembley",
    state="",
    postal="HA9 0WS",
    lat=51.5560247,
    lng=-0.2821926,
    housenumber="",
)
TOTTENHAM_HOTSPURS_STADIUM = SportsballGeocodeTuple(
    city="London",
    state="",
    postal="N17 0BX",
    lat=51.6042204,
    lng=-0.071094,
    housenumber="782",
)
DEUTSCHE_BANK_PARK = SportsballGeocodeTuple(
    city="Frankfurt am Main",
    state="",
    postal="60528",
    lat=50.0685807,
    lng=8.6428971,
    housenumber="362",
)
ALLIANZ_ARENA = SportsballGeocodeTuple(
    city="München",
    state="",
    postal="80939",
    lat=48.2187966,
    lng=11.6221325,
    housenumber="25",
)
GEORGIA_DOME = SportsballGeocodeTuple(
    city="Atlanta",
    state="GA",
    postal="",
    lat=33.758,
    lng=-84.401,
    housenumber="1",
)
TRANS_WORLD_DOME = SportsballGeocodeTuple(
    city="St. Louis",
    state="MO",
    postal="63101",
    lat=38.6328232,
    lng=-90.1910817,
    housenumber="701",
)
CANDLESTICK_PARK = SportsballGeocodeTuple(
    city="San Francisco",
    state="CA",
    postal="94124",
    lat=37.7129826,
    lng=-122.4064101,
    housenumber="",
)
SILVERDOME = SportsballGeocodeTuple(
    city="Pontiac",
    state="MI",
    postal="48342",
    lat=42.6456689,
    lng=-83.2572144,
    housenumber="",
)
TEXAS_STADIUM = SportsballGeocodeTuple(
    city="Irving",
    state="TX",
    postal="",
    lat=32.839722,
    lng=-96.9146954,
    housenumber="",
)
SDCCU_STADIUM = SportsballGeocodeTuple(
    city="San Diego",
    state="CA",
    postal="92108",
    lat=32.7809825,
    lng=-117.1244523,
    housenumber="9449",
)
MOUNTAIN_AMERICA_STADIUM = SportsballGeocodeTuple(
    city="Tempe",
    state="AZ",
    postal="85287",
    lat=33.4264574,
    lng=-111.9374442,
    housenumber="500",
)
LOS_ANGELES_MEMORIAL_COLESIUM = SportsballGeocodeTuple(
    city="Los Angeles",
    state="CA",
    postal="90037",
    lat=34.0136647,
    lng=-118.2904104,
    housenumber="3911",
)
KEZAR_STADIUM = SportsballGeocodeTuple(
    city="San Francisco",
    state="CA",
    postal="94118",
    lat=37.7669182,
    lng=-122.4567445,
    housenumber="670",
)
CITY_STADIUM = SportsballGeocodeTuple(
    city="Green Bay",
    state="WI",
    postal="54301",
    lat=44.5076658,
    lng=-87.9975486,
    housenumber="1500",
)
COTTON_BOWL = SportsballGeocodeTuple(
    city="Dallas",
    state="TX",
    postal="75215",
    lat=32.7796106,
    lng=-96.7602328,
    housenumber="3750",
)
WRIGLEY_FIELD = SportsballGeocodeTuple(
    city="Chicago",
    state="IL",
    postal="60613",
    lat=41.9484384,
    lng=-87.6579076,
    housenumber="1060",
)
YANKEE_STADIUM = SportsballGeocodeTuple(
    city="Bronx",
    state="NY",
    postal="10451",
    lat=40.8296425,
    lng=-73.9310454,
    housenumber="1",
)
TIGER_STADIUM = SportsballGeocodeTuple(
    city="Baton Rouge",
    state="LA",
    postal="70803",
    lat=30.412035,
    lng=-91.1863912,
    housenumber="",
)
RFK_STADIUM = SportsballGeocodeTuple(
    city="Washington",
    state="DC",
    postal="20003",
    lat=38.8898525,
    lng=-76.9731573,
    housenumber="2400",
)
WAR_MEMORIAL_STADIUM = SportsballGeocodeTuple(
    city="Little Rock",
    state="AR",
    postal="72205",
    lat=34.749861,
    lng=-92.3314143,
    housenumber="",
)
SHEA_STADIUM = SportsballGeocodeTuple(
    city="Flushing",
    state="NY",
    postal="11368",
    lat=40.7570861,
    lng=-73.8653052,
    housenumber="41",
)
MUNICIPAL_STADIUM = SportsballGeocodeTuple(
    city="Kansas City",
    state="MS",
    postal="",
    lat=39.087,
    lng=-94.558,
    housenumber="2123",
)
YALE_BOWL = SportsballGeocodeTuple(
    city="New Haven",
    state="CT",
    postal="06515",
    lat=41.3132191,
    lng=-72.9630891,
    housenumber="81",
)
RICE_STADIUM = SportsballGeocodeTuple(
    city="Houston",
    state="TX",
    postal="77005",
    lat=29.7162887,
    lng=-95.41188622,
    housenumber="6100",
)
ROSE_BOWL = SportsballGeocodeTuple(
    city="Pasadena",
    state="CA",
    postal="91103",
    lat=34.1613284,
    lng=-118.1702211,
    housenumber="1001",
)
MILWAUKEE_COUNTY_STADIUM = SportsballGeocodeTuple(
    city="Milwaukee",
    state="WI",
    postal="53208",
    lat=43.0303919,
    lng=-87.9787396,
    housenumber="201",
)
STANFORD_STADIUM = SportsballGeocodeTuple(
    city="Stanford",
    state="CA",
    postal="94305",
    lat=37.4345298,
    lng=-122.1636976,
    housenumber="625",
)
LIBERTY_BOWL_MEMORIAL_STADIUM = SportsballGeocodeTuple(
    city="Memphis",
    state="TN",
    postal="38119",
    lat=35.1213707,
    lng=-89.9969239,
    housenumber="959",
)
NEO_QUIMICA_ARENA = SportsballGeocodeTuple(
    city="São Paulo",
    state="SP",
    postal="08295-005",
    lat=-23.5453134,
    lng=-46.4768041,
    housenumber="111",
)
_CACHED_GEOCODES: dict[str, Any] = {
    "S.C.G. - Australia": SportsballGeocodeTuple(
        city="Moore Park",
        state="NSW",
        postal="2021",
        lat=-33.8915316,
        lng=151.2248515,
        housenumber="",
    ),
    "Victoria Park - Australia": SportsballGeocodeTuple(
        city="Abbotsford",
        state="VIC",
        postal="3067",
        lat=-37.8105167,
        lng=144.9822987,
        housenumber="",
    ),
    "Tom Benson Hall of Fame Stadium": TOM_BENSON_HALL_OF_FAME_STADIUM,
    "MetLife Stadium": METLIFE_STADIUM,
    "Gillette Stadium": GILETTE_STADIUM,
    "Acrisure Stadium": ACRISURE_STADIUM,
    "Hard Rock Stadium": HARD_ROCK_STADIUM,
    "M&T Bank Stadium": MTT_BANK_STADIUM,
    "Highmark Stadium": HIGHMARK_STADIUM,
    "U.S. Bank Stadium": US_BANK_STADIUM,
    "Cleveland Browns Stadium": CLEVELAND_BROWNS_STADIUM,
    "EverBank Stadium": EVERBANK_STADIUM,
    "Nissan Stadium": NISSAN_STADIUM,
    "Paycor Stadium": PAYCOR_STADIUM,
    "SoFi Stadium": SOFI_STADIUM,
    "State Farm Stadium": STATE_FARM_STADIUM,
    "Lucas Oil Stadium": LUCAS_OIL_STADIUM,
    "NRG Stadium": NRG_STADIUM,
    "Soldier Field": SOLDIER_FIELD,
    "GEHA Field at Arrowhead Stadium": ARROWHEAD_STADIUM,
    "Bank of America Stadium": BANK_OF_AMERICA_STADIUM,
    "Allegiant Stadium": ALLEGIANT_STADIUM,
    "Empower Field at Mile High": EMPOWER_FIELD,
    "Levi's Stadium": LEVI_STADIUM,
    "Mercedes-Benz Stadium": MERCEDES_BANZ_STADIUM,
    "Raymond James Stadium": RAYMOND_JAMES_STADIUM,
    "Lambeau Field": LAMBEAU_FIELD,
    "Lincoln Financial Field": LINCOLN_FINANCIAL_FIELD,
    "Ford Field": FORD_FIELD,
    "AT&T Stadium": ATT_STADIUM,
    "Lumen Field": LUMEN_FIELD,
    "Caesars Superdome": CAESARS_SUPERDOME,
    "Neo Química Arena": NEO_QUIMICA_ARENA,
    "FedExField": FEDEX_FIELD,
    "Tottenham Hotspur Stadium": TOTTENHAM_HOTSPURS_STADIUM,
    "Wembley Stadium": WEMBLEY_STADIUM,
    "Allianz Arena": ALLIANZ_ARENA,
    "Levi Stadium": LEVI_STADIUM,
    "Levi’s Stadium": LEVI_STADIUM,
    "Deutsche Bank Park": DEUTSCHE_BANK_PARK,
    "Arrowhead Stadium": ARROWHEAD_STADIUM,
    "Paul Brown Stadium": PAYCOR_STADIUM,
    "Trans World Dome": TRANS_WORLD_DOME,
    "Kingdome": LUMEN_FIELD,
    "Georgia Dome": GEORGIA_DOME,
    "Louisiana Superdome": CAESARS_SUPERDOME,
    "Tom Benson Hall of Fame Stadium - Canton - OH - 44708": TOM_BENSON_HALL_OF_FAME_STADIUM,
    "Gillette Stadium - Foxborough - MA - 02035": GILETTE_STADIUM,
    "Lumen Field - Seattle - WA - 98134": LUMEN_FIELD,
    "Paycor Stadium - Cincinnati - OH - 45202": PAYCOR_STADIUM,
    "Ford Field - Detroit - MI - 48226": FORD_FIELD,
    "Hard Rock Stadium - Miami Gardens - FL - 33056": HARD_ROCK_STADIUM,
    "Raymond James Stadium - Tampa - FL - 33607": RAYMOND_JAMES_STADIUM,
    "Huntington Bank Field - Cleveland - OH - 44114": CLEVELAND_BROWNS_STADIUM,
    "State Farm Stadium - Glendale - AZ - 85305": STATE_FARM_STADIUM,
    "Highmark Stadium - Orchard Park - NY - 14127": HIGHMARK_STADIUM,
    "Soldier Field - Chicago - IL - 60605": SOLDIER_FIELD,
    "Bank of America Stadium - Charlotte - NC - 28202": BANK_OF_AMERICA_STADIUM,
    "AT&T Stadium - Arlington - TX - 76011": ATT_STADIUM,
    "M&T Bank Stadium - Baltimore - MD - 21230": MTT_BANK_STADIUM,
    "SoFi Stadium - Inglewood - CA - 90301": SOFI_STADIUM,
    "Caesars Superdome - New Orleans - LA - 70112": CAESARS_SUPERDOME,
    "Allegiant Stadium - Las Vegas - NV - 89118": ALLEGIANT_STADIUM,
    "Lincoln Financial Field - Philadelphia - PA - 19148": LINCOLN_FINANCIAL_FIELD,
    "MetLife Stadium - East Rutherford - NJ - 07073": METLIFE_STADIUM,
    "Mercedes-Benz Stadium - Atlanta - GA - 30313": MERCEDES_BANZ_STADIUM,
    "NRG Stadium - Houston - TX - 77054": NRG_STADIUM,
    "Acrisure Stadium - Pittsburgh - PA - 15212": ACRISURE_STADIUM,
    "Lucas Oil Stadium - Indianapolis - IN - 46225": LUCAS_OIL_STADIUM,
    "Lambeau Field - Green Bay - WI - 54304": LAMBEAU_FIELD,
    "U.S. Bank Stadium - Minneapolis - MN - 55415": US_BANK_STADIUM,
    "Levi's Stadium - Santa Clara - CA - 95054": LEVI_STADIUM,
    "Northwest Stadium - Landover - MD - 20785": FEDEX_FIELD,
    "Nissan Stadium - Nashville - TN - 37213": NISSAN_STADIUM,
    "GEHA Field at Arrowhead Stadium - Kansas City - MO - 64129": ARROWHEAD_STADIUM,
    "EverBank Stadium - Jacksonville - FL - 32202": EVERBANK_STADIUM,
    "Empower Field at Mile High - Denver - CO - 80204": EMPOWER_FIELD,
    "Brunswick St - Australia": SportsballGeocodeTuple(
        city="Fitzroy North",
        state="VIC",
        postal="3068",
        lat=-37.7891016,
        lng=144.9759327,
        housenumber="1",
    ),
    "Corio Oval - Australia": SportsballGeocodeTuple(
        city="East Geelong",
        state="VIC",
        postal="3219",
        lat=-38.1525822,
        lng=144.3787522,
        housenumber="5",
    ),
    "Lake Oval - Australia": SportsballGeocodeTuple(
        city="Albert Park",
        state="VIC",
        postal="3206",
        lat=-37.8403445,
        lng=144.9458567,
        housenumber="",
    ),
    "East Melbourne - Australia": SportsballGeocodeTuple(
        city="Richmond",
        state="VIC",
        postal="3002",
        lat=-37.8174763,
        lng=144.9777351,
        housenumber="",
    ),
    "Junction Oval - Australia": SportsballGeocodeTuple(
        city="St Kilda",
        state="VIC",
        postal="3182",
        lat=-37.8559698,
        lng=144.9779958,
        housenumber="",
    ),
    "M.C.G. - Australia": SportsballGeocodeTuple(
        city="Richmond",
        state="VIC",
        postal="3002",
        lat=-37.8199668,
        lng=144.9785784,
        housenumber="",
    ),
    "Princes Park - Australia": SportsballGeocodeTuple(
        city="Carlton North",
        state="VIC",
        postal="3054",
        lat=-37.7849821,
        lng=144.9565047,
        housenumber="200-590",
    ),
    "Wembley Stadium - London": WEMBLEY_STADIUM,
    "Tottenham Hotspur Stadium - London": TOTTENHAM_HOTSPURS_STADIUM,
    "Punt Rd - Australia": SportsballGeocodeTuple(
        city="East Melbourne",
        state="VIC",
        postal="3002",
        lat=-37.8222208,
        lng=144.9856865,
        housenumber="",
    ),
    "Frankfurt Stadium - Frankfurt": DEUTSCHE_BANK_PARK,
    "Windy Hill - Australia": SportsballGeocodeTuple(
        city="Essendon",
        state="VIC",
        postal="3040",
        lat=-37.7515878,
        lng=144.9001347,
        housenumber="",
    ),
    "Camping World Stadium - Orlando - FL - 32805": SportsballGeocodeTuple(
        city="Orlando",
        state="FL",
        postal="32805",
        lat=28.5390192,
        lng=-81.4033962,
        housenumber="1",
    ),
    "Allianz Arena - Munich": ALLIANZ_ARENA,
    "Estadio Azteca - Mexico City": SportsballGeocodeTuple(
        city="Ciudad de México",
        state="CDMX",
        postal="04650",
        lat=19.3028606,
        lng=-99.1553986,
        housenumber="3465",
    ),
    "Glenferrie Oval - Australia": SportsballGeocodeTuple(
        city="Hawthorn",
        state="VIC",
        postal="3122",
        lat=-37.8206183,
        lng=145.0303644,
        housenumber="34",
    ),
    "Dignity Health Sports Park - Carson - CA - 90746": SportsballGeocodeTuple(
        city="Carson",
        state="CA",
        postal="90746",
        lat=33.8643776,
        lng=-118.2660135,
        housenumber="18400",
    ),
    "Arden St - Australia": SportsballGeocodeTuple(
        city="North Melbourne",
        state="VIC",
        postal="3051",
        lat=-37.7989787,
        lng=144.9388898,
        housenumber="204-206",
    ),
    "Oakland Coliseum - Oakland - CA - 94621": SportsballGeocodeTuple(
        city="Oakland",
        state="CA",
        postal="94621",
        lat=37.7514142,
        lng=-122.2034855,
        housenumber="204-206",
    ),
    "Los Angeles Memorial Coliseum - Los Angeles - CA - 90037": LOS_ANGELES_MEMORIAL_COLESIUM,
    "Western Oval - Australia": SportsballGeocodeTuple(
        city="Parkville",
        state="VIC",
        postal="3052",
        lat=-37.7781687,
        lng=144.9505349,
        housenumber="",
    ),
    "Twickenham Stadium - London": SportsballGeocodeTuple(
        city="Twickenham",
        state="",
        postal="TW2 7BA",
        lat=51.4559558,
        lng=-0.34408,
        housenumber="200",
    ),
    "Olympic Park - Australia": SportsballGeocodeTuple(
        city="Heidelberg West",
        state="VIC",
        postal="3081",
        lat=-37.7397886,
        lng=145.0317471,
        housenumber="",
    ),
    "Georgia Dome - Atlanta - GA": GEORGIA_DOME,
    "SDCCU Stadium - San Diego - CA": SDCCU_STADIUM,
    "Kardinia Park - Australia": SportsballGeocodeTuple(
        city="South Geelong",
        state="VIC",
        postal="3220",
        lat=-38.1579979,
        lng=144.3520981,
        housenumber="370",
    ),
    "The Dome at America's Center - St. Louis - MO - 63101": TRANS_WORLD_DOME,
    "Huntington Bank Stadium - Minneapolis - MN - 55455": US_BANK_STADIUM,
    "Yarraville Oval - Australia": SportsballGeocodeTuple(
        city="Yarraville",
        state="VIC",
        postal="3013",
        lat=-37.8150875,
        lng=144.8824932,
        housenumber="",
    ),
    "Candlestick Park - San Francisco - CA": CANDLESTICK_PARK,
    "Mall of America Field - Minneapolis - MN - 55415": US_BANK_STADIUM,
    "Toorak Park - Australia": SportsballGeocodeTuple(
        city="Armadale",
        state="VIC",
        postal="3143",
        lat=-37.8528107,
        lng=145.0114987,
        housenumber="580",
    ),
    "Rogers Centre - Toronto - ON": SportsballGeocodeTuple(
        city="Toronto",
        state="ON",
        postal="M5V 1J1",
        lat=43.6415757,
        lng=-79.3942991,
        housenumber="580",
    ),
    "Euroa - Australia": SportsballGeocodeTuple(
        city="Euroa",
        state="VIC",
        postal="3666",
        lat=-36.7464868,
        lng=145.5724273,
        housenumber="",
    ),
    "Aloha Stadium - Honolulu - HI - 96818": SportsballGeocodeTuple(
        city="Aiea",
        state="HI",
        postal="96701",
        lat=21.3728016,
        lng=-157.9348645,
        housenumber="99-500",
    ),
    "Giants Stadium - East Rutherford - NJ": METLIFE_STADIUM,
    "Metrodome - Minneapolis - MN - 55415": US_BANK_STADIUM,
    "North Hobart - Australia": SportsballGeocodeTuple(
        city="North Hobart",
        state="TAS",
        postal="7000",
        lat=-42.8682555,
        lng=147.3146486,
        housenumber="1-5",
    ),
    "Texas Stadium - Irving - TX": TEXAS_STADIUM,
    "Yallourn - Australia": SportsballGeocodeTuple(
        city="Yallourn North",
        state="VIC",
        postal="3825",
        lat=-38.1629374,
        lng=146.3595115,
        housenumber="",
    ),
    "Albury - Australia": SportsballGeocodeTuple(
        city="Hamilton Valley",
        state="NSW",
        postal="2641",
        lat=-36.0349793,
        lng=146.9073391,
        housenumber="1",
    ),
    "Invesco Field - Denver - CO - 80804": EMPOWER_FIELD,
    "Brisbane Exhibition - Australia": SportsballGeocodeTuple(
        city="Bowen Hills",
        state="QLD",
        postal="4006",
        lat=-27.4503048,
        lng=153.0301872,
        housenumber="600",
    ),
    "Monster Park - San Francisco - CA - 94124": CANDLESTICK_PARK,
    "RCA Dome - Indianapolis - IN": LUCAS_OIL_STADIUM,
    "Mountain America Stadium - Tempe - AZ - 85287": MOUNTAIN_AMERICA_STADIUM,
    "Veterans Stadium - Philadelphia - PA": LINCOLN_FINANCIAL_FIELD,
    "Silverdome - Pontiac - MI": SILVERDOME,
    "Giants Stadium": METLIFE_STADIUM,
    "Mile High Stadium": EMPOWER_FIELD,
    "Pontiac Silverdome": SILVERDOME,
    "Foxboro Stadium": GILETTE_STADIUM,
    "Veterans Stadium": LINCOLN_FINANCIAL_FIELD,
    "Texas Stadium": TEXAS_STADIUM,
    "Three Rivers Stadium": ACRISURE_STADIUM,
    "Qualcomm Stadium": SDCCU_STADIUM,
    "Sun Devil Stadium": MOUNTAIN_AMERICA_STADIUM,
    "Three Rivers Stadium - Pittsburgh - PA": ACRISURE_STADIUM,
    "Moorabbin Oval - Australia": SportsballGeocodeTuple(
        city="Moorabbin",
        state="VIC",
        postal="3189",
        lat=-37.9371257,
        lng=145.0404112,
        housenumber="3",
    ),
    "Vanderbilt Stadium": SportsballGeocodeTuple(
        city="Nashville",
        state="TN",
        postal="37212",
        lat=36.1438701,
        lng=-86.8284249,
        housenumber="",
    ),
    "Liberty Bowl Memorial Stadium": LIBERTY_BOWL_MEMORIAL_STADIUM,
    "RFK Stadium": RFK_STADIUM,
    "Astrodome": NRG_STADIUM,
    "Cleveland Municipal Stadium": CLEVELAND_BROWNS_STADIUM,
    "Riverfront Stadium": PAYCOR_STADIUM,
    "Candlestick Park": CANDLESTICK_PARK,
    "Los Angeles Memorial Coliseum": LOS_ANGELES_MEMORIAL_COLESIUM,
    "Coburg Oval - Australia": SportsballGeocodeTuple(
        city="Coburg",
        state="VIC",
        postal="3058",
        lat=-37.7437207,
        lng=144.9671031,
        housenumber="",
    ),
    "Waverley Park - Australia": SportsballGeocodeTuple(
        city="Mulgrave",
        state="VIC",
        postal="3170",
        lat=-37.9258818,
        lng=145.1869239,
        housenumber="2A",
    ),
    "Rose Bowl": ROSE_BOWL,
    "Miami Orange Bowl": SportsballGeocodeTuple(
        city="Miami",
        state="FL",
        postal="33125",
        lat=25.7781487,
        lng=-80.2221747,
        housenumber="501",
    ),
    "Stanford Stadium": STANFORD_STADIUM,
    "Milwaukee County Stadium": MILWAUKEE_COUNTY_STADIUM,
    "Shea Stadium": SHEA_STADIUM,
    "Schaefer Stadium": GILETTE_STADIUM,
    "Yale Bowl": YALE_BOWL,
    "Tiger Stadium": TIGER_STADIUM,
    "War Memorial Stadium": WAR_MEMORIAL_STADIUM,
    "Yankee Stadium": YANKEE_STADIUM,
    "Municipal Stadium": MUNICIPAL_STADIUM,
    "Cotton Bowl": COTTON_BOWL,
    "Kezar Stadium": KEZAR_STADIUM,
    "Franklin Field": SportsballGeocodeTuple(
        city="Philadelphia",
        state="PA",
        postal="19104",
        lat=39.9502158,
        lng=-75.1949801,
        housenumber="235",
    ),
    "Wrigley Field": WRIGLEY_FIELD,
    "City Stadium": CITY_STADIUM,
    "IG Field - Winnipeg - MB": SportsballGeocodeTuple(
        city="Winnipeg",
        state="MB",
        postal="R3T 1Z2",
        lat=49.8077033,
        lng=-97.1456866,
        housenumber="315",
    ),
    "Subiaco - Australia": SportsballGeocodeTuple(
        city="Subiaco",
        state="WA",
        postal="6008",
        lat=-31.9444594,
        lng=115.8285952,
        housenumber="304",
    ),
    "Rice Stadium": RICE_STADIUM,
    "Gabba - Australia": SportsballGeocodeTuple(
        city="Woolloongabba",
        state="QLD",
        postal="4102",
        lat=-27.4858375,
        lng=153.0332144,
        housenumber="",
    ),
    "Independence Stadium - 71109": SportsballGeocodeTuple(
        city="Shreveport",
        state="LA",
        postal="71109",
        lat=32.475745,
        lng=-93.7944423,
        housenumber="3301",
    ),
    "Carrara - Australia": SportsballGeocodeTuple(
        city="Carrara",
        state="QLD",
        postal="4211",
        lat=-28.0063039,
        lng=153.3645259,
        housenumber="",
    ),
    "W.A.C.A. - Australia": SportsballGeocodeTuple(
        city="East Perth",
        state="WA",
        postal="6004",
        lat=-31.959812,
        lng=115.874661,
        housenumber="",
    ),
    "Los Angeles Memorial Coliseum - Los Angeles, California - United States": LOS_ANGELES_MEMORIAL_COLESIUM,
    "Memorial Stadium (Lincoln) - Terre Haute, Indiana, USA - United States": SportsballGeocodeTuple(
        city="Lincoln",
        state="NE",
        postal="68588",
        lat=40.8206975,
        lng=-96.7081629,
        housenumber="1",
    ),
    "Kezar Stadium - San Francisco, California - United States": KEZAR_STADIUM,
    "Cotton Bowl - Dallas, Texas - United States": COTTON_BOWL,
    "Wrigley Field - Chicago, Illinois - United States": WRIGLEY_FIELD,
    "Yankee Stadium - Bronx, New York - United States": YANKEE_STADIUM,
    "Tiger Stadium - Baton Rouge, Louisiana, USA - United States": TIGER_STADIUM,
    "Lambeau Field - Green Bay, Wisconsin - United States": LAMBEAU_FIELD,
    "RFK Stadium - Washington DC - United States": RFK_STADIUM,
    "War Memorial Stadium - Little Rock, Arkansas - United States": WAR_MEMORIAL_STADIUM,
    "Three Rivers Stadium - Pittsburgh, PA - United States": ACRISURE_STADIUM,
    "Astrodome - Houston, TX - United States": NRG_STADIUM,
    "Mile High Stadium -  - ": EMPOWER_FIELD,
    "Football Park - Australia": SportsballGeocodeTuple(
        city="West Lakes",
        state="SA",
        postal="5021",
        lat=-34.8797138,
        lng=138.4910204,
        housenumber="",
    ),
    "Docklands - Australia": SportsballGeocodeTuple(
        city="Docklands",
        state="VIC",
        postal="3008",
        lat=-37.8165647,
        lng=144.9449306,
        housenumber="740",
    ),
    "Manuka Oval - Australia": SportsballGeocodeTuple(
        city="Griffith",
        state="ACT",
        postal="2603",
        lat=-35.3181329,
        lng=149.1297911,
        housenumber="",
    ),
    "Stadium Australia - Australia": SportsballGeocodeTuple(
        city="Sydney Olympic Park",
        state="NSW",
        postal="2127",
        lat=-33.8471156,
        lng=151.0608386,
        housenumber="",
    ),
    "York Park - Australia": SportsballGeocodeTuple(
        city="Invermay",
        state="TAS",
        postal="7248",
        lat=-41.4259371,
        lng=147.137879,
        housenumber="2",
    ),
    "Marrara Oval - Australia": SportsballGeocodeTuple(
        city="Marrara",
        state="NT",
        postal="0812",
        lat=-12.3991939,
        lng=130.8847367,
        housenumber="70",
    ),
    "Adelaide Oval - Australia": SportsballGeocodeTuple(
        city="North Adelaide",
        state="SA",
        postal="5006",
        lat=-34.9156273,
        lng=138.5914356,
        housenumber="70",
    ),
    "Sydney Showground - Australia": SportsballGeocodeTuple(
        city="Sydney Olympic Park",
        state="NSW",
        postal="2127",
        lat=-33.8430698,
        lng=151.0651214,
        housenumber="",
    ),
    "Bellerive Oval - Australia": SportsballGeocodeTuple(
        city="Bellerive",
        state="TAS",
        postal="7018",
        lat=-42.8772962,
        lng=147.3691419,
        housenumber="15",
    ),
    "Cazaly's Stadium - Australia": SportsballGeocodeTuple(
        city="Westcourt",
        state="QLD",
        postal="4870",
        lat=-16.9357343,
        lng=145.7464957,
        housenumber="",
    ),
    "Wellington - Australia": SportsballGeocodeTuple(
        city="Pipitea",
        state="",
        postal="6140",
        lat=-41.2729198,
        lng=174.7846279,
        housenumber="105",
    ),
    "Traeger Park - Australia": SportsballGeocodeTuple(
        city="The Gap",
        state="NT",
        postal="0870",
        lat=-23.7090566,
        lng=133.8701488,
        housenumber="",
    ),
    "Eureka Stadium - Australia": SportsballGeocodeTuple(
        city="Wendouree",
        state="VIC",
        postal="3355",
        lat=-37.5386166,
        lng=143.8273839,
        housenumber="725",
    ),
    "Perth Stadium - Australia": SportsballGeocodeTuple(
        city="Burswood",
        state="WA",
        postal="6100",
        lat=-31.9511597,
        lng=115.884175,
        housenumber="333",
    ),
    "Jiangwan Stadium - Australia": SportsballGeocodeTuple(
        city="Shanghai",
        state="",
        postal="200433",
        lat=31.3076026,
        lng=121.5160351,
        housenumber="",
    ),
    "Soldier Field - Chicago, Illinois - United States": SOLDIER_FIELD,
    "Arrowhead Stadium - Kansas City, Missouri - United States": ARROWHEAD_STADIUM,
    "Yale Bowl - New Haven, Connecticut, USA - United States": YALE_BOWL,
    "Rice Stadium - Houston, Texas, U.S. - United States": RICE_STADIUM,
    "Giants Stadium - New York - United States": METLIFE_STADIUM,
    "Rose Bowl - Hampshire - England": ROSE_BOWL,
    "Riverfront Stadium - Cincinnati, OH - United States": PAYCOR_STADIUM,
    "Kingdome - Seattle, WA - United States": LUMEN_FIELD,
    "Milwaukee County Stadium - Milwaukee, WI - United States": MILWAUKEE_COUNTY_STADIUM,
    "Candlestick Park - San Francisco, CA - United States": CANDLESTICK_PARK,
    "Cleveland Municipal Stadium - Cleveland, OH - United States": CLEVELAND_BROWNS_STADIUM,
    "Stanford Stadium - Stanford, California, USA - United States": STANFORD_STADIUM,
    "Sun Devil Stadium - Tempe, Arizona, USA - United States": MOUNTAIN_AMERICA_STADIUM,
    "Liberty Bowl Memorial Stadium - Memphis, Tennessee, USA - United States": LIBERTY_BOWL_MEMORIAL_STADIUM,
    "Qualcomm Stadium - San Diego, California - United States": SDCCU_STADIUM,
    "Raymond James Stadium - Tampa Bay, Florida, USA - United States": RAYMOND_JAMES_STADIUM,
    "Cleveland Browns Stadium - Cleveland, Ohio - United States": CLEVELAND_BROWNS_STADIUM,
    "Citi Field - Flushing, New York - United States": SHEA_STADIUM,
    "Bruce Stadium - Australia": SportsballGeocodeTuple(
        city="Bruce",
        state="ACT",
        postal="2617",
        lat=-35.249994,
        lng=149.1001351,
        housenumber="",
    ),
    "Blacktown - Australia": SportsballGeocodeTuple(
        city="Rooty Hill",
        state="NSW",
        postal="2766",
        lat=-33.7695492,
        lng=150.8558658,
        housenumber="",
    ),
    "Gillette Stadium - Foxborough, Massachusetts - United States": GILETTE_STADIUM,
    "Riverway Stadium - Australia": SportsballGeocodeTuple(
        city="Thuringowa Central",
        state="QLD",
        postal="4817",
        lat=-19.3176321,
        lng=146.7270047,
        housenumber="",
    ),
    "Norwood Oval - Australia": SportsballGeocodeTuple(
        city="Norwood",
        state="SA",
        postal="5067",
        lat=-34.9198089,
        lng=138.6278735,
        housenumber="",
    ),
    "Summit Sports Park - Australia": SportsballGeocodeTuple(
        city="Mount Barker Summit",
        state="SA",
        postal="5251",
        lat=-35.0779754,
        lng=138.8908443,
        housenumber="304",
    ),
    "Mile High": EMPOWER_FIELD,
    "Nissan Stadium - Nashville, Tennessee, USA - United States": NISSAN_STADIUM,
    "SoFi Stadium - Inglewood, CA - United States": SOFI_STADIUM,
    "Highmark Stadium - Orchard Park, New York - United States": HIGHMARK_STADIUM,
    "Mercedes-Benz Stadium - Atlanta, Georgia - United States": MERCEDES_BANZ_STADIUM,
    "Lucas Oil Stadium - Indianapolis, Indiana, USA - United States": LUCAS_OIL_STADIUM,
    "U.S. Bank Stadium - Minneapolis, Minnesota, USA - United States": US_BANK_STADIUM,
    "Caesars Superdome - New Orleans, Louisiana, United States - United States": CAESARS_SUPERDOME,
    "Acrisure Stadium - Pittsburgh, Pennsylvania, USA - United States": ACRISURE_STADIUM,
    "FedExField - Landover, Maryland, USA - United States": FEDEX_FIELD,
    "M&T Bank Stadium - Baltimore, Maryland - United States": MTT_BANK_STADIUM,
    "Empower Field at Mile High - Denver, Colorado, USA - United States": EMPOWER_FIELD,
    "Lumen Field - Seattle, WA, USA - United States": LUMEN_FIELD,
    "MetLife Stadium - East Rutherford, New Jersey - United States": METLIFE_STADIUM,
    "Lincoln Financial Field - Philadelphia, Pennsylvania - United States": LINCOLN_FINANCIAL_FIELD,
    "Paycor Stadium - Cincinnati, Ohio - United States": PAYCOR_STADIUM,
    "Ford Field - Detroit, Michigan - United States": FORD_FIELD,
    "EverBank Stadium - Jacksonville, Florida - United States": EVERBANK_STADIUM,
    "NRG Stadium - Houston, Texas, USA - United States": NRG_STADIUM,
    "State Farm Stadium - Glendale, Arizona - United States": STATE_FARM_STADIUM,
    "AT&T Stadium - Arlington, Texas, USA - United States": ATT_STADIUM,
    "Bank of America Stadium - Charlotte, NC, United States - United States": BANK_OF_AMERICA_STADIUM,
    "Hard Rock Stadium - Coral Gables, Florida, USA - United States": HARD_ROCK_STADIUM,
    "GEHA Field at Arrowhead Stadium - Kansas City, Missouri, United States - United States": ARROWHEAD_STADIUM,
    "Wembley Stadium - Wembley, London - International": WEMBLEY_STADIUM,
    "Tottenham Hotspur Stadium - Bill Nicholson Way, Tottenham, London - England": TOTTENHAM_HOTSPURS_STADIUM,
    "Deutsche Bank Park - Frankfurt, Germany - Germany": DEUTSCHE_BANK_PARK,
    "Arlington Stadium - Arlington, TX - United States": ATT_STADIUM,
    "Allegiant Stadium - Paradise, Nevada, USA - United States": ALLEGIANT_STADIUM,
    "Neo Química Arena - São Paulo, Brazil - Brazil": NEO_QUIMICA_ARENA,
    "Allianz Arena - Munich, Germany - Germany": ALLIANZ_ARENA,
    "Levi's Stadium - Santa Clara, California, USA - United States": LEVI_STADIUM,
}


class GoogleAddressModel(AddressModel):
    """Google implementation of the address model."""

    def __init__(
        self, query: str, session: requests.Session, dt: datetime.datetime
    ) -> None:
        g = _CACHED_GEOCODES.get(query)
        if g is None:
            g = geocoder.google(query, session=session)
            _CACHED_GEOCODES[query] = g
        super().__init__(session, g.city, g.state, g.postal)
        if g.lat is None or g.lng is None:
            print(f"Failed to reverse geocode {query}")
        self._latitude = g.lat
        self._longitude = g.lng
        self._housenumber = g.housenumber
        self._dt = dt
        self._tz = None
        if self._latitude is not None and self._longitude is not None:
            tf = TimezoneFinder()
            self._tz = tf.timezone_at(lng=self._longitude, lat=self._latitude)

    @property
    def latitude(self) -> float | None:
        """Return the latitude."""
        return self._latitude

    @property
    def longitude(self) -> float | None:
        """Return the longitude."""
        return self._longitude

    @property
    def housenumber(self) -> str | None:
        """Return the housenumber."""
        return self._housenumber

    @property
    def weather(self) -> WeatherModel | None:
        """Return the weather."""
        latitude = self._latitude
        longitude = self._longitude
        if latitude is None or longitude is None:
            return None
        dt = self._dt
        timezone = self.timezone
        if (
            dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None
        ) and timezone is not None:
            dt = pytz.timezone(timezone).localize(dt)
        if dt >= datetime.datetime.now(datetime.timezone.utc):
            return None
        if dt <= pytz.utc.localize(datetime.datetime(year=1940, month=1, day=1)):
            return None
        return OpenmeteoWeatherModel(
            self.session, self._latitude, self._longitude, dt, timezone
        )

    @property
    def timezone(self) -> str:
        """Return the timezone."""
        tz = self._tz
        if tz is None:
            tz = "UTC"
        return tz

    @staticmethod
    def urls_expire_after() -> (
        Dict[
            Union[str, Pattern[Any]],
            Optional[Union[int, float, str, datetime.datetime, datetime.timedelta]],
        ]
    ):
        """Return the URL cache rules."""
        return {}
