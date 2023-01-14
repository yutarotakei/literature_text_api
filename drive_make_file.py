# from pydrive2.auth import GoogleAuth
# from pydrive2.drive import GoogleDrive
# from oauth2client.service_account import ServiceAccountCredentials
 
# JSON_FILE = "credentials.json"
# ID = "1MqXJ_Gqf1jbHVqxSKqvkZSGQ1eHiBiPc"
 
# gauth = GoogleAuth()
# scope = ["https://www.googleapis.com/auth/drive"]
# gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE, scope)
# drive = GoogleDrive(gauth)
 
# file = drive.CreateFile({"title": "test.txt", "parents": [{"id": ID}]})
# file.SetContentString("テスト")
# file.Upload()

import os
import pprint

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

print(type(drive))
# <class 'pydrive.drive.GoogleDrive'>


f = drive.CreateFile()
f.SetContentFile('/Users/yutarotakei/Desktop/Screen Shot 2022-11-14 at 10.35.21.png')
f.Upload()