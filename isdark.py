from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta, date
import os
import pytz
import subprocess

fName = "laststatus.log"
city = LocationInfo(
    name='Moscow',
    region='Russian Federation',
    timezone='Europe/Moscow',
    latitude=55.75,
    longitude=37.58)
todaysDate = date.today();
tz = pytz.timezone(city.timezone)
currDate = datetime.now(tz)

if os.path.exists(fName):
    with open(fName, "r") as f:
        laststatus = f.read()
else:
    laststatus = "day"

s = sun(city.observer, date=todaysDate, tzinfo=city.timezone)
if s['sunrise'] + timedelta(hours = 1) < currDate < s['sunset'] - timedelta(hours = 1):
    if laststatus == "night":
        subprocess.run(["CommandApp_USBRelay.exe", "BITFT", "close", "02"])
    laststatus = "day"
else:
    if laststatus == "day":
        subprocess.run(["CommandApp_USBRelay.exe", "BITFT", "open", "02"])
    laststatus = "night"

with open(fName, "w") as w:
    w.write(laststatus)
