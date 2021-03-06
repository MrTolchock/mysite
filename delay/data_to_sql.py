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


# Initiate stats
results_received = js["nhits"]
empty_fields = 0


# Connect to Django SQL DB
path = "../db.sqlite3"
conn = sqlite3.connect(path)
cur = conn.cursor()


# Save and write data

# Define all items
items = ["fahrt_bezeichner", "bpuic", "haltestellen_name", "linien_text", "betriebstag", "ankunftszeit", "an_prognose", "an_prognose_status", "abfahrtszeit", "ab_prognose", "ab_prognose_status", "faellt_aus_tf"]

# Define time zone function
def tzone(utc_dt):
    return utc_dt.astimezone(timezone("Europe/Zurich"))

# Save all items to list and SQL
for train in js["records"]:

    # Save data to list and prepare
    info = list()

    for item in items:
        infoline = train["fields"].get(item)

        # Count skipped fields
        if infoline==None:
            empty_fields = empty_fields + 1
            info.append(infoline)
            continue

        # Adjust date time fields
        if item in ["ankunftszeit", "an_prognose", "abfahrtszeit", "ab_prognose"]:
            infoline = datetime.strptime(str(infoline), "%Y-%m-%dT%H:%M:%S")
            infoline = tzone(infoline)

        if item in ["betriebstag"]:
            infoline = datetime.strptime(str(infoline), "%Y-%m-%d")
            infoline = tzone(infoline)

        # Turn faellt aus into integer
        if item in ["faellt_aus_tf"]:
            if infoline == "false":
                infoline = 0
            else:
                infoline = 1

        info.append(infoline)

    # Calculate delay
    try:
        if info[9] is None or info[8] is None:
            ab_delay = None
            print("Input <", info[9], "-", info[8], "> could not be computed. Delay left empty.")
        else:
            ab_diff = info[9] - info[8]
            ab_delay = int(ab_diff.total_seconds())
    except:
        ab_delay = None
        print("Input <", info[9], "-", info[8], "> could not be computed. Delay left empty.")

    info.append(ab_delay)


    # Create unique ID as an integer
    uid = str(train["fields"]["fahrt_bezeichner"]) + str(train["fields"]["betriebstag"])
    uid = uid.replace("85:11:", "")
    uid = uid.replace(":00", "")
    uid = uid.replace("-", "")
    uid = int(uid)
    info.append(uid)


    #print(info, len(info))
    cur.execute("INSERT OR REPLACE INTO delay_train VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)

    conn.commit()

print(conn.total_changes, "of", results_received, " results imported.", empty_fields, "empty fields.")

cur.close()
