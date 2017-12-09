import json
import urllib.request, urllib.parse, urllib.error
import ssl
from datetime import datetime
from pytz import timezone
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Load API data
#https://data.sbb.ch/explore/dataset/actual-data-sbb-previous-day/api/?timezone=Europe%2FZurich&refine.bpuic=8503011

url = "https://data.sbb.ch/api/records/1.0/search/?dataset=actual-data-sbb-previous-day&rows=1000&facet=linien_text&facet=faellt_aus_tf&facet=bpuic&facet=ankunftszeit&facet=an_prognose&facet=an_prognose_status&facet=ab_prognose_status&facet=abfahrtsverspatung&refine.bpuic=8503011"


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)
#print(json.dumps(js["records"], indent=4, sort_keys=True))


# Connect to Django SQL DB
path = "../db.sqlite3"
#path = "test.db"
conn = sqlite3.connect(path)
cur = conn.cursor()


# Save data into list and then to SQL
items = ["fahrt_bezeichner", "bpuic", "haltestellen_name", "linien_text", "betriebstag", "ankunftszeit", "an_prognose", "an_prognose_status", "abfahrtszeit", "ab_prognose", "ab_prognose_status", "faellt_aus_tf"]

def tzone(utc_dt):
    return utc_dt.astimezone(timezone("Europe/Zurich"))

for train in js["records"]:
    info = list()
    for item in items:

        if item in ["ankunftszeit", "an_prognose", "abfahrtszeit", "ab_prognose"]:
            train["fields"][item] = datetime.strptime(str(train["fields"][item]), "%Y-%m-%dT%H:%M:%S")
            train["fields"][item] = tzone(train["fields"][item])

        if item in ["betriebstag"]:
            train["fields"][item] = datetime.strptime(str(train["fields"][item]), "%Y-%m-%d")
            train["fields"][item] = tzone(train["fields"][item])

        info.append(train["fields"][item])

    ab_delay = train["fields"]["ab_prognose"] - train["fields"]["abfahrtszeit"]
    info.append(str(ab_delay))

    #print(info, len(info))

    cur.execute("INSERT OR IGNORE INTO history_train VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)

    conn.commit()

cur.close()
