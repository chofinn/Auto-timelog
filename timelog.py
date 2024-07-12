import requests
from datetime import datetime, date, timedelta
import time
import json

url = 'http://140.124.181.95:30200/api/log/record'
with open('config.json', 'r') as f:
  myJson = json.load(fp = f)
user_id = myJson["config"]["user_id"]
print("Enter Date :")
print("Enter 't' for this week")
print("Enter 'l' for last week, 'll' for 2 week ago, and so on")
print("Or enter date directly (yyyy/mm/dd)")
t = input()
if t == "test":
  startdate = date.today() - timedelta(days=date.today().weekday())
elif t == "t":
  startdate = date.today() - timedelta(days=date.today().weekday())
elif t[0] == "l":
  startdate = date.today() - timedelta(days=date.today().weekday(), weeks=len(t))
else:
  startdate = datetime.strptime(t, "%Y/%m/%d").date()  #input format : yyyy/mm/dd
print("Start Date : " + startdate.strftime("%Y/%m/%d"))
if (startdate.weekday() != 0):
  raise Exception("wrong date")

print("'r' for routine\n'c' for custom:")
activity = input()
if activity == "r":
  week = myJson["routine"]
elif activity == "c":
  week = myJson["custom"]
else:
  raise Exception("Wrong Input")

print("press enter to start")
input()
i = 0
for jobs in week:
  for job in jobs:
    target_date = startdate + timedelta(days=i)
    myobj =  {
      "userID": user_id,
      "title": "dctrack",
      "activityTypeName": job[0],
      "startTime": "{} {}:00".format(target_date.strftime("%Y/%m/%d"), job[1]),
      "endTime": "{} {}:00".format(target_date.strftime("%Y/%m/%d"), job[2]),
      "description": "",
      "activityUnitID": user_id
    }
    if t != "test":
      x = requests.post(url, json = myobj)
      print(target_date, x.text)
      time.sleep(1)
    else:
      print(target_date, job)
  i += 1

