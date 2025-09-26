"""WNBA combined league model."""

# pylint: disable=line-too-long
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.wnba_espn_league_model import WNBAESPNLeagueModel
from ..oddsportal.wnba_oddsportal_league_model import WNBAOddsPortalLeagueModel

MERCURY = "11"
LIBERTY = "9"
MYSTICS = "16"
ROCKERS = "2"
MONARCHS = "13"
SPARKS = "6"
COMETS = "4"
STARZZ = "15"
LYNX = "8"
STING = "1"
MIRACLE = "10"
SHOCK = "3"
SOL = "7"
STORM = "14"
FIRE = "12"
FEVER = "5"
WEST = "99"
EAST = "98"
SUN = "18"
SILVER_STARS = "17"
TEAM_USA = "97"
TEAM_WNBA = "96"
SKY = "19"
DREAM = "20"
TEAM_CHINA = "21"
TEAM_POLAND = "22"
TEAM_GREAT_BRITAIN = "24"
JX_SUNFLOWERS = "23"
TEAM_JAPAN = "25"
TEAM_BRAZIL = "17473"
TEAM_AUSTRALIA = "17472"
WNBA_TEAM_IDENTITY_MAP: dict[str, str] = {
    # ESPN
    "11": MERCURY,
    "9": LIBERTY,
    "16": MYSTICS,
    "2": ROCKERS,
    "13": MONARCHS,
    "6": SPARKS,
    "4": COMETS,
    "15": STARZZ,
    "8": LYNX,
    "1": STING,
    "10": MIRACLE,
    "3": SHOCK,
    "7": SOL,
    "14": STORM,
    "12": FIRE,
    "5": FEVER,
    "99": WEST,
    "98": EAST,
    "18": SUN,
    "17": SILVER_STARS,
    "97": TEAM_USA,
    "96": TEAM_WNBA,
    "19": SKY,
    "20": DREAM,
    "21": TEAM_CHINA,
    "22": TEAM_POLAND,
    "24": TEAM_GREAT_BRITAIN,
    "23": JX_SUNFLOWERS,
    "25": TEAM_JAPAN,
    # OddsPortal
    "17473": TEAM_BRAZIL,
    "17475": TEAM_JAPAN,
    "17472": TEAM_AUSTRALIA,
}
MADISON_SQUARE_GARDEN = "1830"
CAPITAL_ONE_ARENA = "1823"
QUICKEN_LOANS_ARENA = "3417"
CRYPTO_COM_ARENA = "1841"
TARGET_CENTER = "2029"
THE_PALACE_OF_AUBURN_HILLS = "3419"
KEY_ARENA = "2184"
AMERICAN_AIRLINES_ARENA = "3438"
PHX_ARENA = "1949"
ROSE_GARDEN = "3423"
MOHEGAN_SUN_ARENA = "2160"
FROST_BANK_CENTER = "780"
PRUDENTIAL_CENTER = "1826"
BOK_CENTER = "1911"
GAINBRIDGE_FIELDHOUSE = "2183"
STATE_FARM_ARENA = "1827"
ALLSTATE_ARENA = "977"
THE_ARENA_AT_GWINNETT_CENTER = "1245"
JACOBY_DICKENS_CENTER = "4332"
WALTER_PYRAMID = "539"
SRC_ARENA = "2082"
BISMARCK_EVENT_CENTER = "3446"
MCCAMISH_PAVILION = "2206"
HP_FIELD_HOUSE = "2222"
LAKIN_CENTER = "3500"
BOB_CARPENTER_CENTER = "2189"
FREEMAN_COLISEUM = "2935"
WNBA_VENUE_IDENTITY_MAP: dict[str, str] = {
    # ESPN
    "1830": MADISON_SQUARE_GARDEN,
    "1823": CAPITAL_ONE_ARENA,
    "3417": QUICKEN_LOANS_ARENA,
    "1841": CRYPTO_COM_ARENA,
    "2029": TARGET_CENTER,
    "3419": THE_PALACE_OF_AUBURN_HILLS,
    "2184": KEY_ARENA,
    "3438": AMERICAN_AIRLINES_ARENA,
    "1949": PHX_ARENA,
    "3423": ROSE_GARDEN,
    "2160": MOHEGAN_SUN_ARENA,
    "780": FROST_BANK_CENTER,
    "1826": PRUDENTIAL_CENTER,
    "1911": BOK_CENTER,
    "2183": GAINBRIDGE_FIELDHOUSE,
    "1827": STATE_FARM_ARENA,
    "977": ALLSTATE_ARENA,
    "1245": THE_ARENA_AT_GWINNETT_CENTER,
    "4332": JACOBY_DICKENS_CENTER,
    "539": WALTER_PYRAMID,
    "2082": SRC_ARENA,
    "3446": BISMARCK_EVENT_CENTER,
    "2206": MCCAMISH_PAVILION,
    "2222": HP_FIELD_HOUSE,
    "3500": LAKIN_CENTER,
    "2189": BOB_CARPENTER_CENTER,
    "2935": FREEMAN_COLISEUM,
}
WNBA_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class WNBACombinedLeagueModel(CombinedLeagueModel):
    """WNBA combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.WNBA,
            [
                WNBAESPNLeagueModel(session, position=0),
                WNBAOddsPortalLeagueModel(session, position=1),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return WNBA_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return WNBA_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return WNBA_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "wnba-combined-league-model"
