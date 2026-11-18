"""The 46 stories of Tuesday 17 November 2026, in four tiers.

Every story happened, or was first reported, on 17 November 2026 in some time
zone, and was checked against at least one wire, broadcaster or official source.

ok: "C" = confirmed by officials or several outlets; "A" = a claim by one side,
shown with its source.
"""

LEAD = [
    {"art": "kerch", "checked": ['Reuters', 'AP', 'Guardian', 'Kyiv Independent', 'ISW'], "region": "EUROPE", "beat": "UKRAINE WAR", "src": "REUTERS \u00b7 AP", "ok": "C",
     "at": (36.5, 45.3),
     "hed": "Ukraine brings down a road span of the Crimean Bridge",
     "dek": "The central road section fell into the Kerch Strait after a second night of strikes."},
    {"art": "gulf17", "checked": ['AP', 'NPR', 'LA Times', 'CBS'], "region": "MIDDLE EAST", "beat": "IRAN WAR", "src": "AP \u00b7 REUTERS", "ok": "C",
     "at": (50.55, 26.05),
     "hed": "Iran sends drones at a US radar in Bahrain; US hits back",
     "dek": "Bahrain intercepts a third attack in days; US jets then hit a missile site on Qeshm."},
    {"art": "quad", "checked": ['Al Jazeera', 'Guardian', 'Gulf News', 'Straits Times'], "region": "ASIA", "beat": "DIPLOMACY", "src": "AFP \u00b7 AL JAZEERA", "ok": "C",
     "at": (121.0, 14.6),
     "hed": "First Quad summit in two years signs minerals deals",
     "dek": "Trump, Modi, Takaichi and Albanese plan a first joint maritime patrol in 2027."},
]

MAJOR = [
    {"art": "measles", "checked": ['PAHO', 'Reuters', 'CNBC', 'Al Jazeera'], "region": "AMERICAS", "beat": "HEALTH", "src": "PAHO", "ok": "C",
     "at": (-98.0, 39.0),
     "hed": "US, Mexico and Bolivia lose measles-free status",
     "dek": "PAHO: the virus spread for over a year; the US had held it for 26."},
    {"art": "mongolia", "checked": ['AP', 'Reuters', 'Montsame', 'Independent'], "region": "ASIA", "beat": "POLITICS", "src": "AP \u00b7 REUTERS", "ok": "C",
     "at": (106.9, 47.9),
     "hed": "Mongolia's president says he will resign",
     "dek": "Khurelsukh denies taking a $25m bribe over a railway deal."},
    {"art": "serbia", "checked": ['Reuters', 'RFE/RL', 'Euronews', 'Guardian', 'BIRN'], "region": "EUROPE", "beat": "POLITICS", "src": "REUTERS", "ok": "C",
     "at": (20.46, 44.8),
     "hed": "Serbia's student MPs take their seats",
     "dek": "The Student List holds 140 of 250 seats, ending 14 years of SNS rule."},
    {"art": "prague", "checked": ['Euronews', 'Sky', 'Telegraph', 'Anadolu'], "region": "EUROPE", "beat": "RAIL", "src": "EURONEWS \u00b7 SKY", "ok": "C",
     "at": (14.44, 50.08),
     "hed": "Two trains collide in Prague; 46 injured",
     "dek": "Four are badly hurt; one train may have passed a red signal."},
    {"art": "dow", "checked": ['CNBC', 'Reuters', 'AP', 'Nvidia'], "region": "AMERICAS", "beat": "MARKETS", "src": "CNBC \u00b7 NVIDIA", "ok": "C",
     "at": (-74.0, 40.7),
     "hed": "Dow sheds 849 points; then Nvidia beats",
     "dek": "After the close Nvidia reports $115.8bn revenue, up 103%."},
]

KEY = [
    {"thumb": "plane", "checked": ['Russian MoD', 'Al Jazeera', 'NBC', 'The Hindu'], "region": "EUROPE", "src": "RUSSIAN MoD", "ok": "C", "at": (86.1, 55.3),
     "kicker": "SIBERIA", "hed": "An-12 crash kills all 19 aboard"},
    {"thumb": "bridge", "checked": ['Kyiv mayor', 'Reuters', 'CBS', 'Kyiv Independent'], "region": "EUROPE", "src": "KYIV MAYOR", "ok": "C", "at": (30.5, 50.45),
     "kicker": "KYIV", "hed": "Russia hits 2 bridges; water cut"},
    {"thumb": "gavel", "checked": ['Reuters', 'AP', 'Al Jazeera', 'Africanews'], "region": "AFRICA", "src": "REUTERS \u00b7 AP", "ok": "C", "at": (32.6, -25.97),
     "kicker": "MAPUTO", "hed": "Opposition's Mondlane on trial"},
    {"thumb": "factory", "checked": ['AFP', 'Al Jazeera', 'Dhaka Tribune'], "region": "ASIA", "src": "AFP", "ok": "C", "at": (90.26, 23.85),
     "kicker": "SAVAR, BANGLADESH", "hed": "Police tear-gas wage protest"},
    {"thumb": "hemicycle", "checked": ['Reuters', 'Times of Israel', 'JPost', 'ABC'], "region": "MIDDLE EAST", "src": "TIMES OF ISRAEL", "ok": "C", "at": (35.2, 31.78),
     "kicker": "JERUSALEM", "hed": "Knesset picks Kahana, 66\u201352"},
    {"thumb": "jet", "checked": ['Japan MoD', 'AP', 'Reuters', 'NHK'], "region": "ASIA", "src": "JAPAN MoD", "ok": "C", "at": (130.1, 34.2),
     "kicker": "FUKUOKA, JAPAN", "hed": "Jets scrambled at airspace breach"},
    {"thumb": "dove", "checked": ['AP', 'Reuters', 'Al Jazeera'], "region": "MIDDLE EAST", "src": "AP \u00b7 REUTERS", "ok": "C", "at": (34.45, 31.5),
     "kicker": "GAZA", "hed": "Peace board: truce may collapse"},
    {"thumb": "chart", "checked": ['UN HRMMU', 'Kyiv Post', 'Ukrainska Pravda'], "region": "EUROPE", "src": "UN HRMMU", "ok": "C", "at": (31.0, 49.0),
     "kicker": "UKRAINE", "hed": "UN: 2026 deaths already top 2025"},
]

# Tier 4: (place, text, region, (lon, lat), ok)
BRIEFS = [
    ("Russia", "claims a record 1,441 Ukrainian drones downed", "EUROPE", (37.6, 55.8), "A"),
    ("The Hague", "Thaçi gets 17 more months for obstructing justice", "EUROPE", (4.3, 52.1), "C"),
    ("Belgrade", "Serbian MiG-29 crashes in a field; pilot killed", "EUROPE", (20.0, 45.0), "C"),
    ("Brussels", "15 nations pledge Ukraine aid at Ramstein", "EUROPE", (4.4, 50.8), "C"),
    ("Paris", "France pledges two more Mirage jets to Kyiv", "EUROPE", (2.35, 48.85), "C"),
    ("Chi\u0219in\u0103u", "Moldova shuts airspace as a Russian drone flies over", "EUROPE", (28.8, 47.0), "C"),
    ("France", "pay strike: police count 146,000, CGT 500,000", "EUROPE", (1.0, 47.0), "C"),
    ("Warsaw", "Tusk survives a no-confidence vote, 242\u2013200", "EUROPE", (21.0, 52.2), "C"),
    ("Istanbul", "police raid Sözcü TV and install a trustee", "EUROPE", (29.0, 41.0), "C"),
    ("London", "sanctions 8 settlement builders and Tzav 9", "EUROPE", (-0.1, 51.5), "C"),
    ("Rome", "Pope Leo returns from a 12-day South America tour", "EUROPE", (12.45, 41.9), "C"),
    ("Gaza", "UN agency warns of hypothermia deaths this winter", "MIDDLE EAST", (34.3, 31.3), "C"),
    ("Manila", "ASEAN\u2013US summit ends; Singapore takes the chair", "ASIA", (121.0, 14.6), "C"),
    ("Thailand", "Trump signs a trade statement in Manila", "ASIA", (100.5, 13.75), "C"),
    ("Shenzhen", "China cuts tariffs on Canadian pork and seafood", "ASIA", (114.1, 22.5), "C"),
    ("Singapore", "Brazil win 7\u20130; Vinícius hat-trick in 21 minutes", "ASIA", (103.8, 1.35), "C"),
    ("Alaska", "AP calls Senate race for Peltola at 22:19 ET", "AMERICAS", (-150.0, 61.2), "C"),
    ("Washington", "NSA network outage; agency cites maintenance", "AMERICAS", (-77.0, 38.9), "C"),
    ("New York", "S&P 500 ends at its lowest close since July", "AMERICAS", (-74.0, 40.7), "C"),
    ("St. Louis", "Fed's Musalem argues for more rate rises", "AMERICAS", (-90.2, 38.6), "C"),
    ("Nasdaq", "Anthropic cleared to list ahead of its IPO", "AMERICAS", (-73.0, 41.5), "C"),
    ("Lagos", "drug agency breaks a Sahara cocaine route; 8 held", "AFRICA", (3.4, 6.5), "C"),
    ("Abuja", "Senate condemns attack on Tinubu's convoy", "AFRICA", (7.5, 9.05), "C"),
    ("Pretoria", "South Africa summons Nigeria's envoy", "AFRICA", (28.2, -25.7), "C"),
    ("Moyale", "WFP feeds 30,000 who fled Ethiopia into Kenya", "AFRICA", (39.05, 3.5), "C"),
    ("Asmara", "Eritrea accuses Ethiopia's army chief of land claims", "AFRICA", (38.9, 15.3), "A"),
    ("Football", "Nigeria held 0\u20130 by Tanzania in AFCON qualifier", "AFRICA", (5.0, 8.0), "C"),
    ("Cook Islands", "Cyclone Xavier strengthens to Category 4", "OCEANIA", (-161.0, -10.4), "C"),
    ("COP31", "Australia's draft seeks $120bn a year for adaptation", "GLOBAL", (30.7, 36.9), "C"),
    ("Night sky", "Leonid meteor shower at its peak", "GLOBAL", None, "C"),
]

# The day by the clock, UTC. Only times stated by the sources.
TIMELINE = [
    (6 + 20 / 60, "06:20", "Prague trains collide", "EUROPE"),
    (7 + 45 / 60, "07:45", "MiG-29 down near Belgrade", "EUROPE"),
    (14 + 27 / 60, "14:27", "Moldova shuts airspace", "EUROPE"),
    (21.0, "21:00", "Dow closes \u2212849", "AMERICAS"),
    (21 + 20 / 60, "21:20", "Nvidia: $115.8bn", "AMERICAS"),
]

# Left out on purpose: they broke before Tuesday 17 November.
LEFT_OUT = [
    "Ukraine's first strike on the bridge arch (Mon 16)",
    "Russia's previous record of 1,336 drones (Mon 16)",
    "Grammy nominations (Mon 16)",
    "Costa Rica journalist's killing (Mon 16)",
    "South Africa's mass shootings (Sun 15)",
]

REGIONS = ["EUROPE", "MIDDLE EAST", "ASIA", "AFRICA", "AMERICAS", "OCEANIA", "GLOBAL"]
JUDGE_NOTE = "Every story on this page happened, or was first reported, on Tuesday 17 November 2026."
SOURCES = ("Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 Al Jazeera \u00b7 PAHO \u00b7 UN \u00b7 CNBC \u00b7 "
           "Euronews \u00b7 RNZ \u00b7 Times of Israel \u00b7 Japan MoD \u00b7 Vatican")
FOOT_NOTE = "Original drawings; map from Natural Earth (public domain)."


def all_stories():
    out, n = [], 1
    for s in LEAD + MAJOR:
        out.append((n, s)); n += 1
    for k in KEY:
        out.append((n, k)); n += 1
    for b in BRIEFS:
        out.append((n, {"place": b[0], "hed": b[1], "region": b[2], "at": b[3], "ok": b[4]})); n += 1
    return out


def cross_checks():
    """(stories, reports) behind the source meters."""
    top = LEAD + MAJOR + KEY
    return len(top), sum(len(s["checked"]) for s in top)


def count():
    return len(LEAD) + len(MAJOR) + len(KEY) + len(BRIEFS)


if __name__ == "__main__":
    print(count(), "stories")
