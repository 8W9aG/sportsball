"""EPL combined league model."""

# pylint: disable=line-too-long
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.epl_espn_league_model import EPLESPNLeagueModel
from ..footballdata.epl_footballdata_league_model import \
    EPLFootballDataLeagueModel
from ..oddsportal.epl_oddsportal_league_model import EPLOddsPortalLeagueModel

BOLTON_WANDERERS = "358"
WEST_HAM_UNITED = "371"
DERBY_COUNTY = "374"
SUNDERLAND = "366"
NEWCASTLE_UNITED = "361"
SOUTHAMPTON = "376"
CHARLTON_ATHLETIC = "372"
MANCHESTER_UNITED = "360"
IPSWICH_TOWN = "373"
LIVERPOOL = "364"
TOTTENHAM_HOTSPUR = "367"
LEICESTER_CITY = "375"
MIDDLESBOROUGH = "369"
LEEDS_UNITED = "357"
ASTON_VILLA = "362"
CHELSEA = "363"
FULHAM = "370"
BLACKBURN_ROVERS = "365"
EVERTON = "368"
ARSENAL = "359"
BRENTFORD = "Brentford"
NOTTINGHAM_FOREST = "Nott'm Forest"
BRIGHTON = "Brighton"
CRYSTAL_PALACE = "Crystal Palace"
BOURNEMOUTH = "Bournemouth"
WOLVES = "Wolves"
BURNLEY = "379"
MANCHESTER_CITY = "382"
SHEFFIELD_UNITED = "398"
LUTON_TOWN = "301"
NORWICH_CITY = "381"
WATFORD = "395"
EPL_TEAM_IDENTITY_MAP: dict[str, str] = {
    # ESPN
    "358": BOLTON_WANDERERS,
    "371": WEST_HAM_UNITED,
    "374": DERBY_COUNTY,
    "366": SUNDERLAND,
    "361": NEWCASTLE_UNITED,
    "376": SOUTHAMPTON,
    "372": CHARLTON_ATHLETIC,
    "360": MANCHESTER_UNITED,
    "373": IPSWICH_TOWN,
    "364": LIVERPOOL,
    "367": TOTTENHAM_HOTSPUR,
    "375": LEICESTER_CITY,
    "369": MIDDLESBOROUGH,
    "357": LEEDS_UNITED,
    "362": ASTON_VILLA,
    "363": CHELSEA,
    "370": FULHAM,
    "365": BLACKBURN_ROVERS,
    "368": EVERTON,
    "359": ARSENAL,
    "380": WOLVES,
    "393": NOTTINGHAM_FOREST,
    "379": BURNLEY,
    "382": MANCHESTER_CITY,
    "349": BOURNEMOUTH,
    "384": CRYSTAL_PALACE,
    "331": BRIGHTON,
    "337": BRENTFORD,
    "398": SHEFFIELD_UNITED,
    "301": LUTON_TOWN,
    "381": NORWICH_CITY,
    "395": WATFORD,
    # FootballData
    "Brentford": BRENTFORD,
    "Arsenal": ARSENAL,
    "Aston Villa": ASTON_VILLA,
    "Southampton": SOUTHAMPTON,
    "Everton": EVERTON,
    "Nott'm Forest": NOTTINGHAM_FOREST,
    "Leicester": LEICESTER_CITY,
    "Brighton": BRIGHTON,
    "Crystal Palace": CRYSTAL_PALACE,
    "Man City": MANCHESTER_CITY,
    "Liverpool": LIVERPOOL,
    "Tottenham": TOTTENHAM_HOTSPUR,
    "West Ham": WEST_HAM_UNITED,
    "Chelsea": CHELSEA,
    "Newcastle": NEWCASTLE_UNITED,
    "Bournemouth": BOURNEMOUTH,
    "Wolves": WOLVES,
    "Ipswich": IPSWICH_TOWN,
    "Fulham": FULHAM,
}
BOLEYN_GROUND = "304"
STADIUM_OF_LIGHT = "194"
ST_MARYS_STADIUM = "303"
OLD_TRAFFORD = "250"
ANFIELD = "192"
FILBERT_STREET = "191"
ELLAND_ROAD = "190"
STAMFORD_BRIDGE = "249"
EWOOD_PARK = "280"
HIGHBURY = "267"
PORTMAN_ROAD = "257"
WHITE_HART_LANE = "195"
THE_RIVERSIDE_STADIUM = "193"
PRIDE_PARK_STADIUM = "189"
VILLA_PARK = "307"
CRAVEN_COTTAGE = "279"
THE_VALLEY = "188"
ST_JAMES_PARK = "308"
TOUGHSHEET_COMMUNITY_STADIUM = "256"
GOODISON_PARK = "253"
TOTTENHAM_HOTSPUR_STADIUM = "7827"
ETIHAD_STADIUM = "4036"
SELHURT_PARK = "135"
GTECH_COMMUNITY_STADIUM = "8480"
EMIRATES_STADIUM = "2267"
VITALITY_STADIUM = "6020"
MOLINEUX_STADIUM = "136"
LONDON_STADIUM = "6660"
TURF_MOOR = "197"
AMERICAN_EXPRESS_STADIUM = "4440"
THE_CITY_GROUND = "131"
KING_POWER_STADIUM = "5774"
BRAMALL_LANE = "6291"
KENILWORTH_ROAD = "3336"
EPL_VENUE_IDENTITY_MAP: dict[str, str] = {
    # ESPN
    "304": BOLEYN_GROUND,
    "194": STADIUM_OF_LIGHT,
    "303": ST_MARYS_STADIUM,
    "250": OLD_TRAFFORD,
    "192": ANFIELD,
    "191": FILBERT_STREET,
    "190": ELLAND_ROAD,
    "249": STAMFORD_BRIDGE,
    "280": EWOOD_PARK,
    "267": HIGHBURY,
    "257": PORTMAN_ROAD,
    "195": WHITE_HART_LANE,
    "193": THE_RIVERSIDE_STADIUM,
    "189": PRIDE_PARK_STADIUM,
    "307": VILLA_PARK,
    "279": CRAVEN_COTTAGE,
    "188": THE_VALLEY,
    "308": ST_JAMES_PARK,
    "256": TOUGHSHEET_COMMUNITY_STADIUM,
    "253": GOODISON_PARK,
    "135": SELHURT_PARK,
    "136": MOLINEUX_STADIUM,
    "197": TURF_MOOR,
    "131": THE_CITY_GROUND,
    # OddsPortal
    "6660": LONDON_STADIUM,
    "4440": AMERICAN_EXPRESS_STADIUM,
    "8480": GTECH_COMMUNITY_STADIUM,
    "2267": EMIRATES_STADIUM,
    "6020": VITALITY_STADIUM,
    "4684": ST_JAMES_PARK,
    "7827": TOTTENHAM_HOTSPUR_STADIUM,
    "4036": ETIHAD_STADIUM,
    "4850": ST_MARYS_STADIUM,
    "5774": KING_POWER_STADIUM,
    "6291": BRAMALL_LANE,
    "3336": KENILWORTH_ROAD,
}
EPL_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class EPLCombinedLeagueModel(CombinedLeagueModel):
    """NBA combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.EPL,
            [
                EPLESPNLeagueModel(session, position=0),
                EPLOddsPortalLeagueModel(session, position=1),
                EPLFootballDataLeagueModel(session, position=2),
                # EPLSportsDBLeagueModel(session, position=3),
                # EPLSportsReferenceLeagueModel(session, position=4),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return EPL_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return EPL_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return EPL_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "epl-combined-league-model"
