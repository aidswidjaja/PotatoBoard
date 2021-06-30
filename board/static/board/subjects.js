var SUBJECT_ROLE_IDS = {
    "OTH": "NULL",
    "MET": "NULL",
    "WKS": "700120714811801631",
    "ENS": "807811981238861844",
    "ENA": "807811751750926356",
    "EN1": "807812013870415912",
    "EN2": "NULL",
    "MAS": "807812111190327306",
    "MAT": "807812159693783061",
    "MA1": "807812213955362816",
    "MA2": "807812213975810089",
    "BIO": "807812213980790784",
    "CHE": "807812222587502604",
    "PHY": "807812778424664095",
    "INS": "807812623634661387",
    "ENG": "807813063990181919",
    "SIC": "807812876916097024",
    "SOR": "807812817059053568",
    "SRX": "807812849644732426",
    "ECO": "807812429911687178",
    "BUS": "807812219693694976",
    "LST": "807812704453525504",
    "HIA": "807812512115327007",
    "HIM": "807812603740160010",
    "GEO": "807812512032096266",
    "PDH": "807812758061318225",
    "DRA": "807812222943887410",
    "VAR": "807812797332717578",
    "MU1": "807812726704439309",
    "MU2": "807812741946540093",
    "FRE": "807812452079108096",
    "LAT": "807812675413082173",
    "JAP": "807812651211816990"
}

/*

Making Discord role pings work with a key:pair dictionary that corresponds to role IDs. Role IDs are stored as strings.

PotatoBoard dictates a Field.choices as a list iterable consisting of exactly two items
  
    {A: "B", P: "Q", X: "Y"}

see https://docs.djangoproject.com/en/1.8/ref/models/fields/#choices for more info.

*/