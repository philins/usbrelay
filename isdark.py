from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta, date
import pytz
import subprocess


city = LocationInfo(
    name='Moscow',
    region='Russian Federation',
    timezone='Europe/Moscow',
    latitude=55.75,
    longitude=37.58)
todaysDate = date.today();
tz = pytz.timezone(city.timezone)
currDate = datetime.now(tz)

s = sun(city.observer, date=todaysDate, tzinfo=city.timezone)
if s['sunrise'] + timedelta(hours = 1) < currDate < s['sunset'] - timedelta(hours = 1):
    subprocess.run(["CommandApp_USBRelay.exe", "BITFT", "close", "02"])
else:
    subprocess.run(["CommandApp_USBRelay.exe", "BITFT", "open", "02"])
