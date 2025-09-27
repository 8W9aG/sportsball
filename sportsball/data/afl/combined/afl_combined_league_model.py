"""AFL combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..afl.afl_afl_league_model import AFLAFLLeagueModel
from ..afltables.afl_afltables_league_model import AFLAFLTablesLeagueModel
from ..aussportsbetting.afl_aussportsbetting_league_model import \
    AFLAusSportsBettingLeagueModel
from ..espn.afl_espn_league_model import AFLESPNLeagueModel
from ..oddsportal.afl_oddsportal_league_model import AFLOddsPortalLeagueModel

FITZROY = "fitzroy_idx"
CARLTON = "carlton_idx"
COLLINGWOOD = "collingwood_idx"
STKILDA = "stkilda_idx"
GEELONG = "geelong_idx"
ESSENDON = "essendon_idx"
SWANS = "swans_idx"
MELBOURNE = "melbourne_idx"
UNIVERSITY = "university_idx"
RICHMOND = "richmond_idx"
BULLDOGS = "bullldogs_idx"
KANGAROOS = "kangaroos_idx"
HAWTHORN = "hawthorn_idx"
BRISBANE = "brisbaneb_idx"
WESTCOAST = "westcoast_idx"
ADELAIDE = "adelaide_idx"
FREMANTLE = "fremantle_idx"
BRISBANE_LIONS = "brisbanel_idx"
PORT_ADELAIDE = "padelaide_idx"
GWS = "gws_idx"
GOLDCOAST = "goldcoast_idx"
AFL_TEAM_IDENTITY_MAP = {
    "fitzroy_idx": FITZROY,
    "carlton_idx": CARLTON,
    "collingwood_idx": COLLINGWOOD,
    "stkilda_idx": STKILDA,
    "geelong_idx": GEELONG,
    "essendon_idx": ESSENDON,
    "swans_idx": SWANS,
    "melbourne_idx": MELBOURNE,
    "university_idx": UNIVERSITY,
    "richmond_idx": RICHMOND,
    "bullldogs_idx": BULLDOGS,
    "kangaroos_idx": KANGAROOS,
    "hawthorn_idx": HAWTHORN,
    "brisbaneb_idx": BRISBANE,
    "westcoast_idx": WESTCOAST,
    "adelaide_idx": ADELAIDE,
    "fremantle_idx": FREMANTLE,
    "brisbanel_idx": BRISBANE_LIONS,
    "padelaide_idx": PORT_ADELAIDE,
    "gws_idx": GWS,
    "goldcoast_idx": GOLDCOAST,
    "Sydney": SWANS,
    "Brisbane": BRISBANE_LIONS,
    "Geelong": GEELONG,
    "Port Adelaide": PORT_ADELAIDE,
    "GWS Giants": GWS,
    "Hawthorn": HAWTHORN,
    "Carlton": CARLTON,
    "Western Bulldogs": BULLDOGS,
    "Fremantle": FREMANTLE,
    "St Kilda": STKILDA,
    "Adelaide": ADELAIDE,
    "Essendon": ESSENDON,
    "Richmond": RICHMOND,
    "Gold Coast": GOLDCOAST,
    "West Coast": WESTCOAST,
    "North Melbourne": KANGAROOS,
    "Melbourne": MELBOURNE,
    "Collingwood": COLLINGWOOD,
    # OddsPortal
    "Collingwood Magpies": COLLINGWOOD,
    "Port Adelaide Power": PORT_ADELAIDE,
    "Richmond Tigers": RICHMOND,
    "Carlton Blues": CARLTON,
    "Hawthorn Hawks": HAWTHORN,
    "Essendon Bombers": ESSENDON,
    "Sydney Swans": SWANS,
    "Adelaide Crows": ADELAIDE,
    "St Kilda Saints": STKILDA,
    "Brisbane Lions": BRISBANE_LIONS,
    "Melbourne Demons": MELBOURNE,
    "Geelong Cats": GEELONG,
    "Fremantle Dockers": FREMANTLE,
    "West Coast Eagles": WESTCOAST,
    "Gold Coast Suns": GOLDCOAST,
    # AFL
    "GWS GIANTS": GWS,
    "Gold Coast SUNS": GOLDCOAST,
    "Kuwarna": ADELAIDE,
    "Yartapuulti": PORT_ADELAIDE,
    "Walyalup": FREMANTLE,
    "Narrm": MELBOURNE,
    "Waalitj Marawar": WESTCOAST,
    "Euro-Yroke": STKILDA,
    # ESPN
    "8": GWS,
    "15": ADELAIDE,
    "3": WESTCOAST,
    "7": PORT_ADELAIDE,
    "16": ESSENDON,
    "4": SWANS,
    "12": RICHMOND,
    "14": GEELONG,
    "17": COLLINGWOOD,
    "13": HAWTHORN,
    "10": GOLDCOAST,
    "1": FREMANTLE,
    "5": KANGAROOS,
    "6": BULLDOGS,
    "11": BRISBANE_LIONS,
    "9": CARLTON,
    "2": MELBOURNE,
    "18": STKILDA,
}
BRUNSWICK_ST = "brunswick_st"
VICTORIA_PARK = "victoria_park"
CORIO_OVAL = "corio_oval"
LAKE_OVAL = "lake_oval"
EAST_MELBOURNE = "east_melbourne"
JUNCTION_OVAL = "junction_oval"
MCG = "mcg"
PRINCES_PARK = "princes_park"
SCG = "scg"
PUNT_RD = "punt_rd"
WINDY_HILL = "windy_hill"
GLENFERRIE_OVAL = "glenferrie_oval"
ARDEN_ST = "arden_st"
WESTERN_OVAL = "western_oval"
OLYMPIC_PARK = "olympic_park"
KARDINIA_PARK = "kardinia_park"
YARRAVILLE_OVAL = "yarraville_oval"
TOORAK_PARK = "toorak_park"
EUROA = "euroa"
NORTH_HOBART = "north_hobart"
YALLOURN = "yallourn"
ALBURY = "albury"
BRISBANE_EXHIBITION = "brisbane_exhibition"
MOORABBIN_OVAL = "moorabbin_oval"
COBURG_OVAL = "coburg_oval"
WAVERLEY_PARK = "waverley_park"
SUBIACO = "subiaco"
GABBA = "gabba"
CARRARA = "carrara"
WACA = "waca"
FOOTBALL_PARK = "football_park"
MANUKA_OVAL = "manuka_oval"
DOCKLANDS = "docklands"
STADIUM_AUSTRALIA = "stadium_australia"
YORK_PARK = "york_park"
SHOWGROUND = "showground"
MARRARA_OVAL = "marrara_oval"
CAZALYS_STADIUM = "cazalys_stadium"
ADELAIDE_OVAL = "adelaide_oval"
WELLINGTON = "wrs"
BELLERIVE_OVAL = "bellerive_oval"
TRAEGER = "traeger"
JIANGWAN = "jiangwan"
EUREKA = "eureka"
PERTH = "perth"
BRUCE_STADIUM = "bruce_stadium"
BLACKTOWN = "blacktown"
RIVERWAY = "riverway"
NORWOOD = "norwood"
SUMMIT = "summit"
ANGEL_STADIUM = "Angel Stadium of Anaheim"
THUNDERDOME_STADIUM = "Thunderdome Stadium"
SPOTLAND_STADIUM = "Spotland Stadium"
GIANTS_STADIUM = "Giants Stadium"
TIPOS_ARENA = "Ondrej Nepela Arena"
BAROSSA_PARK = "Barossa Park"
HANDS_OVAL = "Hands Oval, Bunbury"
AFL_VENUE_IDENTITY_MAP = {
    "brunswick_st": BRUNSWICK_ST,
    "victoria_park": VICTORIA_PARK,
    "corio_oval": CORIO_OVAL,
    "lake_oval": LAKE_OVAL,
    "east_melbourne": EAST_MELBOURNE,
    "junction_oval": JUNCTION_OVAL,
    "mcg": MCG,
    "princes_park": PRINCES_PARK,
    "scg": SCG,
    "punt_rd": PUNT_RD,
    "windy_hill": WINDY_HILL,
    "glenferrie_oval": GLENFERRIE_OVAL,
    "arden_st": ARDEN_ST,
    "western_oval": WESTERN_OVAL,
    "olympic_park": OLYMPIC_PARK,
    "kardinia_park": KARDINIA_PARK,
    "yarraville_oval": YARRAVILLE_OVAL,
    "toorak_park": TOORAK_PARK,
    "euroa": EUROA,
    "north_hobart": NORTH_HOBART,
    "yallourn": YALLOURN,
    "albury": ALBURY,
    "brisbane_exhibition": BRISBANE_EXHIBITION,
    "moorabbin_oval": MOORABBIN_OVAL,
    "coburg_oval": COBURG_OVAL,
    "waverley_park": WAVERLEY_PARK,
    "subiaco": SUBIACO,
    "gabba": GABBA,
    "carrara": CARRARA,
    "waca": WACA,
    "football_park": FOOTBALL_PARK,
    "manuka_oval": MANUKA_OVAL,
    "docklands": DOCKLANDS,
    "stadium_australia": STADIUM_AUSTRALIA,
    "york_park": YORK_PARK,
    "showground": SHOWGROUND,
    "marrara_oval": MARRARA_OVAL,
    "cazalys_stadium": CAZALYS_STADIUM,
    "adelaide_oval": ADELAIDE_OVAL,
    "wrs": WELLINGTON,
    "bellerive_oval": BELLERIVE_OVAL,
    "traeger": TRAEGER,
    "jiangwan": JIANGWAN,
    "eureka": EUREKA,
    "perth": PERTH,
    "bruce_stadium": BRUCE_STADIUM,
    "blacktown": BLACKTOWN,
    "riverway": RIVERWAY,
    "norwood": NORWOOD,
    "summit": SUMMIT,
    "barossa": BAROSSA_PARK,
    "hands": HANDS_OVAL,
    # Aus Sports Betting
    "MCG": MCG,
    "SCG": SCG,
    "ENGIE Stadium": STADIUM_AUSTRALIA,
    "Adelaide Oval": ADELAIDE_OVAL,
    "Gabba": GABBA,
    "Optus Stadium": PERTH,
    "Marvel Stadium": DOCKLANDS,
    "Mars Stadium": EUREKA,
    "GMHBA Stadium": KARDINIA_PARK,
    "UTAS Stadium": YORK_PARK,
    "People First Stadium": CARRARA,
    "Blundstone Arena": BELLERIVE_OVAL,
    "Manuka Oval": MANUKA_OVAL,
    "Norwood Oval": NORWOOD,
    "Adelaide Hills": SUMMIT,
    "TIO Stadium": MARRARA_OVAL,
    "Traeger Park": TRAEGER,
    "Cazaly’s Stadium": CAZALYS_STADIUM,
    "Marvl": DOCKLANDS,
    "Accor Stadium": STADIUM_AUSTRALIA,
    "Riverway Stadium": RIVERWAY,
    "Jiangwan Sports Centre": JIANGWAN,
    "Domain Stadium": SUBIACO,
    "Westpac Stadium": WELLINGTON,
    "AAMI Stadium": FOOTBALL_PARK,
    "Blacktown Park": BLACKTOWN,
    # OddsPortal
    "Melbourne Cricket Ground": MCG,
    "Angel Stadium of Anaheim": ANGEL_STADIUM,
    "The Gabba": GABBA,
    "Sydney Cricket Ground": SCG,
    "Subiaco Oval": SUBIACO,
    "Thunderdome Stadium": THUNDERDOME_STADIUM,
    "University of Tasmania Stadium": YORK_PARK,
    "Spotland Stadium": SPOTLAND_STADIUM,
    "Engie Stadium": STADIUM_AUSTRALIA,
    "Cazaly's Stadium": CAZALYS_STADIUM,
    "Jiangwan Stadium": JIANGWAN,
    "TIO Traeger Park": TRAEGER,
    "Marrara Oval": MARRARA_OVAL,
    "Giants Stadium": GIANTS_STADIUM,
    "Ondrej Nepela Arena": TIPOS_ARENA,
    "Barossa Park": BAROSSA_PARK,
    "Ninja Stadium": BELLERIVE_OVAL,
    # AFL
    "TIO Stadium, Darwin": MARRARA_OVAL,
    "SCG, Sydney": SCG,
    "MCG, Melbourne": MCG,
    "Adelaide Oval, Adelaide": ADELAIDE_OVAL,
    "ENGIE Stadium, Sydney": STADIUM_AUSTRALIA,
    "Marvel Stadium, Melbourne": DOCKLANDS,
    "Gabba, Brisbane": GABBA,
    "Optus Stadium, Perth": PERTH,
    "GMHBA Stadium, Geelong": KARDINIA_PARK,
    "People First Stadium, Gold Coast": CARRARA,
    "TIO Traeger Park, Alice Springs": TRAEGER,
    "Corroboree Group Oval Manuka, Canberra": MANUKA_OVAL,
    "Hands Oval, Bunbury": HANDS_OVAL,
    "Hands Oval - Australia": HANDS_OVAL,
    "UTAS Stadium, Launceston": YORK_PARK,
    "Hands Oval": HANDS_OVAL,
    "University of Tasmania Stadium, Launceston": YORK_PARK,
    "Ninja Stadium, Hobart": BELLERIVE_OVAL,
    # ESPN
    "6": ADELAIDE_OVAL,
    "10": STADIUM_AUSTRALIA,
    "7": SCG,
    "1": MCG,
    "2": SUBIACO,
    "3": DOCKLANDS,
    "5": GABBA,
    "4": MANUKA_OVAL,
    "9": YORK_PARK,
}


class AFLCombinedLeagueModel(CombinedLeagueModel):
    """AFL combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.AFL,
            [
                AFLAFLTablesLeagueModel(session, position=0),
                AFLESPNLeagueModel(session, position=1),
                AFLAusSportsBettingLeagueModel(session, position=2),
                AFLOddsPortalLeagueModel(session, position=3),
                AFLAFLLeagueModel(session, position=4),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return AFL_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return AFL_VENUE_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "afl-combined-league-model"
