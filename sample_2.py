import requests
import json

#ハイフンありなしどちらでも入力可能
postal_code = input("郵便番号を入力してください(7桁)")
#呼びだすAPI元のURL
RECEST_URL = "http://zipcloud.ibsnet.co.jp/api/search?zipcode={0}".format(postal_code)

#住所
address = ""
#住所のカナ
kana = ""

response = requests.get(RECEST_URL)
json_result = response.text
#json文字列から辞書型へ変換
json_to_dic_result = json.loads(response.text)

#該当する情報の判定
#2019/02/06追記 != None を == Noneへ変更
if json_to_dic_result["message"] == None:
    result_dic = json_to_dic_result["results"][0]
else:
    print("お探しの住所は見つかりませんでした(´・∀・｀)")
    sys.exit()

for i in range(1, 4):
    address += result_dic["address" + str(i)]
    kana += result_dic["kana" + str(i)]

context = {"郵便番号:": postal_code, "カナ:": kana, "住所:": address}

print("|-- {0:^10} --|".format("検索結果"))
for k, v in context.items():
    print(k, v)