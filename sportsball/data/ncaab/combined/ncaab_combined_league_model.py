"""NCAAB combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.ncaab_espn_league_model import NCAABESPNLeagueModel
from ..oddsportal.ncaab_oddsportal_league_model import \
    NCAABOddsPortalLeagueModel

DEPAUL_BLUE_DEMONS = "DePaul Blue Demons Men's"
GEORGETOWN_HOYAS = "Georgetown Hoyas Men's"
CAL_STATE_NORTHRIDGE_MATADORS = "Cal State Northridge Matadors Men's"
HAWAII_RAINBOW_WARRIORS = "Hawaii Rainbow Warriors Men's"
INDIANA_HOOSIERS = "Indiana Hoosiers Men's"
OHIO_STATE_BUCKEYES = "Ohio State Buckeyes Men's"
OHIO_BOBCATS = "Ohio Bobcats Men's"
AKRON_ZIPS = "Akron Zips Men's"
ROBERT_MORRIS_COLONIALS = "Robert Morris Colonials Men's"
GREEN_BAY_PHOENIX = "Green Bay Phoenix Men's"
VCU_RAMS = "VCU Rams Men's"
ST_JOSEPHS_HAWKS = "St. Joseph's Hawks Men's"
PROVIDENCE_FRIARS = "Providence Friars Men's"
VILLANOVA_WILDCATS = "Villanova Wildcats Men's"
YOUNGSTOWN_STATE_PENGUINS = "Youngstown State Penguins Men's"
MILWAUKEE_PANTHERS = "Milwaukee Panthers Men's"
IOWA_HAWKEYES = "Iowa Hawkeyes Men's"
UCLA_BRUINS = "UCLA Bruins Men's"
AIR_FORCE_FALCONS = "Air Force Falcons Men's"
FRESNO_STATE_BULLDOGS = "Fresno State Bulldogs Men's"
BOISE_STATE_BRONCOS = "Boise State Broncos Men's"
NEW_MEXICO_LOBOS = "New Mexico Lobos Men's"
GONZAGA_BULLDOGS = "Gonzaga Bulldogs Men's"
OREGON_STATE_BEAVERS = "Oregon State Beavers Men's"
MEMPHIS_TIGERS = "Memphis Tigers Men's"
TEMPLE_OWLS = "Temple Owls Men's"
MICHIGAN_WOLVERINES = "Michigan Wolverines Men's"
MINNESOTA_GOLDEN_GOPHERS = "Minnesota Golden Gophers Men's"
COLLEGE_CHARLESTON_COUGARS = "College of Charleston Cougars Men's"
CAMPBELL_FIGHTING_CAMELS = "Campbell Fighting Camels Men's"
STONY_BROOKS_SEAWOLVES = "Stony Brook Seawolves Men's"
DELAWARE_FIGHTIN_BLUE_HENS = "Delaware Fightin' Blue Hens Men's"
NEW_MEXICO_STATE_AGGIES = "New Mexico State Aggies Men's"
FLORIDA_INTERNATIONAL_PANTHERS = "Florida International Panthers Men's"
NEW_HAMPSHIRE_WILDCATS = "New Hampshire Wildcats Men's"
UMBC_RETRIEVERS = "UMBC Retrievers Men's"
APPALACHIAN_STATE_MOUNTAINEERS = "Appalachian State Mountaineers Men's"
OLD_DOMINION_MONARCHS = "Old Dominion Monarchs Men's"
MARIST_RED_FOXES = "Marist Red Foxes Men's"
ST_PETERS_PEACOCKS = "St. Peter's Peacocks Men's"
QUEENS_ROYALS = "Queens (NC) Royals Men's"
STETSON_HATTERS = "Stetson Hatters Men's"
EASTERN_KENTUCKY_COLONELS = "Eastern Kentucky Colonels Men's"
AUSTIN_PEAY_GOVERNORS = "Austin Peay Governors Men's"
RUTGERS_SCARLET_KNIGHTS = "Rutgers Scarlet Knights Men's"
NEBRASKA_CORNHUSKERS = "Nebraska Cornhuskers Men's"
MARYLAND_TERRAPINS = "Maryland Terrapins Men's"
NORTHWESTERN_WILDCATS = "Northwestern Wildcats Men's"
SIU_EDWARDSVILLE_COUGARS = "SIU-Edwardsville Cougars Men's"
TENNESSEE_STATE_TIGERS = "Tennessee State Tigers Men's"
SOUTHEAST_MISSOURI_STATE_REDHAWKS = "Southeast Missouri State Redhawks Men's"
TENNESSEE_TECH_GOLDEN_EAGLES = "Tennessee Tech Golden Eagles Men's"
UC_RIVERSIDE_HIGHLANDERS = "UC-Riverside Highlanders Men's"
UCSB_GAUCHOS = "UCSB Gauchos Men's"
WASHINGTON_STATE_COUGARS = "Washington State Cougars Men's"
SAN_DIEGO_TOREROS = "San Diego Toreros Men's"
MERRIMACK_WARRIORS = "Merrimack Warriors Men's"
QUINNIPIAC_BOBCATS = "Quinnipiac Bobcats Men's"
COPPIN_STATE_EAGLES = "Coppin State Eagles Men's"
MAINE_BLACK_BEARS = "Maine Black Bears Men's"
NJIT_HIGHLANDERS = "NJIT Highlanders Men's"
BRYANT_BULLDOGS = "Bryant Bulldogs Men's"
ALBANY_NY_GREAT_DANES = "Albany (NY) Great Danes Men's"
LIPSCOMB_BISONS = "Lipscomb Bisons Men's"
BELLARMINE_KNIGHTS = "Bellarmine Knights Men's"
WEST_GEORGIA_WOLVES = "West Georgia Wolves Men's"
FLORIDA_GULF_COAST_EAGLES = "Florida Gulf Coast Eagles Men's"
GEORGIA_SOUTHERN_EAGLES = "Georgia Southern Eagles Men's"
COASTAL_CAROLINA_CHANTICLEERS = "Coastal Carolina Chanticleers Men's"
ELON_PHOENIX = "Elon Phoenix Men's"
DREXEL_DRAGONS = "Drexel Dragons Men's"
NIAGARA_PURPLE_EAGLES = "Niagara Purple Eagles Men's"
FAIRFIELD_STAGS = "Fairfield Stags Men's"
WILLIAM_AND_MARY_TRIBE = "William & Mary Tribe Men's"
HAMPTON_PIRATES = "Hampton Pirates Men's"
CANISIUS_GOLDEN_GRIFFINS = "Canisius Golden Griffins Men's"
IONA_GAELS = "Iona Gaels Men's"
NORTH_ALABAMA_LIONS = "North Alabama Lions Men's"
JACKSONVILLE_DOLPHINS = "Jacksonville Dolphins Men's"
LOUISIANA_TECH_BULLDOGS = "Louisiana Tech Bulldogs Men's"
JACKSONVILLE_STATE_GAMECOCKS = "Jacksonville State Gamecocks Men's"
MARSHALL_THUNDERING_HERD = "Marshall Thundering Herd Men's"
JAMES_MADISON_DUKES = "James Madison Dukes Men's"
SAM_HOUSTON_BEARKATS = "Sam Houston Bearkats Men's"
KENNESAW_STATE_OWLS = "Kennesaw State Owls Men's"
HIGH_POINT_PANTHERS = "High Point Panthers Men's"
LONGWOOD_LANCERS = "Longwood Lancers Men's"
WESTERN_ILLINOIS_LEATHERNECKS = "Western Illinois Leathernecks Men's"
MOREHEAD_STATE_EAGLES = "Morehead State Eagles Men's"
MONMOUTH_HAWKS = "Monmouth Hawks Men's"
NORTH_CAROLINA_ATT_AGGIES = "North Carolina A&T Aggies Men's"
NORTHEASTERN_HUSKIES = "Northeastern Huskies Men's"
UNC_WILMINGTON_SEAHAWKS = "UNC Wilmington Seahawks Men's"
CENTRAL_ARKANSAS_BEARS = "Central Arkansas Bears Men's"
NORTH_FLORIDA_OSPREYS = "North Florida Ospreys Men's"
MOUNT_ST_MARYS_MOUNTAINEERS = "Mount St. Mary's Mountaineers Men's"
RIDER_BRONCS = "Rider Broncs Men's"
SACRED_HEART_PIONEERS = "Sacred Heart Pioneers Men's"
SIENA_SAINTS = "Siena Saints Men's"
HOFSTRA_PRIDE = "Hofstra Pride Men's"
TOWSON_TIGERS = "Towson Tigers Men's"
BINGHAMTON_BEARCATS = "Binghamton Bearcats Men's"
VERMONT_CATAMOUNTS = "Vermont Catamounts Men's"
LOUISIANA_RAGIN_CAJUNS = "Louisiana Ragin' Cajuns Men's"
ARKANSAS_STATE_RED_WOLVES = "Arkansas State Red Wolves Men's"
MONTANA_STATE_BOBCATS = "Montana State Bobcats Men's"
IDAHO_STATE_BENGALS = "Idaho State Bengals Men's"
KANSAS_CITY_ROOS = "Kansas City Roos Men's"
NORTH_DAKOTA_STATE_BISON = "North Dakota State Bison Men's"
SACRAMENTO_STATE_HORNETS = "Sacramento State Hornets Men's"
NORTHERN_ARIZONA_LUMBERJACKS = "Northern Arizona Lumberjacks Men's"
ORAL_ROBERTS_GOLDEN_EAGLES = "Oral Roberts Golden Eagles Men's"
SOUTH_DAKOTA_COYOTES = "South Dakota Coyotes Men's"
NORTH_DAKOTA_FIGHTING_HAWKS = "North Dakota Fighting Hawks Men's"
SOUTH_DAKOTA_STATE_JACKRABBITS = "South Dakota State Jackrabbits Men's"
LINDENWOOD_LIONS = "Lindenwood Lions Men's"
SOUTHERN_INDIANA_SCREAMING_EAGLES = "Southern Indiana Screaming Eagles Men's"
CALIFORNIA_BAPTIST_LANCERS = "California Baptist Lancers Men's"
TARLETON_STATE_TEXANS = "Tarleton State Texans Men's"
EASTERN_ILLINOIS_PANTHERS = "Eastern Illinois Panthers Men's"
UT_MARTIN_SKYHAWKS = "UT-Martin Skyhawks Men's"
UTAH_VALLEY_WOLVERINES = "Utah Valley Wolverines Men's"
UT_ARLINGTON_MAVERICKS = "UT Arlington Mavericks Men's"
ABILENE_CHRISTIAN_WILDCATS = "Abilene Christian Wildcats Men's"
GRAND_CANYON_ANTELOPES = "Grand Canyon Antelopes Men's"
UTEP_MINERS = "UTEP Miners Men's"
LIBERTY_FLAMES = "Liberty Flames Men's"
PORTLAND_STATE_VIKINGS = "Portland State Vikings Men's"
NORTHERN_COLORADO_BEARS = "Northern Colorado Bears Men's"
MONTANA_GRIZZLIES = "Montana Grizzlies Men's"
WEBER_STATE_WILDCATS = "Weber State Wildcats Men's"
UC_DAVIS_AGGIES = "UC-Davis Aggies Men's"
CAL_POLY_MUSTANGS = "Cal Poly Mustangs Men's"
CAL_STATE_FULLERTON_TITANS = "Cal State Fullerton Titans Men's"
UC_IRVINE_ANTEATERS = "UC-Irvine Anteaters Men's"
UC_SAN_DIEGO_TRITONS = "UC-San Diego Tritons Men's"
LONG_BEACH_STATE_BEACH = "Long Beach State Beach Men's"
SANTA_CLARA_BRONCOS = "Santa Clara Broncos Men's"
LOYOLA_MARYMOUNT_LIONS = "Loyola Marymount Lions Men's"
SAN_FRANCISCO_DONS = "San Francisco Dons Men's"
PEPPERDINE_WAVES = "Pepperdine Waves Men's"
PACIFIC_TIGERS = "Pacific Tigers Men's"
PORTLAND_PILOTS = "Portland Pilots Men's"
UTAH_TECH_TRAILBLAZERS = "Utah Tech Trailblazers Men's"
SEATTLE_REDHAWKS = "Seattle Redhawks Men's"
KANSAS_JAYHAWKS = "Kansas Jayhawks Men's"
IOWA_STATE_CYCLONES = "Iowa State Cyclones Men's"
GEORGIA_BULLDOGS = "Georgia Bulldogs Men's"
TENNESSEE_VOLUNTEERS = "Tennessee Volunteers Men's"
WEST_VIRGINIA_MOUNTAINEERS = "West Virginia Mountaineers Men's"
HOUSTON_COUGARS = "Houston Cougars Men's"
PENN_STATE_NITTANY_LIONS = "Penn State Nittany Lions Men's"
MICHIGAN_STATE_SPARTANS = "Michigan State Spartans Men's"
PURDUE_BOILERMAKERS = "Purdue Boilermakers Men's"
WASHINGTON_HUSKIES = "Washington Huskies Men's"
UTAH_STATE_AGGIES = "Utah State Aggies Men's"
UNLV_REBELS = "UNLV Rebels Men's"
LAFAYETTE_LEOPARDS = "Lafayette Leopards Men's"
ARMY_BLACK_KNIGHTS = "Army Black Knights Men's"
WOFFORD_TERRIERS = "Wofford Terriers Men's"
CHATTANOOGA_MOCS = "Chattanooga Mocs Men's"
GEORGE_MASON_PATRIOTS = "George Mason Patriots Men's"
DAYTON_FLYERS = "Dayton Flyers Men's"
DAVIDSON_WILDCATS = "Davidson Wildcats Men's"
LA_SALLE_EXPLORERS = "La Salle Explorers Men's"
SAMFORD_BULLDOGS = "Samford Bulldogs Men's"
MERCER_BEARS = "Mercer Bears Men's"
GARDNER_WEBB_RUNNIN_BULLDOGS = "Gardner-Webb Runnin' Bulldogs Men's"
RADFORD_HIGHLANDERS = "Radford Highlanders Men's"
ILLINOIS_STATE_REDBIRDS = "Illinois State Redbirds Men's"
DRAKE_BULLDOGS = "Drake Bulldogs Men's"
RHODE_ISLAND_RAMS = "Rhode Island Rams Men's"
LOYOLA_IL_RAMBLERS = "Loyola (IL) Ramblers Men's"
SOUTHERN_ILLINOIS_SALUKIS = "Southern Illinois Salukis Men's"
MISSOURI_STATE_BEARS = "Missouri State Bears Men's"
LEHIGH_MOUNTAIN_HAWKS = "Lehigh Mountain Hawks Men's"
BOSTON_UNIVERSITY_TERRIERS = "Boston University Terriers Men's"
USC_UPSTATE_SPARTANS = "USC Upstate Spartans Men's"
UNC_ASHEVILLE_BULLDOGS = "UNC Asheville Bulldogs Men's"
SOUTH_CAROLINA_GAMECOCKS = "South Carolina Gamecocks Men's"
VANDERBILT_COMMODORES = "Vanderbilt Commodores Men's"
WESTERN_CAROLINA_CATAMOUNTS = "Western Carolina Catamounts Men's"
VMI_KEYDETS = "VMI Keydets Men's"
STANFORD_CARDINAL = "Stanford Cardinal Men's"
WAKE_FOREST_DEMON_DEACONS = "Wake Forest Demon Deacons Men's"
CHARLESTON_SOUTHERN_BUCCANEERS = "Charleston Southern Buccaneers Men's"
WINTHROP_EAGLES = "Winthrop Eagles Men's"
HOLY_CROSS_CRUSADERS = "Holy Cross Crusaders Men's"
BUCKNELL_BISON = "Bucknell Bison Men's"
SETON_HALL_PIRATES = "Seton Hall Pirates Men's"
BUTLER_BULLDOGS = "Butler Bulldogs Men's"
NORTHERN_KENTUCKY_NORSE = "Northern Kentucky Norse Men's"
CLEVELAND_STATE_VIKINGS = "Cleveland State Vikings Men's"
UMASS_MINUTEMEN = "UMass Minutemen Men's"
FORDHAM_RAMS = "Fordham Rams Men's"
ETSU_BUCCANEERS = "ETSU Buccaneers Men's"
FURMANS_PALADINS = "Furman Paladins Men's"
DUQUESNE_DUKES = "Duquesne Dukes Men's"
GEORGE_WASHINGTON_REVOLUTIONARIES = "George Washington Revolutionaries Men's"
HOWARD_BISON = "Howard Bison Men's"
TROY_TROJANS = "Troy Trojans Men's"
LOUISIANA_MONRE_WARHAWKS = "Louisiana-Monroe Warhawks Men's"
COLGATE_RAIDERS = "Colgate Raiders Men's"
NAVY_MIDSHIPMEN = "Navy Midshipmen Men's"
CALIFORNIA_GOLDEN_BEARS = "California Golden Bears Men's"
UNC_TAR_HEELS = "UNC Tar Heels Men's"
THE_CITADEL_BULLDOGS = "The Citadel Bulldogs Men's"
UNC_GREENSBORO_SPARTANS = "UNC Greensboro Spartans Men's"
IU_INDIANAPOLIS_JAGUARS = "IU Indianapolis Jaguars Men's"
OAKLAND_GOLDEN_GRIZZLIES = "Oakland Golden Grizzlies Men's"
UAB_BLAZERS = "UAB Blazers Men's"
SOUTH_FLORIDA_BULLS = "South Florida Bulls Men's"
RICHMOND_SPIDERS = "Richmond Spiders Men's"
ST_BONAVENTURE_BONNIES = "St. Bonaventure Bonnies Men's"
FLORIDA_ATLANTIC_OWLS = "Florida Atlantic Owls Men's"
TULANE_GREEN_WAVE = "Tulane Green Wave Men's"
NC_STATE_WOLFPACK = "NC State Wolfpack Men's"
VIRGINIA_TECH_HOKIES = "Virginia Tech Hokies Men's"
PURDUE_FORT_WAYNE_MASTODONS = "Purdue Fort Wayne Mastodons Men's"
WRIGHT_STATE_RAIDERS = "Wright State Raiders Men's"
INDIANA_STATE_SYCAMORES = "Indiana State Sycamores Men's"
BRADLEY_BRAVES = "Bradley Braves Men's"
MURRAY_STATE_RACERS = "Murray State Racers Men's"
UIC_FLAMES = "UIC Flames Men's"
SOUTHERN_MISS_GOLDEN_EAGLES = "Southern Miss Golden Eagles Men's"
SOUTH_ALABAMA_JAGUARS = "South Alabama Jaguars Men's"
UTAH_UTES = "Utah Utes Men's"
TCU_HORNED_FROGS = "TCU Horned Frogs Men's"
GEORGIA_STATE_PANTHERS = "Georgia State Panthers Men's"
TEXAS_STATE_BOBCATS = "Texas State Bobcats Men's"
CINCINNATI_BEARCATS = "Cincinnati Bearcats Men's"
COLORADO_BUFFALOES = "Colorado Buffaloes Men's"
OMAHA_MAVERICKS = "Omaha Mavericks Men's"
DENVER_PIONEERS = "Denver Pioneers Men's"
PITT_PANTHERS = "Pitt Panthers Men's"
FLORIDA_STATE_SEMINOLES = "Florida State Seminoles Men's"
SMU_MUSTANGS = "SMU Mustangs Men's"
VIRGINIA_CAVALIERS = "Virginia Cavaliers Men's"
TEXAS_LONGHORNS = "Texas Longhorns Men's"
OKLAHOMA_SOONERS = "Oklahoma Sooners Men's"
MISSISSIPPI_STATE_BULLDOGS = "Mississippi State Bulldogs Men's"
AUBURN_TIGERS = "Auburn Tigers Men's"
MIAMI_FL_HURRIANCES = "Miami (FL) Hurricanes Men's"
DUKE_BLUE_DEVILS = "Duke Blue Devils Men's"
OLE_MISS_REBELS = "Ole Miss Rebels Men's"
ALABAMA_CRIMSON_TIDE = "Alabama Crimson Tide Men's"
MISSOURI_TIGERS = "Missouri Tigers Men's"
FLORIDA_GATORS = "Florida Gators Men's"
MARQUETTE_GOLDEN_EAGLES = "Marquette Golden Eagles Men's"
TEXAS_AM_AGGIES = "Texas A&M Aggies Men's"
KENTUCKY_WILDCATS = "Kentucky Wildcats Men's"
ILLINOIS_FIGHTING_ILLINI = "Illinois Fighting Illini Men's"
WISCONSIN_BADGERS = "Wisconsin Badgers Men's"
BAYLOR_BEARS = "Baylor Bears Men's"
ARIZONA_WILDCATS = "Arizona Wildcats Men's"
WESTERN_MICHIGAN_BRONCOS = "Western Michigan Broncos Men's"
KENT_STATE_GOLDEN_FLASHES = "Kent State Golden Flashes Men's"
ST_JOHNS_NY_RED_STORM = "St. John's (NY) Red Storm Men's"
SAINT_LOUIS_BILLIKENS = "Saint Louis Billikens Men's"
VALPARAISO_BEACONS = "Valparaiso Beacons Men's"
BELMONT_BRUINS = "Belmont Bruins Men's"
TEXAS_TECH_RED_RAIDERS = "Texas Tech Red Raiders Men's"
KANSAS_STATE_WILDCATS = "Kansas State Wildcats Men's"
MIAMI_OH_REDHAWKS = "Miami (OH) RedHawks Men's"
NORTHERN_ILLINOIS_HUSKIES = "Northern Illinois Huskies Men's"
EVANSVILLE_PURPLE_ACES = "Evansville Purple Aces Men's"
NORTHERN_IOWA_PANTHERS = "Northern Iowa Panthers Men's"
UCF_KNIGHTS = "UCF Knights Men's"
ARIZONA_STATE_SUN_DEVILS = "Arizona State Sun Devils Men's"
NEVADA_WOLF_PACK = "Nevada Wolf Pack Men's"
SAN_JOSE_STATE_SPARTANS = "San Jose State Spartans Men's"
USC_TROJANS = "USC Trojans Men's"
XAVIER_MUSKETEERS = "Xavier Musketeers Men's"
TOLEDO_ROCKETS = "Toledo Rockets Men's"
BUFFALO_BULLS = "Buffalo Bulls Men's"
BOWLING_GREEN_STATE_FALCONS = "Bowling Green State Falcons Men's"
EASTERN_MICHIGAN_EAGLES = "Eastern Michigan Eagles Men's"
CENTRAL_MICHIGAN_CHIPPEWAS = "Central Michigan Chippewas Men's"
NORTH_TEXAS_MEAN_GREEN = "North Texas Mean Green Men's"
EAST_CAROLINA_PIRATES = "East Carolina Pirates Men's"
BALL_STATE_CARDINALS = "Ball State Cardinals Men's"
LOUISVILLE_CARDINALS = "Louisville Cardinals Men's"
SYRACUSE_ORANGE = "Syracuse Orange Men's"
CHARLOTTE_49ERS = "Charlotte 49ers Men's"
WICHITA_STATE_SHOCKERS = "Wichita State Shockers Men's"
CREIGHTON_BLUEJAYS = "Creighton Bluejays Men's"
UTSA_ROADRUNNERS = "UTSA Roadrunners Men's"
RICE_OWLS = "Rice Owls Men's"
LITTLE_ROCK_TROJANS = "Little Rock Trojans Men's"
WYOMING_COWBOYS = "Wyoming Cowboys Men's"
OKLAHOMA_STATE_COWBOYS = "Oklahoma State Cowboys Men's"
BYU_COUGARS = "BYU Cougars Men's"
CLEMSON_TIGERS = "Clemson Tigers Men's"
GEORGIA_TECH_YELLOW_JACKETS = "Georgia Tech Yellow Jackets Men's"
ARKANSAS_RAZORBACKS = "Arkansas Razorbacks Men's"
LSU_FIGHTING_TIGERS = "LSU Fighting Tigers Men's"
COLORADO_STATE_RAMS = "Colorado State Rams Men's"
SAN_DIEGO_STATE_AZTECS = "San Diego State Aztecs Men's"
AMERICAN_EAGLES = "American Eagles Men's"
LOYOLA_MD_GREYHOUNDS = "Loyola (MD) Greyhounds Men's"
ALABAMA_STATE_HORNETS = "Alabama State Hornets Men's"
ALCORN_STATE_BRAVES = "Alcorn State Braves Men's"
PRAIRIE_VIEW_PANTHERS = "Prairie View Panthers Men's"
ARKANSAS_PINE_BLUFF_GOLDEN_LIONS = "Arkansas-Pine Bluff Golden Lions Men's"
FLORIDA_AM_RATTLERS = "Florida A&M Rattlers Men's"
GRAMBLING_TIGERS = "Grambling Tigers Men's"
NICHOLLS_STATE_COLONELS = "Nicholls State Colonels Men's"
INCARNATE_WORD_CARDINALS = "Incarnate Word Cardinals Men's"
ALABAMA_AM_BULLDOGS = "Alabama A&M Bulldogs Men's"
JACKSON_STATE_TIGERS = "Jackson State Tigers Men's"
TEXAS_SOUTHERN_TIGERS = "Texas Southern Tigers Men's"
MISSISSIPPI_VALLEY_STATE_DELTA_DEVILS = "Mississippi Valley State Delta Devils Men's"
NORFOLK_STATE_SPARTANS = "Norfolk State Spartans Men's"
MORGAN_STATE_BEARS = "Morgan State Bears Men's"
DELAWARE_STATE_HORNETS = "Delaware State Hornets Men's"
NORTH_CAROLINA_CENTRAL_EAGLES = "North Carolina Central Eagles Men's"
BOSTON_COLLEGE_EAGLES = "Boston College Eagles Men's"
NOTRE_DAME_FIGHTING_IRISH = "Notre Dame Fighting Irish Men's"
MARYLAND_EASTERN_SHORE_HAWKS = "Maryland-Eastern Shore Hawks Men's"
SOUTH_CAROLINA_STATE_BULLDOGS = "South Carolina State Bulldogs Men's"
SOUTHEASTERN_LOUISIANA_LIONS = "Southeastern Louisiana Lions Men's"
STEPHEN_F_AUSTIN_LUMBERJACKS = "Stephen F. Austin Lumberjacks Men's"
EAST_TEXAS_AM_LIONS = "East Texas A&M Lions Men's"
TEXAS_RIO_GRANDE_VALLEY_VAQUEROS = "Texas-Rio Grande Valley Vaqueros Men's"
MCNEESE_STATE_COWBOYS = "McNeese State Cowboys Men's"
HOUSTON_CHRISTIAN_HUSKIES = "Houston Christian Huskies Men's"
NEW_ORLEANS_PRIVATEERS = "New Orleans Privateers Men's"
LAMAR_CARDINALS = "Lamar Cardinals Men's"
BETHUNE_COOKMAN_WILDCATS = "Bethune-Cookman Wildcats Men's"
SOUTHERN_JAGUARS = "Southern Jaguars Men's"
NORTHWESTERN_STATE_DEMONS = "Northwestern State Demons Men's"
TEXAS_AM_CORPUS_CHRISTI_ISLANDERS = "Texas A&M-Corpus Christi Islanders Men's"
OREGON_DUCKS = "Oregon Ducks Men's"
MANHATTAN_JASPERS = "Manhattan Jaspers Men's"
LIU_SHARKS = "LIU Sharks Men's"
CENTRAL_CONNECTICUT_BLUE_DEVILS = "Central Connecticut Blue Devils Men's"
SAINT_FRANCIS_PA_RED_FLASH = "Saint Francis (PA) Red Flash Men's"
FDU_KNIGHTS = "FDU Knights Men's"
STONEHILL_SKYHAWKS = "Stonehill Skyhawks Men's"
CHICAGO_STATE_COUGARS = "Chicago State Cougars Men's"
MERCYHURST_LAKERS = "Mercyhurst Lakers Men's"
LE_MOYNE_DOLPHINS = "Le Moyne Dolphins Men's"
TULSA_GOLDEN_HURRICANE = "Tulsa Golden Hurricane Men's"
UCONN_HUSKIES = "UConn Huskies Men's"
PENN_QUAKERS = "Penn Quakers Men's"
DARTMOUTH_BIG_GREEN = "Dartmouth Big Green Men's"
UMASS_LOWELL_RIVER_HAWKS = "UMass-Lowell River Hawks Men's"
WESTERN_KENTUCKY_HILLTOPPERS = "Western Kentucky Hilltoppers Men's"
SAINT_MARYS_GAELS = "Saint Mary's Gaels Men's"
CORNELL_BIG_RED = "Cornell Big Red Men's"
COLUMBIA_LIONS = "Columbia Lions Men's"
PRINCETON_TIGERS = "Princeton Tigers Men's"
HARVARD_CRIMSON = "Harvard Crimson Men's"
PRESBYTERIAN_BLUE_HOSE = "Presbyterian Blue Hose Men's"
BROWN_BEARS = "Brown Bears Men's"
YALE_BULLDOGS = "Yale Bulldogs Men's"
EASTERN_WASHINGTON_EAGLES = "Eastern Washington Eagles Men's"
IDAHO_VANDALS = "Idaho Vandals Men's"
MIDDLE_TENNESSEE_BLUE_RAIDERS = "Middle Tennessee Blue Raiders Men's"
DETROIT_MERCY_TITANS = "Detroit Mercy Titans Men's"
SOUTHERN_UTAH_THUNDERBIRDS = "Southern Utah Thunderbirds Men's"
ST_THOMAS_TOMMIES = "St. Thomas Tommies Men's"
CAL_STATE_BAKERSFIELD_ROADRUNNERS = "Cal State Bakersfield Roadrunners Men's"
WAGNER_SEAHAWKS = "Wagner Seahawks Men's"
NCAAB_TEAM_IDENTITY_MAP: dict[str, str] = {
    "DePaul Blue Demons Men's": DEPAUL_BLUE_DEMONS,
    "Georgetown Hoyas Men's": GEORGETOWN_HOYAS,
    "Cal State Northridge Matadors Men's": CAL_STATE_NORTHRIDGE_MATADORS,
    "Hawaii Rainbow Warriors Men's": HAWAII_RAINBOW_WARRIORS,
    "Indiana Hoosiers Men's": INDIANA_HOOSIERS,
    "Ohio State Buckeyes Men's": OHIO_STATE_BUCKEYES,
    "Ohio Bobcats Men's": OHIO_BOBCATS,
    "Akron Zips Men's": AKRON_ZIPS,
    "Robert Morris Colonials Men's": ROBERT_MORRIS_COLONIALS,
    "Green Bay Phoenix Men's": GREEN_BAY_PHOENIX,
    "VCU Rams Men's": VCU_RAMS,
    "St. Joseph's Hawks Men's": ST_JOSEPHS_HAWKS,
    "Providence Friars Men's": PROVIDENCE_FRIARS,
    "Villanova Wildcats Men's": VILLANOVA_WILDCATS,
    "Youngstown State Penguins Men's": YOUNGSTOWN_STATE_PENGUINS,
    "Milwaukee Panthers Men's": MILWAUKEE_PANTHERS,
    "Iowa Hawkeyes Men's": IOWA_HAWKEYES,
    "UCLA Bruins Men's": UCLA_BRUINS,
    "Air Force Falcons Men's": AIR_FORCE_FALCONS,
    "Fresno State Bulldogs Men's": FRESNO_STATE_BULLDOGS,
    "Boise State Broncos Men's": BOISE_STATE_BRONCOS,
    "New Mexico Lobos Men's": NEW_MEXICO_LOBOS,
    "Gonzaga Bulldogs Men's": GONZAGA_BULLDOGS,
    "Oregon State Beavers Men's": OREGON_STATE_BEAVERS,
    "Memphis Tigers Men's": MEMPHIS_TIGERS,
    "Temple Owls Men's": TEMPLE_OWLS,
    "Michigan Wolverines Men's": MICHIGAN_WOLVERINES,
    "Minnesota Golden Gophers Men's": MINNESOTA_GOLDEN_GOPHERS,
    "College of Charleston Cougars Men's": COLLEGE_CHARLESTON_COUGARS,
    "Campbell Fighting Camels Men's": CAMPBELL_FIGHTING_CAMELS,
    "Stony Brook Seawolves Men's": STONY_BROOKS_SEAWOLVES,
    "Delaware Fightin' Blue Hens Men's": DELAWARE_FIGHTIN_BLUE_HENS,
    "New Mexico State Aggies Men's": NEW_MEXICO_STATE_AGGIES,
    "Florida International Panthers Men's": FLORIDA_INTERNATIONAL_PANTHERS,
    "New Hampshire Wildcats Men's": NEW_HAMPSHIRE_WILDCATS,
    "UMBC Retrievers Men's": UMBC_RETRIEVERS,
    "Appalachian State Mountaineers Men's": APPALACHIAN_STATE_MOUNTAINEERS,
    "Old Dominion Monarchs Men's": OLD_DOMINION_MONARCHS,
    "Marist Red Foxes Men's": MARIST_RED_FOXES,
    "St. Peter's Peacocks Men's": ST_PETERS_PEACOCKS,
    "Queens (NC) Royals Men's": QUEENS_ROYALS,
    "Stetson Hatters Men's": STETSON_HATTERS,
    "Eastern Kentucky Colonels Men's": EASTERN_KENTUCKY_COLONELS,
    "Austin Peay Governors Men's": AUSTIN_PEAY_GOVERNORS,
    "Rutgers Scarlet Knights Men's": RUTGERS_SCARLET_KNIGHTS,
    "Nebraska Cornhuskers Men's": NEBRASKA_CORNHUSKERS,
    "Maryland Terrapins Men's": MARYLAND_TERRAPINS,
    "Northwestern Wildcats Men's": NORTHWESTERN_WILDCATS,
    "SIU-Edwardsville Cougars Men's": SIU_EDWARDSVILLE_COUGARS,
    "Tennessee State Tigers Men's": TENNESSEE_STATE_TIGERS,
    "Southeast Missouri State Redhawks Men's": SOUTHEAST_MISSOURI_STATE_REDHAWKS,
    "Tennessee Tech Golden Eagles Men's": TENNESSEE_TECH_GOLDEN_EAGLES,
    "UC-Riverside Highlanders Men's": UC_RIVERSIDE_HIGHLANDERS,
    "UCSB Gauchos Men's": UCSB_GAUCHOS,
    "Washington State Cougars Men's": WASHINGTON_STATE_COUGARS,
    "San Diego Toreros Men's": SAN_DIEGO_TOREROS,
    "Merrimack Warriors Men's": MERRIMACK_WARRIORS,
    "Quinnipiac Bobcats Men's": QUINNIPIAC_BOBCATS,
    "Coppin State Eagles Men's": COPPIN_STATE_EAGLES,
    "Maine Black Bears Men's": MAINE_BLACK_BEARS,
    "NJIT Highlanders Men's": NJIT_HIGHLANDERS,
    "Bryant Bulldogs Men's": BRYANT_BULLDOGS,
    "Albany (NY) Great Danes Men's": ALBANY_NY_GREAT_DANES,
    "Lipscomb Bisons Men's": LIPSCOMB_BISONS,
    "Bellarmine Knights Men's": BELLARMINE_KNIGHTS,
    "West Georgia Wolves Men's": WEST_GEORGIA_WOLVES,
    "Florida Gulf Coast Eagles Men's": FLORIDA_GULF_COAST_EAGLES,
    "Georgia Southern Eagles Men's": GEORGIA_SOUTHERN_EAGLES,
    "Coastal Carolina Chanticleers Men's": COASTAL_CAROLINA_CHANTICLEERS,
    "Elon Phoenix Men's": ELON_PHOENIX,
    "Drexel Dragons Men's": DREXEL_DRAGONS,
    "Niagara Purple Eagles Men's": NIAGARA_PURPLE_EAGLES,
    "Fairfield Stags Men's": FAIRFIELD_STAGS,
    "William & Mary Tribe Men's": WILLIAM_AND_MARY_TRIBE,
    "Hampton Pirates Men's": HAMPTON_PIRATES,
    "Canisius Golden Griffins Men's": CANISIUS_GOLDEN_GRIFFINS,
    "Iona Gaels Men's": IONA_GAELS,
    "North Alabama Lions Men's": NORTH_ALABAMA_LIONS,
    "Jacksonville Dolphins Men's": JACKSONVILLE_DOLPHINS,
    "Louisiana Tech Bulldogs Men's": LOUISIANA_TECH_BULLDOGS,
    "Jacksonville State Gamecocks Men's": JACKSONVILLE_STATE_GAMECOCKS,
    "Marshall Thundering Herd Men's": MARSHALL_THUNDERING_HERD,
    "James Madison Dukes Men's": JAMES_MADISON_DUKES,
    "Sam Houston Bearkats Men's": SAM_HOUSTON_BEARKATS,
    "Kennesaw State Owls Men's": KENNESAW_STATE_OWLS,
    "High Point Panthers Men's": HIGH_POINT_PANTHERS,
    "Longwood Lancers Men's": LONGWOOD_LANCERS,
    "Western Illinois Leathernecks Men's": WESTERN_ILLINOIS_LEATHERNECKS,
    "Morehead State Eagles Men's": MOREHEAD_STATE_EAGLES,
    "Monmouth Hawks Men's": MONMOUTH_HAWKS,
    "North Carolina A&T Aggies Men's": NORTH_CAROLINA_ATT_AGGIES,
    "Northeastern Huskies Men's": NORTHEASTERN_HUSKIES,
    "UNC Wilmington Seahawks Men's": UNC_WILMINGTON_SEAHAWKS,
    "Central Arkansas Bears Men's": CENTRAL_ARKANSAS_BEARS,
    "North Florida Ospreys Men's": NORTH_FLORIDA_OSPREYS,
    "Mount St. Mary's Mountaineers Men's": MOUNT_ST_MARYS_MOUNTAINEERS,
    "Rider Broncs Men's": RIDER_BRONCS,
    "Sacred Heart Pioneers Men's": SACRED_HEART_PIONEERS,
    "Siena Saints Men's": SIENA_SAINTS,
    "Hofstra Pride Men's": HOFSTRA_PRIDE,
    "Towson Tigers Men's": TOWSON_TIGERS,
    "Binghamton Bearcats Men's": BINGHAMTON_BEARCATS,
    "Vermont Catamounts Men's": VERMONT_CATAMOUNTS,
    "Louisiana Ragin' Cajuns Men's": LOUISIANA_RAGIN_CAJUNS,
    "Arkansas State Red Wolves Men's": ARKANSAS_STATE_RED_WOLVES,
    "Montana State Bobcats Men's": MONTANA_STATE_BOBCATS,
    "Idaho State Bengals Men's": IDAHO_STATE_BENGALS,
    "Kansas City Roos Men's": KANSAS_CITY_ROOS,
    "North Dakota State Bison Men's": NORTH_DAKOTA_STATE_BISON,
    "Sacramento State Hornets Men's": SACRAMENTO_STATE_HORNETS,
    "Northern Arizona Lumberjacks Men's": NORTHERN_ARIZONA_LUMBERJACKS,
    "Oral Roberts Golden Eagles Men's": ORAL_ROBERTS_GOLDEN_EAGLES,
    "South Dakota Coyotes Men's": SOUTH_DAKOTA_COYOTES,
    "North Dakota Fighting Hawks Men's": NORTH_DAKOTA_FIGHTING_HAWKS,
    "South Dakota State Jackrabbits Men's": SOUTH_DAKOTA_STATE_JACKRABBITS,
    "Lindenwood Lions Men's": LINDENWOOD_LIONS,
    "Southern Indiana Screaming Eagles Men's": SOUTHERN_INDIANA_SCREAMING_EAGLES,
    "California Baptist Lancers Men's": CALIFORNIA_BAPTIST_LANCERS,
    "Tarleton State Texans Men's": TARLETON_STATE_TEXANS,
    "Eastern Illinois Panthers Men's": EASTERN_ILLINOIS_PANTHERS,
    "UT-Martin Skyhawks Men's": UT_MARTIN_SKYHAWKS,
    "Utah Valley Wolverines Men's": UTAH_VALLEY_WOLVERINES,
    "UT Arlington Mavericks Men's": UT_ARLINGTON_MAVERICKS,
    "Abilene Christian Wildcats Men's": ABILENE_CHRISTIAN_WILDCATS,
    "Grand Canyon Antelopes Men's": GRAND_CANYON_ANTELOPES,
    "UTEP Miners Men's": UTEP_MINERS,
    "Liberty Flames Men's": LIBERTY_FLAMES,
    "Portland State Vikings Men's": PORTLAND_STATE_VIKINGS,
    "Northern Colorado Bears Men's": NORTHERN_COLORADO_BEARS,
    "Montana Grizzlies Men's": MONTANA_GRIZZLIES,
    "Weber State Wildcats Men's": WEBER_STATE_WILDCATS,
    "UC-Davis Aggies Men's": UC_DAVIS_AGGIES,
    "Cal Poly Mustangs Men's": CAL_POLY_MUSTANGS,
    "Cal State Fullerton Titans Men's": CAL_STATE_FULLERTON_TITANS,
    "UC-Irvine Anteaters Men's": UC_IRVINE_ANTEATERS,
    "UC-San Diego Tritons Men's": UC_SAN_DIEGO_TRITONS,
    "Long Beach State Beach Men's": LONG_BEACH_STATE_BEACH,
    "Santa Clara Broncos Men's": SANTA_CLARA_BRONCOS,
    "Loyola Marymount Lions Men's": LOYOLA_MARYMOUNT_LIONS,
    "San Francisco Dons Men's": SAN_FRANCISCO_DONS,
    "Pepperdine Waves Men's": PEPPERDINE_WAVES,
    "Pacific Tigers Men's": PACIFIC_TIGERS,
    "Portland Pilots Men's": PORTLAND_PILOTS,
    "Utah Tech Trailblazers Men's": UTAH_TECH_TRAILBLAZERS,
    "Seattle Redhawks Men's": SEATTLE_REDHAWKS,
    "Kansas Jayhawks Men's": KANSAS_JAYHAWKS,
    "Iowa State Cyclones Men's": IOWA_STATE_CYCLONES,
    "Georgia Bulldogs Men's": GEORGIA_BULLDOGS,
    "Tennessee Volunteers Men's": TENNESSEE_VOLUNTEERS,
    "West Virginia Mountaineers Men's": WEST_VIRGINIA_MOUNTAINEERS,
    "Houston Cougars Men's": HOUSTON_COUGARS,
    "Penn State Nittany Lions Men's": PENN_STATE_NITTANY_LIONS,
    "Michigan State Spartans Men's": MICHIGAN_STATE_SPARTANS,
    "Purdue Boilermakers Men's": PURDUE_BOILERMAKERS,
    "Washington Huskies Men's": WASHINGTON_HUSKIES,
    "Utah State Aggies Men's": UTAH_STATE_AGGIES,
    "UNLV Rebels Men's": UNLV_REBELS,
    "Lafayette Leopards Men's": LAFAYETTE_LEOPARDS,
    "Army Black Knights Men's": ARMY_BLACK_KNIGHTS,
    "Wofford Terriers Men's": WOFFORD_TERRIERS,
    "Chattanooga Mocs Men's": CHATTANOOGA_MOCS,
    "George Mason Patriots Men's": GEORGE_MASON_PATRIOTS,
    "Dayton Flyers Men's": DAYTON_FLYERS,
    "Davidson Wildcats Men's": DAVIDSON_WILDCATS,
    "La Salle Explorers Men's": LA_SALLE_EXPLORERS,
    "Samford Bulldogs Men's": SAMFORD_BULLDOGS,
    "Mercer Bears Men's": MERCER_BEARS,
    "Gardner-Webb Runnin' Bulldogs Men's": GARDNER_WEBB_RUNNIN_BULLDOGS,
    "Radford Highlanders Men's": RADFORD_HIGHLANDERS,
    "Illinois State Redbirds Men's": ILLINOIS_STATE_REDBIRDS,
    "Drake Bulldogs Men's": DRAKE_BULLDOGS,
    "Rhode Island Rams Men's": RHODE_ISLAND_RAMS,
    "Loyola (IL) Ramblers Men's": LOYOLA_IL_RAMBLERS,
    "Southern Illinois Salukis Men's": SOUTHERN_ILLINOIS_SALUKIS,
    "Missouri State Bears Men's": MISSOURI_STATE_BEARS,
    "Lehigh Mountain Hawks Men's": LEHIGH_MOUNTAIN_HAWKS,
    "Boston University Terriers Men's": BOSTON_UNIVERSITY_TERRIERS,
    "USC Upstate Spartans Men's": USC_UPSTATE_SPARTANS,
    "UNC Asheville Bulldogs Men's": UNC_ASHEVILLE_BULLDOGS,
    "South Carolina Gamecocks Men's": SOUTH_CAROLINA_GAMECOCKS,
    "Vanderbilt Commodores Men's": VANDERBILT_COMMODORES,
    "Western Carolina Catamounts Men's": WESTERN_CAROLINA_CATAMOUNTS,
    "VMI Keydets Men's": VMI_KEYDETS,
    "Stanford Cardinal Men's": STANFORD_CARDINAL,
    "Wake Forest Demon Deacons Men's": WAKE_FOREST_DEMON_DEACONS,
    "Charleston Southern Buccaneers Men's": CHARLESTON_SOUTHERN_BUCCANEERS,
    "Winthrop Eagles Men's": WINTHROP_EAGLES,
    "Holy Cross Crusaders Men's": HOLY_CROSS_CRUSADERS,
    "Bucknell Bison Men's": BUCKNELL_BISON,
    "Seton Hall Pirates Men's": SETON_HALL_PIRATES,
    "Butler Bulldogs Men's": BUTLER_BULLDOGS,
    "Northern Kentucky Norse Men's": NORTHERN_KENTUCKY_NORSE,
    "Cleveland State Vikings Men's": CLEVELAND_STATE_VIKINGS,
    "UMass Minutemen Men's": UMASS_MINUTEMEN,
    "Fordham Rams Men's": FORDHAM_RAMS,
    "ETSU Buccaneers Men's": ETSU_BUCCANEERS,
    "Furman Paladins Men's": FURMANS_PALADINS,
    "Duquesne Dukes Men's": DUQUESNE_DUKES,
    "George Washington Revolutionaries Men's": GEORGE_WASHINGTON_REVOLUTIONARIES,
    "Howard Bison Men's": HOWARD_BISON,
    "Troy Trojans Men's": TROY_TROJANS,
    "Louisiana-Monroe Warhawks Men's": LOUISIANA_MONRE_WARHAWKS,
    "Colgate Raiders Men's": COLGATE_RAIDERS,
    "Navy Midshipmen Men's": NAVY_MIDSHIPMEN,
    "California Golden Bears Men's": CALIFORNIA_GOLDEN_BEARS,
    "UNC Tar Heels Men's": UNC_TAR_HEELS,
    "The Citadel Bulldogs Men's": THE_CITADEL_BULLDOGS,
    "UNC Greensboro Spartans Men's": UNC_GREENSBORO_SPARTANS,
    "IU Indianapolis Jaguars Men's": IU_INDIANAPOLIS_JAGUARS,
    "Oakland Golden Grizzlies Men's": OAKLAND_GOLDEN_GRIZZLIES,
    "UAB Blazers Men's": UAB_BLAZERS,
    "South Florida Bulls Men's": SOUTH_FLORIDA_BULLS,
    "Richmond Spiders Men's": RICHMOND_SPIDERS,
    "St. Bonaventure Bonnies Men's": ST_BONAVENTURE_BONNIES,
    "Florida Atlantic Owls Men's": FLORIDA_ATLANTIC_OWLS,
    "Tulane Green Wave Men's": TULANE_GREEN_WAVE,
    "NC State Wolfpack Men's": NC_STATE_WOLFPACK,
    "Virginia Tech Hokies Men's": VIRGINIA_TECH_HOKIES,
    "Purdue Fort Wayne Mastodons Men's": PURDUE_FORT_WAYNE_MASTODONS,
    "Wright State Raiders Men's": WRIGHT_STATE_RAIDERS,
    "Indiana State Sycamores Men's": INDIANA_STATE_SYCAMORES,
    "Bradley Braves Men's": BRADLEY_BRAVES,
    "Murray State Racers Men's": MURRAY_STATE_RACERS,
    "UIC Flames Men's": UIC_FLAMES,
    "Southern Miss Golden Eagles Men's": SOUTHERN_MISS_GOLDEN_EAGLES,
    "South Alabama Jaguars Men's": SOUTH_ALABAMA_JAGUARS,
    "Utah Utes Men's": UTAH_UTES,
    "TCU Horned Frogs Men's": TCU_HORNED_FROGS,
    "Georgia State Panthers Men's": GEORGIA_STATE_PANTHERS,
    "Texas State Bobcats Men's": TEXAS_STATE_BOBCATS,
    "Cincinnati Bearcats Men's": CINCINNATI_BEARCATS,
    "Colorado Buffaloes Men's": COLORADO_BUFFALOES,
    "Omaha Mavericks Men's": OMAHA_MAVERICKS,
    "Denver Pioneers Men's": DENVER_PIONEERS,
    "Pitt Panthers Men's": PITT_PANTHERS,
    "Florida State Seminoles Men's": FLORIDA_STATE_SEMINOLES,
    "SMU Mustangs Men's": SMU_MUSTANGS,
    "Virginia Cavaliers Men's": VIRGINIA_CAVALIERS,
    "Texas Longhorns Men's": TEXAS_LONGHORNS,
    "Oklahoma Sooners Men's": OKLAHOMA_SOONERS,
    "Mississippi State Bulldogs Men's": MISSISSIPPI_STATE_BULLDOGS,
    "Auburn Tigers Men's": AUBURN_TIGERS,
    "Miami (FL) Hurricanes Men's": MIAMI_FL_HURRIANCES,
    "Duke Blue Devils Men's": DUKE_BLUE_DEVILS,
    "Ole Miss Rebels Men's": OLE_MISS_REBELS,
    "Alabama Crimson Tide Men's": ALABAMA_CRIMSON_TIDE,
    "Missouri Tigers Men's": MISSOURI_TIGERS,
    "Florida Gators Men's": FLORIDA_GATORS,
    "Marquette Golden Eagles Men's": MARQUETTE_GOLDEN_EAGLES,
    "Texas A&M Aggies Men's": TEXAS_AM_AGGIES,
    "Kentucky Wildcats Men's": KENTUCKY_WILDCATS,
    "Illinois Fighting Illini Men's": ILLINOIS_FIGHTING_ILLINI,
    "Wisconsin Badgers Men's": WISCONSIN_BADGERS,
    "Baylor Bears Men's": BAYLOR_BEARS,
    "Arizona Wildcats Men's": ARIZONA_WILDCATS,
    "Western Michigan Broncos Men's": WESTERN_MICHIGAN_BRONCOS,
    "Kent State Golden Flashes Men's": KENT_STATE_GOLDEN_FLASHES,
    "St. John's (NY) Red Storm Men's": ST_JOHNS_NY_RED_STORM,
    "Saint Louis Billikens Men's": SAINT_LOUIS_BILLIKENS,
    "Valparaiso Beacons Men's": VALPARAISO_BEACONS,
    "Belmont Bruins Men's": BELMONT_BRUINS,
    "Texas Tech Red Raiders Men's": TEXAS_TECH_RED_RAIDERS,
    "Kansas State Wildcats Men's": KANSAS_STATE_WILDCATS,
    "Miami (OH) RedHawks Men's": MIAMI_OH_REDHAWKS,
    "Northern Illinois Huskies Men's": NORTHERN_ILLINOIS_HUSKIES,
    "Evansville Purple Aces Men's": EVANSVILLE_PURPLE_ACES,
    "Northern Iowa Panthers Men's": NORTHERN_IOWA_PANTHERS,
    "UCF Knights Men's": UCF_KNIGHTS,
    "Arizona State Sun Devils Men's": ARIZONA_STATE_SUN_DEVILS,
    "Nevada Wolf Pack Men's": NEVADA_WOLF_PACK,
    "San Jose State Spartans Men's": SAN_JOSE_STATE_SPARTANS,
    "USC Trojans Men's": USC_TROJANS,
    "Xavier Musketeers Men's": XAVIER_MUSKETEERS,
    "Toledo Rockets Men's": TOLEDO_ROCKETS,
    "Buffalo Bulls Men's": BUFFALO_BULLS,
    "Bowling Green State Falcons Men's": BOWLING_GREEN_STATE_FALCONS,
    "Eastern Michigan Eagles Men's": EASTERN_MICHIGAN_EAGLES,
    "Central Michigan Chippewas Men's": CENTRAL_MICHIGAN_CHIPPEWAS,
    "North Texas Mean Green Men's": NORTH_TEXAS_MEAN_GREEN,
    "East Carolina Pirates Men's": EAST_CAROLINA_PIRATES,
    "Ball State Cardinals Men's": BALL_STATE_CARDINALS,
    "Louisville Cardinals Men's": LOUISVILLE_CARDINALS,
    "Syracuse Orange Men's": SYRACUSE_ORANGE,
    "Charlotte 49ers Men's": CHARLOTTE_49ERS,
    "Wichita State Shockers Men's": WICHITA_STATE_SHOCKERS,
    "Creighton Bluejays Men's": CREIGHTON_BLUEJAYS,
    "UTSA Roadrunners Men's": UTSA_ROADRUNNERS,
    "Rice Owls Men's": RICE_OWLS,
    "Little Rock Trojans Men's": LITTLE_ROCK_TROJANS,
    "Wyoming Cowboys Men's": WYOMING_COWBOYS,
    "Oklahoma State Cowboys Men's": OKLAHOMA_STATE_COWBOYS,
    "BYU Cougars Men's": BYU_COUGARS,
    "Clemson Tigers Men's": CLEMSON_TIGERS,
    "Georgia Tech Yellow Jackets Men's": GEORGIA_TECH_YELLOW_JACKETS,
    "Arkansas Razorbacks Men's": ARKANSAS_RAZORBACKS,
    "LSU Fighting Tigers Men's": LSU_FIGHTING_TIGERS,
    "Colorado State Rams Men's": COLORADO_STATE_RAMS,
    "San Diego State Aztecs Men's": SAN_DIEGO_STATE_AZTECS,
    "American Eagles Men's": AMERICAN_EAGLES,
    "Loyola (MD) Greyhounds Men's": LOYOLA_MD_GREYHOUNDS,
    "Alabama State Hornets Men's": ALABAMA_STATE_HORNETS,
    "Alcorn State Braves Men's": ALCORN_STATE_BRAVES,
    "Prairie View Panthers Men's": PRAIRIE_VIEW_PANTHERS,
    "Arkansas-Pine Bluff Golden Lions Men's": ARKANSAS_PINE_BLUFF_GOLDEN_LIONS,
    "Florida A&M Rattlers Men's": FLORIDA_AM_RATTLERS,
    "Grambling Tigers Men's": GRAMBLING_TIGERS,
    "Nicholls State Colonels Men's": NICHOLLS_STATE_COLONELS,
    "Incarnate Word Cardinals Men's": INCARNATE_WORD_CARDINALS,
    "Alabama A&M Bulldogs Men's": ALABAMA_AM_BULLDOGS,
    "Jackson State Tigers Men's": JACKSON_STATE_TIGERS,
    "Texas Southern Tigers Men's": TEXAS_SOUTHERN_TIGERS,
    "Mississippi Valley State Delta Devils Men's": MISSISSIPPI_VALLEY_STATE_DELTA_DEVILS,
    "Norfolk State Spartans Men's": NORFOLK_STATE_SPARTANS,
    "Morgan State Bears Men's": MORGAN_STATE_BEARS,
    "Delaware State Hornets Men's": DELAWARE_STATE_HORNETS,
    "North Carolina Central Eagles Men's": NORTH_CAROLINA_CENTRAL_EAGLES,
    "Boston College Eagles Men's": BOSTON_COLLEGE_EAGLES,
    "Notre Dame Fighting Irish Men's": NOTRE_DAME_FIGHTING_IRISH,
    "Maryland-Eastern Shore Hawks Men's": MARYLAND_EASTERN_SHORE_HAWKS,
    "South Carolina State Bulldogs Men's": SOUTH_CAROLINA_STATE_BULLDOGS,
    "Southeastern Louisiana Lions Men's": SOUTHEASTERN_LOUISIANA_LIONS,
    "Stephen F. Austin Lumberjacks Men's": STEPHEN_F_AUSTIN_LUMBERJACKS,
    "East Texas A&M Lions Men's": EAST_TEXAS_AM_LIONS,
    "Texas-Rio Grande Valley Vaqueros Men's": TEXAS_RIO_GRANDE_VALLEY_VAQUEROS,
    "McNeese State Cowboys Men's": MCNEESE_STATE_COWBOYS,
    "Houston Christian Huskies Men's": HOUSTON_CHRISTIAN_HUSKIES,
    "New Orleans Privateers Men's": NEW_ORLEANS_PRIVATEERS,
    "Lamar Cardinals Men's": LAMAR_CARDINALS,
    "Bethune-Cookman Wildcats Men's": BETHUNE_COOKMAN_WILDCATS,
    "Southern Jaguars Men's": SOUTHERN_JAGUARS,
    "Northwestern State Demons Men's": NORTHWESTERN_STATE_DEMONS,
    "Texas A&M-Corpus Christi Islanders Men's": TEXAS_AM_CORPUS_CHRISTI_ISLANDERS,
    "Oregon Ducks Men's": OREGON_DUCKS,
    "Manhattan Jaspers Men's": MANHATTAN_JASPERS,
    "LIU Sharks Men's": LIU_SHARKS,
    "Central Connecticut Blue Devils Men's": CENTRAL_CONNECTICUT_BLUE_DEVILS,
    "Saint Francis (PA) Red Flash Men's": SAINT_FRANCIS_PA_RED_FLASH,
    "FDU Knights Men's": FDU_KNIGHTS,
    "Stonehill Skyhawks Men's": STONEHILL_SKYHAWKS,
    "Chicago State Cougars Men's": CHICAGO_STATE_COUGARS,
    "Mercyhurst Lakers Men's": MERCYHURST_LAKERS,
    "Le Moyne Dolphins Men's": LE_MOYNE_DOLPHINS,
    "Tulsa Golden Hurricane Men's": TULSA_GOLDEN_HURRICANE,
    "UConn Huskies Men's": UCONN_HUSKIES,
    "Penn Quakers Men's": PENN_QUAKERS,
    "Dartmouth Big Green Men's": DARTMOUTH_BIG_GREEN,
    "UMass-Lowell River Hawks Men's": UMASS_LOWELL_RIVER_HAWKS,
    "Western Kentucky Hilltoppers Men's": WESTERN_KENTUCKY_HILLTOPPERS,
    "Saint Mary's Gaels Men's": SAINT_MARYS_GAELS,
    "Cornell Big Red Men's": CORNELL_BIG_RED,
    "Columbia Lions Men's": COLUMBIA_LIONS,
    "Princeton Tigers Men's": PRINCETON_TIGERS,
    "Harvard Crimson Men's": HARVARD_CRIMSON,
    "Presbyterian Blue Hose Men's": PRESBYTERIAN_BLUE_HOSE,
    "Brown Bears Men's": BROWN_BEARS,
    "Yale Bulldogs Men's": YALE_BULLDOGS,
    "Eastern Washington Eagles Men's": EASTERN_WASHINGTON_EAGLES,
    "Idaho Vandals Men's": IDAHO_VANDALS,
    "Middle Tennessee Blue Raiders Men's": MIDDLE_TENNESSEE_BLUE_RAIDERS,
    "Detroit Mercy Titans Men's": DETROIT_MERCY_TITANS,
    "Southern Utah Thunderbirds Men's": SOUTHERN_UTAH_THUNDERBIRDS,
    "St. Thomas Tommies Men's": ST_THOMAS_TOMMIES,
    "Cal State Bakersfield Roadrunners Men's": CAL_STATE_BAKERSFIELD_ROADRUNNERS,
    "Wagner Seahawks Men's": WAGNER_SEAHAWKS,
    # SportsDB
    "138501": FLORIDA_GATORS,
    "138705": HOUSTON_COUGARS,
    "138612": DUKE_BLUE_DEVILS,
    "138500": AUBURN_TIGERS,
    "138772": PURDUE_FORT_WAYNE_MASTODONS,
}
ALAMODOME = "19330"
NCAAB_VENUE_IDENTITY_MAP: dict[str, str] = {
    # SportsDB
    "19330": ALAMODOME,
}
NCAAB_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class NCAABCombinedLeagueModel(CombinedLeagueModel):
    """NCAAB combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.NCAAB,
            [
                NCAABESPNLeagueModel(session, position=0),
                NCAABOddsPortalLeagueModel(session, position=1),
                # NCAABSportsDBLeagueModel(session, position=2),
                # NCAABSportsReferenceLeagueModel(session, position=3),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return NCAAB_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return NCAAB_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return NCAAB_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "ncaab-combined-league-model"
