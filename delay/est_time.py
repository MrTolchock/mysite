def sbbtrip():

    import requests
    from xml.etree import ElementTree as ET
    from datetime import datetime, timedelta
    from pytz import timezone
    import xml.dom.minidom
    #8503011 stands for Zuerich Wiedikon, 8503006 for Oerlikon
    #API key: 57c5dbbbf1fe4d000100001810cb98403acc476a9ef255a0dfac27da
    #Doumentation: https://opentransportdata.swiss/de/cookbook/triprequest/

    #request API with key in header
    url = "https://api.opentransportdata.swiss/trias"
    headers = {"content-type": "text/XML", "authorization": "57c5dbbbf1fe4d000100001810cb98403acc476a9ef255a0dfac27da"}

    #define and format time now
    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")

    #get data from API and inject string to request with %
    triprequest = """
    <Trias version="1.1" xmlns="http://www.vdv.de/trias" xmlns:siri="http://www.siri.org.uk/siri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <ServiceRequest>
            <siri:RequestTimestamp>2012-10-28T20:56:00Z</siri:RequestTimestamp>
            <siri:RequestorRef>SEUS</siri:RequestorRef>
            <RequestPayload>
                <TripRequest>
                    <Origin>
                        <LocationRef>
                            <StopPointRef>8503011</StopPointRef>
                        </LocationRef>
                        <DepArrTime>%s</DepArrTime>
                    </Origin>
                    <Destination>
                        <LocationRef>
                            <StopPointRef>8503006</StopPointRef>
                        </LocationRef>
                    </Destination>
                    <Params>
                        <NumberOfResults>7</NumberOfResults>
                        <IncludeTrackSections>false</IncludeTrackSections>
                        <IncludeLegProjection>true</IncludeLegProjection>
                        <IncludeIntermediateStops>false</IncludeIntermediateStops>
                    </Params>
                </TripRequest>
            </RequestPayload>
        </ServiceRequest>
    </Trias>
    """ % (str(now))

    #save xml response to variable "data" and pretty-print
    data = requests.post(url, headers=headers, data=triprequest)
    data.encoding = "utf-8"
    xml = xml.dom.minidom.parseString(data.text)
    pretty_xml_as_string = xml.toprettyxml()
    #print(pretty_xml_as_string)

    #read from XML tree
    tree = ET.fromstring(data.text)
    ns = {'ns': 'http://www.vdv.de/trias'}

    trips = list()
    tripinfo = dict()

    for trip in tree.findall(".//ns:TripResult", ns):
        for board in trip.findall(".//ns:LegBoard", ns):
            tripinfo["from"] = board.find("*/ns:Text", ns).text
            tripinfo["dep"] = board.find("*/ns:TimetabledTime", ns).text
            try:
                tripinfo["dep_est"] = board.find("*/ns:EstimatedTime", ns).text
            except:
                tripinfo["dep_est"] = tripinfo["dep"]
                print("-----no estimated departure-----")

        for alight in trip.findall(".//ns:LegAlight", ns):
            tripinfo["to"] = alight.find("*/ns:Text", ns).text
            tripinfo["arr"] = alight.find("*/ns:TimetabledTime", ns).text
            try:
                tripinfo["arr_est"] = alight.find("*/ns:EstimatedTime", ns).text
            except:
                tripinfo["arr_est"] = tripinfo["arr"]
                print("-----no estimated arrival-----")

        for service in trip.findall(".//ns:PublishedLineName", ns):
            tripinfo["line"] = "S" + service.find("./ns:Text", ns).text

        trips.append(tripinfo.copy())


    #adjust format of time values and time zone
    def tzone(utc_dt):
        return utc_dt.replace(tzinfo=timezone("UTC")).astimezone(timezone("Europe/Zurich"))

    for trip in trips:
        for element in ["dep", "dep_est", "arr", "arr_est"]:
            trip[element] = datetime.strptime(str(trip[element]), "%Y-%m-%dT%H:%M:%SZ")
            trip[element] = tzone(trip[element])


    #compute delay
    for trip in trips:
        trip["dep_delay"] = trip["dep_est"] - trip["dep"]
        trip["arr_delay"] = trip["arr_est"] - trip["arr"]


    #turn results to Django dictionary
    count = 0
    tripdic = dict()
    #now = datetime.now().astimezone(timezone("Europe/Zurich"))
    now = datetime.now()
    now = now.replace(tzinfo=timezone("Europe/Zurich"))

    for element in trips:
        if element["dep_est"] >= now - timedelta(minutes=1):
            if count < 4:
                count = count + 1
                tripdic["trip"+str(count)] = element

    #print(tripdic)

    return tripdic

sbbtrip()
