import requests
import json

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# エンドポイント
url = 'https://www.googleapis.com/youtube/v3/search'

# ペイロード
payload = {
    "type": "video",
    "part": "snippet",
    "q": "HIKAKIN",
    "key": "AIzaSyD9vxAlrgH0Ej9br0-dC-1vxn9iDASz_TE"
}

r = requests.get(url, params=payload)

data = json.loads(r.text)

# credentials = ServiceAccountCredentials.from_json_keyfile_name('sample-310207-19c751130f79.json', scope)
# gc = gspread.authorize(credentials)
# wks = gc.open('spreadTest').sheet1



# wks.update_acell('A1', data)
# print(wks.acell('A1'))

print(data)