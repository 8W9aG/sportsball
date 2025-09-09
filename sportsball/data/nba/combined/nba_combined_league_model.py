"""NBA combined league model."""

# pylint: disable=line-too-long
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.nba_espn_league_model import NBAESPNLeagueModel
from ..nba.nba_nba_league_model import NBANBALeagueModel
from ..nbacom.nba_nbacom_league_model import NBANBAComLeagueModel
from ..oddsportal.nba_oddsportal_league_model import NBAOddsPortalLeagueModel

ORLANDO_MAGIC = "1610612753"
ATLANTA_HAWKS = "1610612737"
PORTLAND_TRAIL_BLAZERS = "1610612757"
DENVER_NUGGETS = "1610612743"
MIAMI_HEAT = "1610612748"
LOS_ANGELES_LAKERS = "1610612747"
BOSTON_CELTICS = "1610612738"
OKLAHOMA_CITY_THUNDER = "1610612760"
SACRAMENTO_KINGS = "1610612758"
INDIANA_PACERS = "1610612754"
SAN_ANTONIO_SPURS = "1610612759"
PHOENIX_SUNS = "1610612756"
WASHINGTON_WIZARDS = "1610612764"
PHILADELPHIA_76ERS = "1610612755"
TORONTO_RAPTORS = "1610612761"
GOLDEN_STATE_WARRIORS = "1610612744"
MINNESOTA_TIMBERWOLVES = "1610612750"
HOUSTON_ROCKETS = "1610612745"
MEMPHIS_GRIZZLIES = "1610612763"
NEW_YORK_KNICKS = "1610612752"
CHARLOTTE_HORNETS = "1610612766"
BROOKLYN_NETS = "1610612751"
DALLAS_MAVERICKS = "1610612742"
CLEVELAND_CAVALIERS = "1610612739"
MILWAUKEE_BUCKS = "1610612749"
DETROIT_PISTONS = "1610612765"
NEW_ORLEANS_PELICANS = "1610612740"
CHICAGO_BULLS = "1610612741"
LA_CLIPPERS = "1610612746"
UTAH_JAZZ = "1610612762"
UNKNOWN = "1610616842"
TEAM_JALEN = "1610616849"
TEAM_TAMIKA = "1610616850"
TEAM_PAU = "1610616847"
TEAM_DETLEF = "1610616848"
TEAM_STEPHEN_A = "1610616840"
EAST_NBA_ALL_STARS = "1610616833"
WEST_NBA_ALL_STARS = "1610616834"
TEAM_SHANNON = "1610616839"
NEW_ZEALAND_BREAKERS = "15020"
RATIOPHARM_ULM = "15025"
CAIRNS_TAIPANS = "15022"
RAANANA_MACCABI = "50009"
FLAMENGO = "12325"
MADRID_BALONCESTO = "12315"
ADELAIDE_36ERS = "15019"
TEAM_USA = "1610616843"
SHANGHAI_SHARKS = "12329"
SESI_FRANCA_BASKETBALL_CLUB_OF_BRAZIL = "12332"
HAIFA_MACABI = "93"
BUENOS_AIRES_SAN_LORENZO = "12330"
GUANGZHOU_LONG_LIONS = "15018"
MELBOURNE_UNITED = "15016"
WORLD = "1610616844"
BEIJING_DUCKS = "15021"
PERTH_WILDCATS = "104"
SYDNEY_KINGS = "15015"
BRISBANE_BULLETS = "15017"
BARCELONA_LASSA = "12304"
ISTANBUL_FENERBAHCE_SPORTS_CLUB = "12321"
MILANO_OLIMPIA = "94"
BAURU_PASCHOALOTTO = "12328"
TEL_AVIV_MACCABI_ELECTRA = "41"
BERLIN_ALBA = "12323"
BILBAO_BASKET = "12324"
MOSCOW_CSKA = "12308"
SIENA_MONTEPASCI = "12322"
SOPHOMORES = "1610616838"
ROOKIES = "1610616837"
VITORIA_CAJAL_LABORAL = "95"
BELGRADE_PARTIZAN = "12319"
ATHENS_OLYMPIACOS = "12320"
HORNETS = "1610612778"
VILNIUS_LIETUVOS_RYTAS = "12314"
ISTANBUL_EFES_PILSEN = "12309"
LOTTOMATICA_ROMA = "12317"
UNICAJA_MALAGA = "12311"
MMT_ESTUDIANTES = "12318"
PANATHINAIKOS = "12313"
ZALGIRIS_KAUNAS = "12316"
TEAM_CHINA = "45"
CLUTCH_CITY = "1610612767"
H_TOWN = "1610612778"
LYON_VILLEURBANNE_ADECCO_ASVEL = "12305"
KHIMKI_BC = "12306"
TEL_AVIV_MACCABI_ELITE = "12303"
SEATTLE_SUPERSONICS = "137362"
BUFFALO_BRAVES = "139606"
ST_LOUIS_BOMBERS = "St. Louis Bombers"
PITTSBURGH_IRONMEN = "Pittsburgh Ironmen"
PROVIDENCE_STEAM_ROLLERS = "Providence Steam Rollers"
BALTIMORE_BULLETS = "Baltimore Bullets"
FORT_WAYNE_PISTONS = "Fort Wayne Pistons"
ROCHESTER_ROYALS = "Rochester Royals"
TRICITIES_BLACKHAWKS = "Tri-Cities Blackhawks"
SHEBOYGAN_REDSKINS = "Sheboygan Red Skins"
WATERLOO_HAWKS = "Waterloo Hawks"
SYRACUSE_NATIONALS = "Syracuse Nationals"
ANDERSON_PACKERS = "Anderson Packers"
CINCINATTI_ROYALS = "Cincinnati Royals"
SAN_FRANCISCO_WARRIORS = "San Francisco Warriors"
OAKLAND_OAKS = "Oakland Oaks"
ANAHEIM_AMIGOS = "Anaheim Amigos"
KENTUCKY_COLONELS = "Kentucky Colonels"
SAN_DIEGO_ROCKETS = "San Diego Rockets"
NEW_JERSEY_AMERICANS = "New Jersey Americans"
CAROLINA_COUGARS = "Carolina Cougars"
VIRGINIA_SQUIRES = "Virginia Squires"
KANSAS_CITY_KINGS = "Kansas City-Omaha Kings"
CAPITAL_BULLETS = "Capital Bullets"
VANCOUVER_GRIZZLIES = "Vancouver Grizzlies"
OGS = "1610616852"
GLOBAL_STARS = "1610616851"
RISING_STARS = "1610616854"
YOUNG_STARS = "1610616853"
TEAM_G_LEAGUE = "1610616858"
TEAM_C = "1610616855"
TEAM_M = "1610616857"
TEAM_T = "1610616856"
NBA_TEAM_IDENTITY_MAP = {
    # NBA API
    "1610612753": ORLANDO_MAGIC,
    "1610612737": ATLANTA_HAWKS,
    "1610612757": PORTLAND_TRAIL_BLAZERS,
    "1610612743": DENVER_NUGGETS,
    "1610612748": MIAMI_HEAT,
    "1610612747": LOS_ANGELES_LAKERS,
    "1610612738": BOSTON_CELTICS,
    "1610612760": OKLAHOMA_CITY_THUNDER,
    "1610612758": SACRAMENTO_KINGS,
    "1610612754": INDIANA_PACERS,
    "1610612759": SAN_ANTONIO_SPURS,
    "1610612756": PHOENIX_SUNS,
    "1610612764": WASHINGTON_WIZARDS,
    "1610612755": PHILADELPHIA_76ERS,
    "1610612761": TORONTO_RAPTORS,
    "1610612744": GOLDEN_STATE_WARRIORS,
    "1610612750": MINNESOTA_TIMBERWOLVES,
    "1610612745": HOUSTON_ROCKETS,
    "1610612763": MEMPHIS_GRIZZLIES,
    "1610612752": NEW_YORK_KNICKS,
    "1610612766": CHARLOTTE_HORNETS,
    "1610612751": BROOKLYN_NETS,
    "1610612742": DALLAS_MAVERICKS,
    "1610612739": CLEVELAND_CAVALIERS,
    "1610612749": MILWAUKEE_BUCKS,
    "1610612765": DETROIT_PISTONS,
    "1610612740": NEW_ORLEANS_PELICANS,
    "1610612741": CHICAGO_BULLS,
    "1610612746": LA_CLIPPERS,
    "1610612762": UTAH_JAZZ,
    "1610616842": UNKNOWN,
    "1610616841": UNKNOWN,
    "1610616849": TEAM_JALEN,
    "1610616850": TEAM_TAMIKA,
    "1610616847": TEAM_PAU,
    "1610616848": TEAM_DETLEF,
    "1610616840": TEAM_STEPHEN_A,
    "1610616833": EAST_NBA_ALL_STARS,
    "1610616834": WEST_NBA_ALL_STARS,
    "1610616839": TEAM_SHANNON,
    "1610616852": OGS,
    "1610616851": GLOBAL_STARS,
    "1610616854": RISING_STARS,
    "15020": NEW_ZEALAND_BREAKERS,
    "15025": RATIOPHARM_ULM,
    "15022": CAIRNS_TAIPANS,
    "50009": RAANANA_MACCABI,
    "12325": FLAMENGO,
    "12315": MADRID_BALONCESTO,
    "15019": ADELAIDE_36ERS,
    "1610616843": TEAM_USA,
    "12329": SHANGHAI_SHARKS,
    "12332": SESI_FRANCA_BASKETBALL_CLUB_OF_BRAZIL,
    "93": HAIFA_MACABI,
    "12330": BUENOS_AIRES_SAN_LORENZO,
    "15018": GUANGZHOU_LONG_LIONS,
    "15016": MELBOURNE_UNITED,
    "1610616844": WORLD,
    "15021": BEIJING_DUCKS,
    "104": PERTH_WILDCATS,
    "15015": SYDNEY_KINGS,
    "15017": BRISBANE_BULLETS,
    "12304": BARCELONA_LASSA,
    "12321": ISTANBUL_FENERBAHCE_SPORTS_CLUB,
    "94": MILANO_OLIMPIA,
    "12328": BAURU_PASCHOALOTTO,
    "41": TEL_AVIV_MACCABI_ELECTRA,
    "12323": BERLIN_ALBA,
    "12324": BILBAO_BASKET,
    "12308": MOSCOW_CSKA,
    "12322": SIENA_MONTEPASCI,
    "1610616838": SOPHOMORES,
    "1610616837": ROOKIES,
    "95": VITORIA_CAJAL_LABORAL,
    "12319": BELGRADE_PARTIZAN,
    "12320": ATHENS_OLYMPIACOS,
    "1610612778": HORNETS,
    "12314": VILNIUS_LIETUVOS_RYTAS,
    "12309": ISTANBUL_EFES_PILSEN,
    "12317": LOTTOMATICA_ROMA,
    "12311": UNICAJA_MALAGA,
    "12318": MMT_ESTUDIANTES,
    "12313": PANATHINAIKOS,
    "12316": ZALGIRIS_KAUNAS,
    "45": TEAM_CHINA,
    "1610612767": CLUTCH_CITY,
    "12305": LYON_VILLEURBANNE_ADECCO_ASVEL,
    "12306": KHIMKI_BC,
    "12303": TEL_AVIV_MACCABI_ELITE,
    "12307": LOTTOMATICA_ROMA,
    "1610616853": YOUNG_STARS,
    "1610616858": TEAM_G_LEAGUE,
    "1610616855": TEAM_C,
    "1610616857": TEAM_M,
    "1610616856": TEAM_T,
    # SportsDB
    "134867": LOS_ANGELES_LAKERS,
    "134872": DETROIT_PISTONS,
    "134865": GOLDEN_STATE_WARRIORS,
    "134863": PHILADELPHIA_76ERS,
    "134860": BOSTON_CELTICS,
    "134880": ATLANTA_HAWKS,
    "134869": SACRAMENTO_KINGS,
    "134862": NEW_YORK_KNICKS,
    "134884": WASHINGTON_WIZARDS,
    "134870": CHICAGO_BULLS,
    "137362": SEATTLE_SUPERSONICS,
    "134876": HOUSTON_ROCKETS,
    "134874": MILWAUKEE_BUCKS,
    "134868": PHOENIX_SUNS,
    "134871": CLEVELAND_CAVALIERS,
    "139606": BUFFALO_BRAVES,
    "134888": PORTLAND_TRAIL_BLAZERS,
    "134889": UTAH_JAZZ,
    "134885": DENVER_NUGGETS,
    "134879": SAN_ANTONIO_SPURS,
    "134873": INDIANA_PACERS,
    "134861": BROOKLYN_NETS,
    "134866": LA_CLIPPERS,
    "134875": DALLAS_MAVERICKS,
    "134881": CHARLOTTE_HORNETS,
    "134882": MIAMI_HEAT,
    "134886": MINNESOTA_TIMBERWOLVES,
    "134883": ORLANDO_MAGIC,
    "134887": OKLAHOMA_CITY_THUNDER,
    "134877": MEMPHIS_GRIZZLIES,
    "134864": TORONTO_RAPTORS,
    "134878": NEW_ORLEANS_PELICANS,
    "135398": NEW_ZEALAND_BREAKERS,
    # SportsReference
    "Los Angeles Lakers": LOS_ANGELES_LAKERS,
    "Milwaukee Bucks": MILWAUKEE_BUCKS,
    "Philadelphia 76ers": PHILADELPHIA_76ERS,
    "Houston Rockets": HOUSTON_ROCKETS,
    "Los Angeles Clippers": LA_CLIPPERS,
    "Dallas Mavericks": DALLAS_MAVERICKS,
    "Indiana Pacers": INDIANA_PACERS,
    "Washington Wizards": WASHINGTON_WIZARDS,
    "Boston Celtics": BOSTON_CELTICS,
    "Toronto Raptors": TORONTO_RAPTORS,
    "Charlotte Hornets": CHARLOTTE_HORNETS,
    "Orlando Magic": ORLANDO_MAGIC,
    "Miami Heat": MIAMI_HEAT,
    "Detroit Pistons": DETROIT_PISTONS,
    "Cleveland Cavaliers": CLEVELAND_CAVALIERS,
    "Brooklyn Nets": BROOKLYN_NETS,
    "Sacramento Kings": SACRAMENTO_KINGS,
    "Oklahoma City Thunder": OKLAHOMA_CITY_THUNDER,
    "Utah Jazz": UTAH_JAZZ,
    "New Orleans Pelicans": NEW_ORLEANS_PELICANS,
    "Minnesota Timberwolves": MINNESOTA_TIMBERWOLVES,
    "Portland Trail Blazers": PORTLAND_TRAIL_BLAZERS,
    "Chicago Bulls": CHICAGO_BULLS,
    "San Antonio Spurs": SAN_ANTONIO_SPURS,
    "Denver Nuggets": DENVER_NUGGETS,
    "New York Knicks": NEW_YORK_KNICKS,
    "Phoenix Suns": PHOENIX_SUNS,
    "Memphis Grizzlies": MEMPHIS_GRIZZLIES,
    "Golden State Warriors": GOLDEN_STATE_WARRIORS,
    "Atlanta Hawks": ATLANTA_HAWKS,
    "Toronto Huskies": TORONTO_RAPTORS,
    "St. Louis Bombers": ST_LOUIS_BOMBERS,
    "Pittsburgh Ironmen": PITTSBURGH_IRONMEN,
    "Providence Steam Rollers": PROVIDENCE_STEAM_ROLLERS,
    "Detroit Falcons": DETROIT_PISTONS,
    "Washington Capitols": WASHINGTON_WIZARDS,
    "Chicago Stags": CHICAGO_BULLS,
    "Cleveland Rebels": CLEVELAND_CAVALIERS,
    "Philadelphia Warriors": PHILADELPHIA_76ERS,
    "Baltimore Bullets": BALTIMORE_BULLETS,
    "Indianapolis Jets": INDIANA_PACERS,
    "Fort Wayne Pistons": FORT_WAYNE_PISTONS,
    "Minneapolis Lakers": MINNESOTA_TIMBERWOLVES,
    "Rochester Royals": ROCHESTER_ROYALS,
    "Tri-Cities Blackhawks": TRICITIES_BLACKHAWKS,
    "Sheboygan Red Skins": SHEBOYGAN_REDSKINS,
    "Indianapolis Olympians": INDIANA_PACERS,
    "Waterloo Hawks": WATERLOO_HAWKS,
    "Syracuse Nationals": SYRACUSE_NATIONALS,
    "Anderson Packers": ANDERSON_PACKERS,
    "Milwaukee Hawks": MILWAUKEE_BUCKS,
    "St. Louis Hawks": ST_LOUIS_BOMBERS,
    "Cincinnati Royals": CINCINATTI_ROYALS,
    "Chicago Packers": CHICAGO_BULLS,
    "Chicago Zephyrs": CHICAGO_BULLS,
    "San Francisco Warriors": SAN_FRANCISCO_WARRIORS,
    "Oakland Oaks": OAKLAND_OAKS,
    "Anaheim Amigos": ANAHEIM_AMIGOS,
    "Seattle SuperSonics": SEATTLE_SUPERSONICS,
    "Kentucky Colonels": KENTUCKY_COLONELS,
    "San Diego Rockets": SAN_DIEGO_ROCKETS,
    "Denver Rockets": DENVER_NUGGETS,
    "Dallas Chaparrals": DALLAS_MAVERICKS,
    "Houston Mavericks": HOUSTON_ROCKETS,
    "New Orleans Buccaneers": NEW_ORLEANS_PELICANS,
    "Minnesota Muskies": MINNESOTA_TIMBERWOLVES,
    "New Jersey Americans": NEW_JERSEY_AMERICANS,
    "Pittsburgh Pipers": PITTSBURGH_IRONMEN,
    "New York Nets": BROOKLYN_NETS,
    "Miami Floridians": MIAMI_HEAT,
    "Minnesota Pipers": MINNESOTA_TIMBERWOLVES,
    "Los Angeles Stars": LOS_ANGELES_LAKERS,
    "Carolina Cougars": CAROLINA_COUGARS,
    "Utah Stars": UTAH_JAZZ,
    "Buffalo Braves": BUFFALO_BRAVES,
    "Pittsburgh Condors": PITTSBURGH_IRONMEN,
    "The Floridians": MIAMI_HEAT,
    "Virginia Squires": VIRGINIA_SQUIRES,
    "Texas Chaparrals": DALLAS_MAVERICKS,
    "Memphis Pros": MEMPHIS_GRIZZLIES,
    "Kansas City-Omaha Kings": KANSAS_CITY_KINGS,
    "Memphis Tams": MEMPHIS_GRIZZLIES,
    "San Diego Conquistadors": SAN_DIEGO_ROCKETS,
    "Capital Bullets": CAPITAL_BULLETS,
    "New Orleans Jazz": NEW_ORLEANS_PELICANS,
    "Spirits of St. Louis": ST_LOUIS_BOMBERS,
    "Memphis Sounds": MEMPHIS_GRIZZLIES,
    "Washington Bullets": WASHINGTON_WIZARDS,
    "Kansas City Kings": KANSAS_CITY_KINGS,
    "San Diego Sails": SAN_DIEGO_ROCKETS,
    "New Jersey Nets": BROOKLYN_NETS,
    "San Diego Clippers": LA_CLIPPERS,
    "Vancouver Grizzlies": VANCOUVER_GRIZZLIES,
    "New Orleans Hornets": NEW_ORLEANS_PELICANS,
    "Charlotte Bobcats": CHARLOTTE_HORNETS,
    "New Orleans/Oklahoma City Hornets": NEW_ORLEANS_PELICANS,
}
WELLS_FARGO_CENTER = "Wells Fargo Center"
PAYCOM_CENTER = "Paycom Center"
TOYOTA_CENTER = "Toyota Center"
UNITED_CENTER = "United Center"
AMERICAN_AIRLINES_CENTER = "American Airlines Center"
KIA_CENTER = "Kia Center"
MADISON_SQUARE_GARDEN = "Madison Square Garden"
FISERV_FORUM = "Fiserv Forum"
BALL_ARENA = "Ball Arena"
GAINBRIDGE_FIELDHOUSE = "Gainbridge Fieldhouse"
LITTLE_CAESARS_ARENA = "Little Caesars Arena"
SPECTRUM_CENTER = "Spectrum Center"
KASEYA_CENTER = "Kaseya Center"
FEDEX_FORUM = "FedExForum"
TD_GARDEN = "TD Garden"
MODA_CENTER = "Moda Center"
CRYPTO_DOT_COM_ARENA = "Crypto.com Arena"
SCOTIABANK_ARENA = "Scotiabank Arena"
SMOOTHIE_KING_CENTER = "Smoothie King Center"
STATE_FARM_ARENA = "State Farm Arena"
ROCKET_MORTGAGE_FIELDHOUSE = "Rocket Mortgage FieldHouse"
DELTA_CENTER = "Delta Center"
BARCLAYS_CENTER = "Barclays Center"
GOLDEN_1_CENTER = "Golden 1 Center"
CAPITAL_ONE_ARENA = "Capital One Arena"
TARGET_CENTER = "Target Center"
FOOTPRINT_CENTER = "Footprint Center"
CHASE_CENTER = "Chase Center"
FROST_BANK_CENTER = "Frost Bank Center"
MOODY_CENTER = "Moody Center"
ARCO_ARENA = "ARCO Arena"
BMO_HARRIS_BRADLEY_CENTER = "BMO Harris Bradley Center"
ORACLE_ARENA = "Oracle Arena"
AMALIE_ARENA = "Amalie Arena"
ESPN_WIDE_WORLD_OF_SPORTS = "The Arena (WWOS)"
STATE_FARM_FIELDHOUSE = "State Farm Field House"
VISA_ATHLETIC_CENTER = "Visa Athletic Center"
ROBERT_F_KENNEDY_MEMORIAL_STADIUM = "Robert F. Kennedy Memorial Stadium"
ORIOLE_PARK = "Oriole Park at Camden Yards"
TOYOTA_STADIUM = "Toyota Stadium"
ANGEL_STADIUM = "Angel Stadium of Anaheim"
PANJIN_JINXIU_STADIUM = "Panjin Jinxiu Stadium"
THE_PALACE_OF_AUBURN_HILLS = "The Palace of Auburn Hills"
ADVENTHEALTH_ARENA = "AdventHealth Arena"
PAYPAL_PARK = "PayPal Park"
INTUIT_DOME = "Intuit Dome"
ACCOR_ARENA = "Accor Arena"
SIXTYNINTH_REGIMENT_ARMORY = "69th Regiment Armory, New York, New York"
ONONDAGA_WAR_MEMORIAL = "Onondaga War Memorial, Syracuse, New York"
KIEL_AUDITORIUM = "Kiel Auditorium, St. Louis, Missouri"
MIAMI_BEACH_AUDITORIUM = "Miami Beach Auditorium, Miami Beach, Florida"
DETROIT_OLYMPIA = "Detroit Olympia, Detroit, Michigan"
CONVENTION_HALL = "Convention Hall, Philadelphia, Pennsylvania"
BALTIMORE_CIVIC_CENTER = "Baltimore Civic Center, Baltimore, Maryland"
INDIANA_STATE_FAIR_COLISEUM = "Indiana State Fair Coliseum, Indianapolis, Indiana"
LOUISVILLE_CONVENTION_CENTER = "Louisville Convention Center, Louisville, Kentucky"
LOYOLA_FIELD_HOUSE = "Loyola Field House, New Orleans, Louisiana"
LONG_ISLAND_ARENA = "Long Island Arena, Commack, New York"
METROPOLITAN_SPORTS_CENTER = "Metropolitan Sports Center, Bloomington, Minnesota"
SAM_HOUSTON_COLISEUM = "Sam Houston Coliseum, Houston, Texas"
OAKLAND_ALAMEDA_COUNTY_COLISEUM_ARENA = (
    "Oakland-Alameda County Coliseum Arena, Oakland, California"
)
DULUTH_ARENA_AUDITORIUM = "Duluth Arena Auditorium, Duluth, Minnesota"
LOS_ANGELES_MEMORIAL_SPORTS_ARENA = (
    "Los Angeles Memorial Sports Arena, Los Angeles, California"
)
DENVER_AUDITORIUM_ARENA = "Denver Auditorium Arena, Denver, Colorado"
MIAMI_BEACH_CONVENTION_HALL = "Miami Beach Convention Hall, Miami Beach, Florida"
TARRANT_COUNTY_CONVENTION_CENTER = "Tarrant County Convention Center, Ft. Worth, Texas"
WEST_PALM_BEACH_AUDITORIUM = "West Palm Beach Auditorium, West Palm Beach, Florida"
BLACKHAM_COLISEUM = "Blackham Coliseum, Lafeyette, Louisiana"
ST_LOUIS_ARENA = "St. Louis Arena, St. Louis, Missouri"
MIAMI_DADE_JUNIOR_COLLEGE_NORTH = "Miami-Dade Junior College North, Miami, Florida"
SAN_JOSE_CIVIC_AUDITORIUM = "San Jose Civic Auditorium, San Jose, California"
ST_PAUL_AUDITORIUM = "St. Paul Auditorium, St. Paul, Minnesota"
ANDERSON_HIGHSCHOOL_WIGWAM = "Anderson High School Wigwam, Anderson, Indiana"
ISLAND_GARDEN = "Island Garden, West Hempstead, New York"
ULINE_ARENA = "Uline Arena, Washington, District of Columbia"
GREENSBORO_COLISEUM = "Greensboro Coliseum, Greensboro, North Carolina"
CHARLOTTE_COLISEUM = "Charlotte Coliseum, Charlotte, North Carolina"
DINNER_KEY_AUDITORIUM = "Dinner Key Auditorium, Miami, Florida"
JS_DORTON_ARENA = "J.S. Dorton Arena, Raleigh, North Carolina"
MIDSOUTH_COLISEUM = "Mid-South Coliseum, Memphis, Tennessee"
COMMUNITY_ARENA = "Community Arena, Steubenville, Ohio"
PITTSBURGH_CIVIC_ARENA = "Pittsburgh Civic Arena, Pittsburgh, Pennsylvania"
SELLAND_ARENA = "Selland Arena, Fresno, California"
LEVITT_ARENA = "Levitt Arena, Wichita, Kansas"
REID_GYMNASIUM = "Reid Gymnasium, Cullowhee, North Carolina"
JACKSONVILLE_COLISEUM = "Jacksonville Coliseum, Jacksonville, Florida"
ANAHEIM_CONVENTION_CENTER = "Anaheim Convention Center, Anaheim, California"
LONG_BEACH_ARENA = "Long Beach Arena, Long Beach, California"
SALT_PALACE = "Salt Palace, Salt Lake City, Utah"
NORFOLK_SCOPE = "Norfolk Scope, Norfolk, Virginia"
FREEDOM_HALL = "Freedom Hall, Louisville, Kentucky"
REYNOLDS_COLISEUM = "Reynolds Coliseum, Raleigh, North Carolina"
HAMPTON_COLISEUM = "Hampton Coliseum, Hampton, Virginia"
CURTIS_HIXON_HALL = "Curtis Hixon Hall, Tampa, Florida"
SIKESTON_FIELD_HOUSE = "Sikeston Field House, Sikeston, Missouri"
SWENSON_GYM = "Swenson Gym, Ogden, Utah"
MOBY_GYM = "Moby Gym, Ft. Collins, Colorado"
LUBBOCK_MUNICIPAL_COLISEUM = "Lubbock Municipal Coliseum, Lubbock, Texas"
RICHMOND_ARENA = "Richmond Arena, Richmond, Virginia"
UTAH_STATE_SPECTRUM = "Utah State Spectrum, Logan, Utah"
ROANOKE_CIVIC_CENTER = "Roanoke Civic Center, Roanoke, Virginia"
SALEM_CIVIC_CENTER = "Salem Civic Center, Salem, Virginia"
HOFSTRA_PHYSICAL_FITNESS_CENTER = "Hofstra Physical Fitness Center, Hempstead, New York"
BAYFRONT_ARENA = "Bayfront Arena, St. Petersburg, Florida"
WINSTON_SALEM_MEMORIAL_COLISEUM = (
    "Winston-Salem Memorial Coliseum, Winston-Salem, North Carolina"
)
RICHMOND_COLISEUM = "Richmond Coliseum, Richmond, Virginia"
MAPLE_LEAF_GARDENS = "Maple Leaf Gardens, Toronto, Canada"
UNIONTOWN_HIGHSCHOOL = "Uniontown High School, Uniontown, Pennsylvania"
NASSAU_VETERANS_MEMORIAL_COLISEUM = (
    "Nassau Veterans Memorial Coliseum, Uniondale, New York"
)
TUCSON_COMMUNITY_CENTER = "Tucson Community Center, Tucson, Arizona"
FAIR_PARK = "Fair Park, Birmingham, Alabama"
INDIANA_ASSEMBLY_HALL = "Indiana Assembly Hall, Bloomington, Indiana"
WAR_MEMORIAL_COLISEUM = "War Memorial Coliseum, Fort Wayne, Indiana"
PETERSON_GYM = "Peterson Gym, San Diego, California"
MABEE_CENTER = "Mabee Center, Tulsa, Oklahoma"
ST_PAUL_CIVIC_CENTER = "St. Paul Civic Center, St. Paul, Minnesota"
HEMISFAIR_ARENA = "HemisFair Arena, San Antonio, Texas"
GOLDEN_HALL = "Golden Hall, San Diego, California"
MEMORIAL_COLISEUM = "Memorial Coliseum, Lexington, Kentucky"
CINCINNATI_RIVER_COLISEUM = "Cincinnati Riverfront Coliseum, Cincinnati, Ohio"
EA_DIDDLE_ARENA = "E.A. Diddle Arena, Bowling Green, Kentucky"
HULMAN_CIVIC_UNIVERSITY_CENTER = "Hulman Civic-University Center, Terre Haute, Indiana"
MARKET_SQUARE_ARENA = "Market Square Arena, Indianapolis, Indiana"
SAN_DIEGO_SPORTS_ARENA = "San Diego Sports Arena, San Diego, California"
MCNICOLS_SPORTS_ARENA = "McNichols Sports Arena, Denver, Colorado"
GENERAL_MOTORS_PLACE = "General Motors Place, Vancouver, Canada"
KEYARENA = "KeyArena at Seattle Center, Seattle, Washington"
STAPLES_CENTER = "STAPLES Center, Los Angeles, California"
TD_WATERHOUSE_CENTER = "TD Waterhouse Centre, Orlando, Florida"
REUNION_ARENA = "Reunion Arena, Dallas, Texas"
COMPAQ_CENTER = "Compaq Center, Houston, Texas"
ALAMODOME = "Alamodome, San Antonio, Texas"
CONTINENTAL_AIRLINES_ARENA = "Continental Airlines Arena, East Rutherford, New Jersey"
FLEETCENTER = "FleetCenter, Boston, Massachusetts"
ROSE_GARDEN_ARENA = "Rose Garden Arena, Portland, Oregon"
PEPSI_CENTER = "Pepsi Center, Denver, Colorado"
THE_ARENA = "The Arena in Oakland, Oakland, California"
AMERICA_WEST_ARENA = "America West Arena, Phoenix, Arizona"
FIRST_UNION_CENTER = "First Union Center, Philadelphia, Pennsylvania"
AIR_CANADA_CENTER = "Air Canada Centre, Toronto, Canada"
PHILIPS_ARENA = "Philips Arena, Atlanta, Georgia"
MCI_CENTER = "MCI Center, Washington, District of Columbia"
BRADLEY_CENTER = "Bradley Center, Milwaukee, Wisconsin"
GUND_ARENA = "Gund Arena, Cleveland, Ohio"
CONSECO_FIELDHOUSE = "Conseco Fieldhouse, Indianapolis, Indiana"
PYRAMID_ARENA = "Pyramid Arena, Memphis, Tennessee"
AMERICAN_AIRLINES_ARENA = "AmericanAirlines Arena, Miami, Florida"
NEW_ORLEANS_ARENA = "New Orleans Arena, New Orleans, Louisiana"
SBC_CENTER = "SBC Center, San Antonio, Texas"
WACHOVIA_CENTER = "Wachovia Center, Philadelphia, Pennsylvania"
FORD_CENTER = "Ford Center, Oklahoma City, Oklahoma"
CHARLOTTE_BOBCATS_ARENA = "Charlotte Bobcats Arena, Charlotte, North Carolina"
AMWAY_ARENA = "Amway Arena, Orlando, Florida"
ENERGYSOLUTIONS_ARENA = "EnergySolutions Arena, Salt Lake City, Utah"
QUICKEN_LOANS_ARENA = "Quicken Loans Arena, Cleveland, Ohio"
US_AIRWAYS_CENTER = "US Airways Center, Phoenix, Arizona"
VERIZON_CENTER = "Verizon Center, Washington, District of Columbia"
ATT_CENTER = "AT&T Center, San Antonio, Texas"
IZOD_CENTER = "Izod Center, East Rutherford, New Jersey"
CHESAPEAKE_ENERGY_ARENA = "Chesapeake Energy Arena, Oklahoma City, Oklahoma"
SLEEP_TRAIN_ARENA = "Sleep Train Arena, Sacramento, California"
BANKERS_LIFE_FIELDHOUSE = "Bankers Life Fieldhouse, Indianapolis, Indiana"
TIME_WARNER_CABLE_ARENA = "Time Warner Cable Arena, Charlotte, North Carolina"
VIVINT_SMART_HOME_ARENA = "Vivint Smart Home Arena, Salt Lake City, Utah"
O2_ARENA = "The O2 Arena, London, United Kingdom"
TALKING_STICK_RESORT_ARENA = "Talking Stick Resort Arena, Phoenix, Arizona"
MEXICO_CITY_ARENA = "Mexico City Arena, Mexico City, Mexico"
UW_MILWAUKEE_PANTHER_ARENA = "UW–Milwaukee Panther Arena, Milwaukee, Wisconsin"
HP_FIELD_HOUSE = "HP Field House, Bay Lake, Florida"
PHOENIX_SUNS_ARENA = "Phoenix Suns Arena, Phoenix, Arizona"
FTX_ARENA = "FTX Arena, Miami, Florida"
T_MOBILE_ARENA = "T-Mobile Arena, Las Vegas, Nevada"
ROCKET_ARENA = "Rocket Arena, Cleveland, Ohio"
BOK_CENTER = "24787"
CLIMATE_PLEDGE_ARENA = "27140"
STAN_SHERIFF_CENTER = "29758"
GREAT_WESTERN_FORUM = "26965"
MIAMI_ARENA = "28215"
CHICAGO_STADIUM = "26964"
YOKOHAMA_ARENA = "16381"
OMNI_COLISEUM = "28151"
ORLANDO_ARENA = "28218"
THE_FORUM = "20173"
THOMAS_AND_MACK_CENTER = "24731"
PONTIAC_SILVERDOME = "18379"
KEMPER_ARENA = "24670"
TACOMA_DOME = "20117"
JOE_LOUIS_ARENA = "24619"
MUNICIPAL_AUDITORIUM = "21237"
LOUISIANA_SUPERDOME = "28181"
COW_PALACE = "24673"
INTERNATIONAL_AMPITHEATRE = "19769"
TOKYO_METROPOLITAN_GYMNASIUM = "28141"
LLOYD_NOBLE_CENTER = "LLoyd Noble Center, Norman, Oklahoma"
PETE_MARAVICH_ASSEMBLY_CENTER = "Pete Maravich Assembly Center, Baton Rouge, Louisiana"
POWER_BALANCE_PAVILION = "Power Balance Pavilion, Sacramento, California"
PRUDENTIAL_CENTER = "Prudential Center, Newark, New Jersey"
THE_CENTER = "The Center, Philadelphia, Pennsylvania"
ETIHAD_ARENA = "20454"
SAITAMA_SUPER_ARENA = "17494"
ROGERS_PLACE = "27210"
BELL_CENTER = "23587"
NBA_VENUE_IDENTITY_MAP: dict[str, str] = {
    # SportsReference
    "Wells Fargo Center": WELLS_FARGO_CENTER,
    "Paycom Center": PAYCOM_CENTER,
    "Toyota Center": TOYOTA_CENTER,
    "United Center": UNITED_CENTER,
    "American Airlines Center": AMERICAN_AIRLINES_CENTER,
    "Kia Center": KIA_CENTER,
    "Madison Square Garden": MADISON_SQUARE_GARDEN,
    "Fiserv Forum": FISERV_FORUM,
    "Ball Arena": BALL_ARENA,
    "Gainbridge Fieldhouse": GAINBRIDGE_FIELDHOUSE,
    "Little Caesars Arena": LITTLE_CAESARS_ARENA,
    "Spectrum Center": SPECTRUM_CENTER,
    "Kaseya Center": KASEYA_CENTER,
    "FedExForum": FEDEX_FORUM,
    "TD Garden": TD_GARDEN,
    "Moda Center": MODA_CENTER,
    "Crypto.com Arena": CRYPTO_DOT_COM_ARENA,
    "Scotiabank Arena": SCOTIABANK_ARENA,
    "Smoothie King Center": SMOOTHIE_KING_CENTER,
    "State Farm Arena": STATE_FARM_ARENA,
    "Rocket Mortgage FieldHouse": ROCKET_MORTGAGE_FIELDHOUSE,
    "Delta Center": DELTA_CENTER,
    "Barclays Center": BARCLAYS_CENTER,
    "Golden 1 Center": GOLDEN_1_CENTER,
    "Capital One Arena": CAPITAL_ONE_ARENA,
    "Target Center": TARGET_CENTER,
    "Footprint Center": FOOTPRINT_CENTER,
    "Chase Center": CHASE_CENTER,
    "Frost Bank Center": FROST_BANK_CENTER,
    "Moody Center": MOODY_CENTER,
    "ARCO Arena": ARCO_ARENA,
    "BMO Harris Bradley Center": BMO_HARRIS_BRADLEY_CENTER,
    "Oracle Arena": ORACLE_ARENA,
    "Amalie Arena": AMALIE_ARENA,
    "The Arena (WWOS)": ESPN_WIDE_WORLD_OF_SPORTS,
    "State Farm Field House": STATE_FARM_FIELDHOUSE,
    "Visa Athletic Center": VISA_ATHLETIC_CENTER,
    "ESPN Wide World of Sports Complex": ESPN_WIDE_WORLD_OF_SPORTS,
    "Robert F. Kennedy Memorial Stadium": ROBERT_F_KENNEDY_MEMORIAL_STADIUM,
    "Oriole Park at Camden Yards": ORIOLE_PARK,
    "Toyota Stadium": TOYOTA_STADIUM,
    "Angel Stadium of Anaheim": ANGEL_STADIUM,
    "Panjin Jinxiu Stadium": PANJIN_JINXIU_STADIUM,
    "The Palace of Auburn Hills": THE_PALACE_OF_AUBURN_HILLS,
    "AdventHealth Arena": ADVENTHEALTH_ARENA,
    "PayPal Park": PAYPAL_PARK,
    "Intuit Dome": INTUIT_DOME,
    "Accor Arena": ACCOR_ARENA,
    "Madison Square Garden (III), New York, New York": MADISON_SQUARE_GARDEN,
    "Boston Garden, Boston, Massachusetts": TD_GARDEN,
    "69th Regiment Armory, New York, New York": SIXTYNINTH_REGIMENT_ARMORY,
    "Onondaga War Memorial, Syracuse, New York": ONONDAGA_WAR_MEMORIAL,
    "Kiel Auditorium, St. Louis, Missouri": KIEL_AUDITORIUM,
    "Miami Beach Auditorium, Miami Beach, Florida": MIAMI_BEACH_AUDITORIUM,
    "Detroit Olympia, Detroit, Michigan": DETROIT_OLYMPIA,
    "Convention Hall, Philadelphia, Pennsylvania": CONVENTION_HALL,
    "Baltimore Civic Center, Baltimore, Maryland": BALTIMORE_CIVIC_CENTER,
    "Indiana State Fair Coliseum, Indianapolis, Indiana": INDIANA_STATE_FAIR_COLISEUM,
    "Louisville Convention Center, Louisville, Kentucky": LOUISVILLE_CONVENTION_CENTER,
    "Loyola Field House, New Orleans, Louisiana": LOYOLA_FIELD_HOUSE,
    "Long Island Arena, Commack, New York": LONG_ISLAND_ARENA,
    "Metropolitan Sports Center, Bloomington, Minnesota": METROPOLITAN_SPORTS_CENTER,
    "Sam Houston Coliseum, Houston, Texas": SAM_HOUSTON_COLISEUM,
    "Oakland-Alameda County Coliseum Arena, Oakland, California": OAKLAND_ALAMEDA_COUNTY_COLISEUM_ARENA,
    "Duluth Arena Auditorium, Duluth, Minnesota": DULUTH_ARENA_AUDITORIUM,
    "Los Angeles Memorial Sports Arena, Los Angeles, California": LOS_ANGELES_MEMORIAL_SPORTS_ARENA,
    "Denver Auditorium Arena, Denver, Colorado": DENVER_AUDITORIUM_ARENA,
    "Miami Beach Convention Hall, Miami Beach, Florida": MIAMI_BEACH_CONVENTION_HALL,
    "Tarrant County Convention Center, Ft. Worth, Texas": TARRANT_COUNTY_CONVENTION_CENTER,
    "West Palm Beach Auditorium, West Palm Beach, Florida": WEST_PALM_BEACH_AUDITORIUM,
    "Blackham Coliseum, Lafeyette, Louisiana": BLACKHAM_COLISEUM,
    "St. Louis Arena, St. Louis, Missouri": ST_LOUIS_ARENA,
    "Miami-Dade Junior College North, Miami, Florida": MIAMI_DADE_JUNIOR_COLLEGE_NORTH,
    "San Jose Civic Auditorium, San Jose, California": SAN_JOSE_CIVIC_AUDITORIUM,
    "St. Paul Auditorium, St. Paul, Minnesota": ST_PAUL_AUDITORIUM,
    "Anderson High School Wigwam, Anderson, Indiana": ANDERSON_HIGHSCHOOL_WIGWAM,
    "Island Garden, West Hempstead, New York": ISLAND_GARDEN,
    "Uline Arena, Washington, District of Columbia": ULINE_ARENA,
    "Greensboro Coliseum, Greensboro, North Carolina": GREENSBORO_COLISEUM,
    "Charlotte Coliseum, Charlotte, North Carolina": CHARLOTTE_COLISEUM,
    "Dinner Key Auditorium, Miami, Florida": DINNER_KEY_AUDITORIUM,
    "J.S. Dorton Arena, Raleigh, North Carolina": JS_DORTON_ARENA,
    "Mid-South Coliseum, Memphis, Tennessee": MIDSOUTH_COLISEUM,
    "Community Arena, Steubenville, Ohio": COMMUNITY_ARENA,
    "Pittsburgh Civic Arena, Pittsburgh, Pennsylvania": PITTSBURGH_CIVIC_ARENA,
    "Selland Arena, Fresno, California": SELLAND_ARENA,
    "Levitt Arena, Wichita, Kansas": LEVITT_ARENA,
    "Reid Gymnasium, Cullowhee, North Carolina": REID_GYMNASIUM,
    "Jacksonville Coliseum, Jacksonville, Florida": JACKSONVILLE_COLISEUM,
    "Anaheim Convention Center, Anaheim, California": ANAHEIM_CONVENTION_CENTER,
    "Long Beach Arena, Long Beach, California": LONG_BEACH_ARENA,
    "Salt Palace, Salt Lake City, Utah": SALT_PALACE,
    "Norfolk Scope, Norfolk, Virginia": NORFOLK_SCOPE,
    "Freedom Hall, Louisville, Kentucky": FREEDOM_HALL,
    "Reynolds Coliseum, Raleigh, North Carolina": REYNOLDS_COLISEUM,
    "Hampton Coliseum, Hampton, Virginia": HAMPTON_COLISEUM,
    "Curtis Hixon Hall, Tampa, Florida": CURTIS_HIXON_HALL,
    "Sikeston Field House, Sikeston, Missouri": SIKESTON_FIELD_HOUSE,
    "Swenson Gym, Ogden, Utah": SWENSON_GYM,
    "Moby Gym, Ft. Collins, Colorado": MOBY_GYM,
    "Lubbock Municipal Coliseum, Lubbock, Texas": LUBBOCK_MUNICIPAL_COLISEUM,
    "Richmond Arena, Richmond, Virginia": RICHMOND_ARENA,
    "Madison Square Garden (IV), New York, New York": MADISON_SQUARE_GARDEN,
    "Utah State Spectrum, Logan, Utah": UTAH_STATE_SPECTRUM,
    "Roanoke Civic Center, Roanoke, Virginia": ROANOKE_CIVIC_CENTER,
    "Salem Civic Center, Salem, Virginia": SALEM_CIVIC_CENTER,
    "Hofstra Physical Fitness Center, Hempstead, New York": HOFSTRA_PHYSICAL_FITNESS_CENTER,
    "Bayfront Arena, St. Petersburg, Florida": BAYFRONT_ARENA,
    "Winston-Salem Memorial Coliseum, Winston-Salem, North Carolina": WINSTON_SALEM_MEMORIAL_COLISEUM,
    "Richmond Coliseum, Richmond, Virginia": RICHMOND_COLISEUM,
    "Maple Leaf Gardens, Toronto, Canada": MAPLE_LEAF_GARDENS,
    "Uniontown High School, Uniontown, Pennsylvania": UNIONTOWN_HIGHSCHOOL,
    "Nassau Veterans Memorial Coliseum, Uniondale, New York": NASSAU_VETERANS_MEMORIAL_COLISEUM,
    "Tucson Community Center, Tucson, Arizona": TUCSON_COMMUNITY_CENTER,
    "Fair Park, Birmingham, Alabama": FAIR_PARK,
    "Indiana Assembly Hall, Bloomington, Indiana": INDIANA_ASSEMBLY_HALL,
    "War Memorial Coliseum, Fort Wayne, Indiana": WAR_MEMORIAL_COLISEUM,
    "Peterson Gym, San Diego, California": PETERSON_GYM,
    "Mabee Center, Tulsa, Oklahoma": MABEE_CENTER,
    "St. Paul Civic Center, St. Paul, Minnesota": ST_PAUL_CIVIC_CENTER,
    "HemisFair Arena, San Antonio, Texas": HEMISFAIR_ARENA,
    "Golden Hall, San Diego, California": GOLDEN_HALL,
    "Memorial Coliseum, Lexington, Kentucky": MEMORIAL_COLISEUM,
    "Cincinnati Riverfront Coliseum, Cincinnati, Ohio": CINCINNATI_RIVER_COLISEUM,
    "E.A. Diddle Arena, Bowling Green, Kentucky": EA_DIDDLE_ARENA,
    "Hulman Civic-University Center, Terre Haute, Indiana": HULMAN_CIVIC_UNIVERSITY_CENTER,
    "Market Square Arena, Indianapolis, Indiana": MARKET_SQUARE_ARENA,
    "San Diego Sports Arena, San Diego, California": SAN_DIEGO_SPORTS_ARENA,
    "McNichols Sports Arena, Denver, Colorado": MCNICOLS_SPORTS_ARENA,
    "General Motors Place, Vancouver, Canada": GENERAL_MOTORS_PLACE,
    "KeyArena at Seattle Center, Seattle, Washington": KEYARENA,
    "STAPLES Center, Los Angeles, California": STAPLES_CENTER,
    "TD Waterhouse Centre, Orlando, Florida": TD_WATERHOUSE_CENTER,
    "AmericanAirlines Arena, Miami, Florida": AMERICAN_AIRLINES_ARENA,
    "Reunion Arena, Dallas, Texas": REUNION_ARENA,
    "Compaq Center, Houston, Texas": COMPAQ_CENTER,
    "Alamodome, San Antonio, Texas": ALAMODOME,
    "Continental Airlines Arena, East Rutherford, New Jersey": CONTINENTAL_AIRLINES_ARENA,
    "The Palace of Auburn Hills, Auburn Hills, Michigan": THE_PALACE_OF_AUBURN_HILLS,
    "Target Center, Minneapolis, Minnesota": TARGET_CENTER,
    "ARCO Arena (II), Sacramento, California": ARCO_ARENA,
    "FleetCenter, Boston, Massachusetts": FLEETCENTER,
    "Rose Garden Arena, Portland, Oregon": ROSE_GARDEN_ARENA,
    "Pepsi Center, Denver, Colorado": PEPSI_CENTER,
    "Delta Center, Salt Lake City, Utah": DELTA_CENTER,
    "The Arena in Oakland, Oakland, California": THE_ARENA,
    "America West Arena, Phoenix, Arizona": AMERICA_WEST_ARENA,
    "First Union Center, Philadelphia, Pennsylvania": FIRST_UNION_CENTER,
    "Air Canada Centre, Toronto, Canada": AIR_CANADA_CENTER,
    "Philips Arena, Atlanta, Georgia": PHILIPS_ARENA,
    "MCI Center, Washington, District of Columbia": MCI_CENTER,
    "Bradley Center, Milwaukee, Wisconsin": BRADLEY_CENTER,
    "United Center, Chicago, Illinois": UNITED_CENTER,
    "Gund Arena, Cleveland, Ohio": GUND_ARENA,
    "Conseco Fieldhouse, Indianapolis, Indiana": CONSECO_FIELDHOUSE,
    "Pyramid Arena, Memphis, Tennessee": PYRAMID_ARENA,
    "American Airlines Center, Dallas, Texas": AMERICAN_AIRLINES_CENTER,
    "New Orleans Arena, New Orleans, Louisiana": NEW_ORLEANS_ARENA,
    "SBC Center, San Antonio, Texas": SBC_CENTER,
    "Toyota Center, Houston, Texas": TOYOTA_CENTER,
    "Wachovia Center, Philadelphia, Pennsylvania": WACHOVIA_CENTER,
    "FedEx Forum, Memphis, Tennessee": FEDEX_FORUM,
    "Oakland Arena, Oakland, California": OAKLAND_ALAMEDA_COUNTY_COLISEUM_ARENA,
    "Ford Center, Oklahoma City, Oklahoma": FORD_CENTER,
    "TD Banknorth Garden, Boston, Massachusetts": TD_GARDEN,
    "Charlotte Bobcats Arena, Charlotte, North Carolina": CHARLOTTE_BOBCATS_ARENA,
    "Amway Arena, Orlando, Florida": AMWAY_ARENA,
    "Oracle Arena, Oakland, California": ORACLE_ARENA,
    "EnergySolutions Arena, Salt Lake City, Utah": ENERGYSOLUTIONS_ARENA,
    "Quicken Loans Arena, Cleveland, Ohio": QUICKEN_LOANS_ARENA,
    "US Airways Center, Phoenix, Arizona": US_AIRWAYS_CENTER,
    "Verizon Center, Washington, District of Columbia": VERIZON_CENTER,
    "AT&T Center, San Antonio, Texas": ATT_CENTER,
    "Izod Center, East Rutherford, New Jersey": IZOD_CENTER,
    "Chesapeake Energy Arena, Oklahoma City, Oklahoma": CHESAPEAKE_ENERGY_ARENA,
    "Barclays Center, Brooklyn, New York": BARCLAYS_CENTER,
    "Sleep Train Arena, Sacramento, California": SLEEP_TRAIN_ARENA,
    "Bankers Life Fieldhouse, Indianapolis, Indiana": BANKERS_LIFE_FIELDHOUSE,
    "Time Warner Cable Arena, Charlotte, North Carolina": TIME_WARNER_CABLE_ARENA,
    "TD Garden, Boston, Massachusetts": TD_GARDEN,
    "Wells Fargo Center, Philadelphia, Pennsylvania": WELLS_FARGO_CENTER,
    "BMO Harris Bradley Center, Milwaukee, Wisconsin": BMO_HARRIS_BRADLEY_CENTER,
    "Amway Center, Orlando, Florida": AMWAY_ARENA,
    "Moda Center, Portland, Oregon": MODA_CENTER,
    "Smoothie King Center, New Orleans, Louisiana": SMOOTHIE_KING_CENTER,
    "Vivint Smart Home Arena, Salt Lake City, Utah": VIVINT_SMART_HOME_ARENA,
    "The O2 Arena, London, United Kingdom": O2_ARENA,
    "Talking Stick Resort Arena, Phoenix, Arizona": TALKING_STICK_RESORT_ARENA,
    "Mexico City Arena, Mexico City, Mexico": MEXICO_CITY_ARENA,
    "Golden 1 Center, Sacramento, California": GOLDEN_1_CENTER,
    "Spectrum Center, Charlotte, North Carolina": SPECTRUM_CENTER,
    "Capital One Arena, Washington, District of Columbia": CAPITAL_ONE_ARENA,
    "Little Caesars Arena, Detroit, Michigan": LITTLE_CAESARS_ARENA,
    "UW–Milwaukee Panther Arena, Milwaukee, Wisconsin": UW_MILWAUKEE_PANTHER_ARENA,
    "Scotiabank Arena, Toronto, Canada": SCOTIABANK_ARENA,
    "Fiserv Forum, Milwaukee, Wisconsin": FISERV_FORUM,
    "State Farm Arena, Atlanta, Georgia": STATE_FARM_ARENA,
    "Chase Center, San Francisco, California": CHASE_CENTER,
    "AccorHotels Arena, Paris, France": ACCOR_ARENA,
    "Rocket Mortgage Fieldhouse, Cleveland, Ohio": ROCKET_MORTGAGE_FIELDHOUSE,
    "HP Field House, Bay Lake, Florida": HP_FIELD_HOUSE,
    "The Arena, Bay Lake, Florida": THE_ARENA,
    "Visa Athletic Center, Bay Lake, Florida": VISA_ATHLETIC_CENTER,
    "Amalie Arena, Tampa, Florida": AMALIE_ARENA,
    "Phoenix Suns Arena, Phoenix, Arizona": PHOENIX_SUNS_ARENA,
    "Ball Arena, Denver, Colorado": BALL_ARENA,
    "Crypto.com Arena, Los Angeles, California": CRYPTO_DOT_COM_ARENA,
    "FTX Arena, Miami, Florida": FTX_ARENA,
    "Gainbridge Fieldhouse, Indianapolis, Indiana": GAINBRIDGE_FIELDHOUSE,
    "Paycom Center, Oklahoma City, Oklahoma": PAYCOM_CENTER,
    "Vivint Arena, Salt Lake City, Utah": VIVINT_SMART_HOME_ARENA,
    "Footprint Center, Phoenix, Arizona": FOOTPRINT_CENTER,
    "Kaseya Center, Miami, Florida": KASEYA_CENTER,
    "Frost Bank Center, San Antonio, Texas": FROST_BANK_CENTER,
    "Kia Center, Orlando, Florida": KIA_CENTER,
    "T-Mobile Arena, Las Vegas, Nevada": T_MOBILE_ARENA,
    "Moody Center, Austin, Texas": MOODY_CENTER,
    "Intuit Dome, Inglewood, California": INTUIT_DOME,
    "Rocket Arena, Cleveland, Ohio": ROCKET_ARENA,
    "LLoyd Noble Center, Norman, Oklahoma": LLOYD_NOBLE_CENTER,
    "Pete Maravich Assembly Center, Baton Rouge, Louisiana": PETE_MARAVICH_ASSEMBLY_CENTER,
    "Oklahoma City Arena, Oklahoma City, Oklahoma": OAKLAND_ALAMEDA_COUNTY_COLISEUM_ARENA,
    "Power Balance Pavilion, Sacramento, California": POWER_BALANCE_PAVILION,
    "Prudential Center, Newark, New Jersey": PRUDENTIAL_CENTER,
    "The Center, Philadelphia, Pennsylvania": THE_CENTER,
    # SportsDB
    "25994": CRYPTO_DOT_COM_ARENA,
    "29509": DELTA_CENTER,
    "24837": FISERV_FORUM,
    "19870": TOYOTA_CENTER,
    "24836": GOLDEN_1_CENTER,
    "24848": BALL_ARENA,
    "24818": MODA_CENTER,
    "30970": INTUIT_DOME,
    "24819": SMOOTHIE_KING_CENTER,
    "24787": BOK_CENTER,
    "24852": PAYCOM_CENTER,
    "29950": FROST_BANK_CENTER,
    "19860": AMERICAN_AIRLINES_CENTER,
    "24835": LITTLE_CAESARS_ARENA,
    "19333": WELLS_FARGO_CENTER,
    "24830": SCOTIABANK_ARENA,
    "24786": TD_GARDEN,
    "23207": TARGET_CENTER,
    "24847": GAINBRIDGE_FIELDHOUSE,
    "16006": MADISON_SQUARE_GARDEN,
    "22906": ROCKET_MORTGAGE_FIELDHOUSE,
    "23213": FOOTPRINT_CENTER,
    "27140": CLIMATE_PLEDGE_ARENA,
    "29758": STAN_SHERIFF_CENTER,
    "28400": GENERAL_MOTORS_PLACE,
    "17606": ESPN_WIDE_WORLD_OF_SPORTS,
    "24699": AMERICAN_AIRLINES_CENTER,
    "24766": AMWAY_ARENA,
    "19838": STAPLES_CENTER,
    "24762": BALL_ARENA,
    "15830": QUICKEN_LOANS_ARENA,
    "24743": TD_GARDEN,
    "24724": PHILIPS_ARENA,
    "24704": WACHOVIA_CENTER,
    "22727": UNITED_CENTER,
    "19852": ROSE_GARDEN_ARENA,
    "16149": ATT_CENTER,
    "26965": GREAT_WESTERN_FORUM,
    "24614": REUNION_ARENA,
    "15554": MCNICOLS_SPORTS_ARENA,
    "28215": MIAMI_ARENA,
    "24640": AMERICA_WEST_ARENA,
    "24644": MARKET_SQUARE_ARENA,
    "24617": BRADLEY_CENTER,
    "26964": CHICAGO_STADIUM,
    "16381": YOKOHAMA_ARENA,
    "24656": CHARLOTTE_COLISEUM,
    "24620": ARCO_ARENA,
    "28151": OMNI_COLISEUM,
    "28198": SPECTRUM_CENTER,
    "30267": TD_GARDEN,
    "26966": THE_PALACE_OF_AUBURN_HILLS,
    "28218": ORLANDO_ARENA,
    "30268": LOS_ANGELES_MEMORIAL_SPORTS_ARENA,
    "25255": MEMORIAL_COLISEUM,
    "20173": THE_FORUM,
    "24731": THOMAS_AND_MACK_CENTER,
    "18379": PONTIAC_SILVERDOME,
    "24670": KEMPER_ARENA,
    "20117": TACOMA_DOME,
    "24619": JOE_LOUIS_ARENA,
    "24625": SAN_DIEGO_SPORTS_ARENA,
    "28217": UW_MILWAUKEE_PANTHER_ARENA,
    "21237": MUNICIPAL_AUDITORIUM,
    "28181": LOUISIANA_SUPERDOME,
    "24673": COW_PALACE,
    "30266": SPECTRUM_CENTER,
    "19769": INTERNATIONAL_AMPITHEATRE,
    "20105": SAN_JOSE_CIVIC_AUDITORIUM,
    "28141": TOKYO_METROPOLITAN_GYMNASIUM,
    "25267": ANAHEIM_CONVENTION_CENTER,
    "24759": NEW_ORLEANS_ARENA,
    "19862": CHESAPEAKE_ENERGY_ARENA,
    "24851": FTX_ARENA,
    "24761": OAKLAND_ALAMEDA_COUNTY_COLISEUM_ARENA,
    "20454": ETIHAD_ARENA,
    "17494": SAITAMA_SUPER_ARENA,
    "27210": ROGERS_PLACE,
    "23587": BELL_CENTER,
    "21308": STATE_FARM_ARENA,
    "18422": KIA_CENTER,
    "19331": CAPITAL_ONE_ARENA,
    "24838": SPECTRUM_CENTER,
    "28619": KASEYA_CENTER,
    "24727": FEDEX_FORUM,
    "24828": CHASE_CENTER,
    # NBACom
    "Paycom Center, Oklahoma City, OK": PAYCOM_CENTER,
    "Madison Square Garden, New York, NY": MADISON_SQUARE_GARDEN,
    "Target Center, Minneapolis, MN": TARGET_CENTER,
}
NBA_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class NBACombinedLeagueModel(CombinedLeagueModel):
    """NBA combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.NBA,
            [
                NBANBALeagueModel(session, position=0),
                NBAESPNLeagueModel(session, position=1),
                NBAOddsPortalLeagueModel(session, position=2),
                NBANBAComLeagueModel(session, position=3),
                # NBASportsDBLeagueModel(session, position=4),
                # NBASportsReferenceLeagueModel(session, position=5),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return NBA_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return NBA_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return NBA_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "nba-combined-league-model"
