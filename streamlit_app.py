import streamlit as st
import pandas as pd
import pydeck as pdk

st.title( 'Bedford MA Interactive Police Log Viewer' )
st.write("Created by John Giaquinto")

df = pd.read_csv("Master.csv")

df['FormattedDateTime'] = pd.to_datetime(df['DateTime']).dt.date

st.sidebar.write("Select incident types")

st.write(" ")
st.write("Select start and end date")

selectiveenforcement = st.sidebar.checkbox('Selective Enforcement', value=True)
PIAC = st.sidebar.checkbox('Patrol Initiated Area Check')
alarmcommercial = st.sidebar.checkbox('Alarm Commercial')
assistFD = st.sidebar.checkbox('Assist Fire Department')
wiresdown = st.sidebar.checkbox('Wires Down')
alarmresident = st.sidebar.checkbox('Alarm Resident')
treedown = st.sidebar.checkbox('Tree Down')
ambulance = st.sidebar.checkbox('Ambulance')
otheralarm = st.sidebar.checkbox('Alarm (Other)')
informational = st.sidebar.checkbox('Informational')
directedpatrol = st.sidebar.checkbox('Directed Patrol')
hangup = st.sidebar.checkbox('911 - Hangup or Abandonded')
suspicious = st.sidebar.checkbox('Suspicious MV or Pers')
animal = st.sidebar.checkbox('Animal Call')
assistPD = st.sidebar.checkbox('Assist Other Police Department')
fireworks = st.sidebar.checkbox('Fireworks')
death = st.sidebar.checkbox('Death')
larceny = st.sidebar.checkbox('Larceny')
unwantedguest= st.sidebar.checkbox('Unwanted Guest')
mvstop = st.sidebar.checkbox('MV Stop')
BE = st.sidebar.checkbox('B&E')
harrassment = st.sidebar.checkbox('Harassment')
civilproblem = st.sidebar.checkbox('Civil Problem/Complaint')
MVDisabled = st.sidebar.checkbox('MV Disabled')
wellbeingcheck = st.sidebar.checkbox('Check Well Being')
servicecall = st.sidebar.checkbox('Service Call')
criminalharassment = st.sidebar.checkbox('258E Criminal Harassment Issue')
buildingfire = st.sidebar.checkbox('Fire Building')
powerfailure = st.sidebar.checkbox('Power Failure')
parkandwalk = st.sidebar.checkbox('Park and Walk')
annoyingcalls = st.sidebar.checkbox('Annoying Calls')
num258e = st.sidebar.checkbox('258E Service or Attempt')
fieldobservation = st.sidebar.checkbox('Field Observation')
followup = st.sidebar.checkbox('Follow-Up')
fraud = st.sidebar.checkbox('Fraud')
num209a = st.sidebar.checkbox('209A Service or Attempt')
mvcrash = st.sidebar.checkbox('MV Crash No Injury')
disturbance = st.sidebar.checkbox('Disturbance')
waterproblem = st.sidebar.checkbox('Water Problem')
noisecomplaint = st.sidebar.checkbox('Noise Complaint')
trafficcomplaint = st.sidebar.checkbox('Traffic Complaint')
arrestwarrant = st.sidebar.checkbox('Arrest - Warrant')
mverratic = st.sidebar.checkbox('MV Erratic Operator')
roadhazard = st.sidebar.checkbox('Hazard - Road')
NEMLEC = st.sidebar.checkbox('NEMLEC Call Out')
missingkid = st.sidebar.checkbox('Missing Juvenile')
checkbuilding = st.sidebar.checkbox('Check Building')
houselockout = st.sidebar.checkbox('Lockout House')
hitandrun = st.sidebar.checkbox('MV Hit and Run Crash')
servecourtdocs = st.sidebar.checkbox('Serve Court Documents')
gasleak = st.sidebar.checkbox('Odor Gas/Oil/Other')
trespass = st.sidebar.checkbox('Trespass Letter on File')
propertylfr = st.sidebar.checkbox('Property - Any L/F/R')
carfire = st.sidebar.checkbox('Fire Car')
missingperson = st.sidebar.checkbox('Missing Person')
safteyseat = st.sidebar.checkbox('Child Passenger Safety Seat')
mvcrashinjury = st.sidebar.checkbox('MV Crash - Injury')
trafficservice = st.sidebar.checkbox('Traffic Function / Service')
hazard = st.sidebar.checkbox('Hazard')
propertydamage = st.sidebar.checkbox('Property Damage')
transport = st.sidebar.checkbox('Transport')
drugviolation = st.sidebar.checkbox('Drug Law Violation')
larceny = st.sidebar.checkbox('Larceny - Shoplifting')
threatening = st.sidebar.checkbox('Threatening')
overdose = st.sidebar.checkbox('Overdose - Medical')
vandalism = st.sidebar.checkbox('Vandalism')
mvviolation = st.sidebar.checkbox('MV Violation')
section12 = st.sidebar.checkbox('Section 12')
eldderaffairs = st.sidebar.checkbox('Elder Affairs Incident')
miscfire = st.sidebar.checkbox('Fire Misc.')
arrest = st.sidebar.checkbox('Arrest')
mvcrashbike = st.sidebar.checkbox('MV Crash - Cyclist')
BEMV = st.sidebar.checkbox('B & E M.V.')
mvlockout = st.sidebar.checkbox('Lockout MV')
fieldinterview = st.sidebar.checkbox('Field Interview')
notification = st.sidebar.checkbox('Notification')
escort = st.sidebar.checkbox('Escort/Funeral/Parad es etc.')
assault = st.sidebar.checkbox('Assault & Battery')
weaponsviolation = st.sidebar.checkbox('Weapons Violation')
mvtowed = st.sidebar.checkbox('MV Towed')
OUI = st.sidebar.checkbox('Oper Under Influence')
bylawviolation = st.sidebar.checkbox('By-Law Violation')
schoolbusincident = st.sidebar.checkbox('School Bus Incident')
sexoffender = st.sidebar.checkbox('Sex Offender Registration')
schoolincident = st.sidebar.checkbox('School Related Incident')
tresspassing = st.sidebar.checkbox('Trespassing')
RO258EE = st.sidebar.checkbox('258E RO Violation')
dumping = st.sidebar.checkbox('Illegal Dumping')
forgery = st.sidebar.checkbox('Forgery / Uttering')
roadrage = st.sidebar.checkbox('MV Road Rage Incident')
overdueperson = st.sidebar.checkbox('Overdue MV/Person')
alcoholoffense = st.sidebar.checkbox('Alcohol Offense')
suspackage = st.sidebar.checkbox('Suspicious Package')
SRO = st.sidebar.checkbox('SRO Function / Service')
cycliststop = st.sidebar.checkbox('MV Stop - Cyclist')
MVCrashPedestrian = st.sidebar.checkbox('MV Crash - Pedestrian')
protectivecustody = st.sidebar.checkbox('Protective Custody')
larcenymv = st.sidebar.checkbox('Larceny of MV')

incident_type_list=[]

if selectiveenforcement:
    incident_type_list.append("Selective Enforcement")
if PIAC:
    incident_type_list.append("Patrol Initiated Area Check")
if alarmcommercial:
    incident_type_list.append("Alarm Commercial")
if assistFD:
    incident_type_list.append("Assist Fire Department")
if wiresdown:
    incident_type_list.append("Wires Down")
if alarmresident:
    incident_type_list.append("Alarm Resident")
if treedown:
    incident_type_list.append("Tree Down")
if ambulance:
    incident_type_list.append("Ambulance")
if otheralarm:
    incident_type_list.append("Alarm (Other)")
if informational:
    incident_type_list.append("Informational")
if directedpatrol:
    incident_type_list.append("Directed Patrol")
if hangup:
    incident_type_list.append("911 - Hangup or Abandonded")
if suspicious:
    incident_type_list.append("Suspicious MV or Pers")
if animal:
    incident_type_list.append("Animal Call")
if assistPD:
    incident_type_list.append("Assist Other Police Department")
if fireworks:
    incident_type_list.append("Fireworks")
if death:
    incident_type_list.append("Death")
if larceny:
    incident_type_list.append("Larceny")
if unwantedguest:
    incident_type_list.append("Unwanted Guest")
if mvstop:
    incident_type_list.append("MV Stop")
if BE:
    incident_type_list.append("B&E")
if harrassment:
    incident_type_list.append("Harassment")
if civilproblem:
    incident_type_list.append("Civil Problem/Complaint")
if MVDisabled:
    incident_type_list.append("MV Disabled")
if wellbeingcheck:
    incident_type_list.append("Check Well Being")
if servicecall:
    incident_type_list.append("Service Call")
if criminalharassment:
    incident_type_list.append("258E Criminal Harassment Issue")
if buildingfire:
    incident_type_list.append("Fire Building")
if powerfailure:
    incident_type_list.append("Power Failure")
if parkandwalk:
    incident_type_list.append("Park and Walk")
if annoyingcalls:
    incident_type_list.append("Annoying Calls")
if num258e:
    incident_type_list.append("258E Service or Attempt")
if fieldobservation:
    incident_type_list.append("Field Observation")
if followup:
    incident_type_list.append("Follow-Up")
if fraud:
    incident_type_list.append("Fraud")
if num209a:
    incident_type_list.append("209A Service or Attempt")
if mvcrash:
    incident_type_list.append("MV Crash No Injury")
if disturbance:
    incident_type_list.append("Disturbance")
if waterproblem:
    incident_type_list.append("Water Problem")
if noisecomplaint:
    incident_type_list.append("Noise Complaint")
if trafficcomplaint:
    incident_type_list.append("Traffic Complaint")
if arrestwarrant:
    incident_type_list.append("Arrest - Warrant")
if mverratic:
    incident_type_list.append("MV Erratic Operator")
if roadhazard:
    incident_type_list.append("Hazard - Road")
if NEMLEC:
    incident_type_list.append("NEMLEC Call Out")
if missingkid:
    incident_type_list.append("Missing Juvenile")
if checkbuilding:
    incident_type_list.append("Check Building")
if houselockout:
    incident_type_list.append("Lockout House")
if hitandrun:
    incident_type_list.append("MV Hit and Run Crash")
if servecourtdocs:
    incident_type_list.append("Serve Court Documents")
if gasleak:
    incident_type_list.append("Odor Gas/Oil/Other")
if trespass:
    incident_type_list.append("Trespass Letter on File")
if propertylfr:
    incident_type_list.append("Property - Any L/F/R")
if carfire:
    incident_type_list.append("Fire Car")
if missingperson:
    incident_type_list.append("Missing Person")
if safteyseat:
    incident_type_list.append("Child Passenger Safety Seat")
if mvcrashinjury:
    incident_type_list.append("MV Crash - Injury")
if trafficservice:
    incident_type_list.append("Traffic Function / Service")
if hazard:
    incident_type_list.append("Hazard")
if propertydamage:
    incident_type_list.append("Property Damage")
if transport:
    incident_type_list.append("Transport")
if drugviolation:
    incident_type_list.append("Drug Law Violation")
if larceny:
    incident_type_list.append("Larceny - Shoplifting")
if threatening:
    incident_type_list.append("Threatening")
if overdose:
    incident_type_list.append("Overdose - Medical")
if vandalism:
    incident_type_list.append("Vandalism")
if mvviolation:
    incident_type_list.append("MV Violation")
if section12:
    incident_type_list.append("Section 12")
if eldderaffairs:
    incident_type_list.append("Elder Affairs Incident")
if miscfire:
    incident_type_list.append("Fire Misc.")
if arrest:
    incident_type_list.append("Arrest")
if mvcrashbike:
    incident_type_list.append("MV Crash - Cyclist")
if BEMV:
    incident_type_list.append("B & E M.V.")
if mvlockout:
    incident_type_list.append("Lockout MV")
if fieldinterview:
    incident_type_list.append("Field Interview")
if notification:
    incident_type_list.append("Notification")
if escort:
    incident_type_list.append("Escort/Funeral/Parad es etc.")
if assault:
    incident_type_list.append("Assault & Battery")
if weaponsviolation:
    incident_type_list.append("Weapons Violation")
if mvtowed:
    incident_type_list.append("MV Towed")
if OUI:
    incident_type_list.append("Oper Under Influence")
if bylawviolation:
    incident_type_list.append("By-Law Violation")
if schoolbusincident:
    incident_type_list.append("School Bus Incident")
if sexoffender:
    incident_type_list.append("Sex Offender Registration")
if schoolincident:
    incident_type_list.append("School Related Incident")
if tresspassing:
    incident_type_list.append("Trespassing")
if RO258EE:
    incident_type_list.append("258E RO Violation")
if dumping:
    incident_type_list.append("Illegal Dumping")
if forgery:
    incident_type_list.append("Forgery / Uttering")
if roadrage:
    incident_type_list.append("MV Road Rage Incident")
if overdueperson:
    incident_type_list.append("Overdue MV/Person")
if alcoholoffense:
    incident_type_list.append("Alcohol Offense")
if suspackage:
    incident_type_list.append("Suspicious Package")
if SRO:
    incident_type_list.append("SRO Function / Service")
if cycliststop:
    incident_type_list.append("MV Stop - Cyclist")
if MVCrashPedestrian:
    incident_type_list.append("MV Crash - Pedestrian")
if protectivecustody:
    incident_type_list.append("Protective Custody")
if larcenymv:
    incident_type_list.append("Larceny of MV")

address_location = df[["FormattedDateTime", "DateTime", "Address", "IncidentType", "ActionTaken", "Remarks", "Lat", "Lon"]]
address_location = address_location[address_location['IncidentType'].isin(incident_type_list)]

min_date = address_location["FormattedDateTime"].min()
max_date = address_location["FormattedDateTime"].max()
date_start = st.date_input('Start date', min_date)
date_end = st.date_input('End date', max_date)

if (date_start < date_end) == False:
    st.error('Error: End date must fall after start date.')

address_location = address_location[(address_location['FormattedDateTime'] > date_start) & (address_location['FormattedDateTime'] < date_end)]
address_location['FormattedDateTime'] = pd.to_datetime(df['FormattedDateTime'])

#https://deckgl.readthedocs.io/en/latest/index.html
st.write("Map of selected police incidents:")

#ViewState represents where the state of a viewport, essentially where the screen is focused
# zoom is between 0 (whole world) and 24 (individual building)
# pitch is the up/down angle relative to the map’s plane, with 0 being looking directly at the map
view_state = pdk.ViewState(
    latitude=address_location["Lat"].mean(),
    longitude=address_location["Lon"].mean(),
    zoom = 13,
    pitch = 0)

# a scatterplot layer
layer1 = pdk.Layer('ScatterplotLayer',
                  data = address_location,
                  get_position = '[Lon, Lat]',
                  get_radius = 5,
                  get_color = [0,0,255],
                  pickable = True)

tool_tip = {"html": "Time:<br/> <b>{DateTime}</b>\
                    <br/><br/>Address:<br/> <b>{Address}</b>\
                    <br/><br/>Incident Type:<br/> <b>{IncidentType}</b>\
                    <br/><br/>ActionTaken:<br/> <b>{ActionTaken}</b>\
                    <br/><br/>Remarks:<br/> <b>{Remarks}</b> ",
            "style": { "backgroundColor": "steelblue",
                        "color": "white"}}

#https://deckgl.readthedocs.io/en/latest/deck.html
# mapbox://styles/mapbox/light-v9
map = pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=view_state,
    layers=[layer1],
    tooltip= tool_tip
)

st.pydeck_chart(map)