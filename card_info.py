import os
import urllib.error
import urllib.request
import json
import csv

class CardInfo:
  
  def __init__(self, card):
    self.id: card["id"]
    self.name: card["name"]
    self.name_kana: card["name_kana"]
    self.name_eng: card["name_eng"]
    self.attr: card["attr"]
    self.race: card["race"]
    self.level: card["level"]
    self.offensive: card["offensive"]
    self.defensive: card["defensive"]
    self.monster_type_1: card["monster_type_1"]
    self.monster_type_2: card["monster_type_2"]
    self.monster_type_3: card["monster_type_3"]
    self.magic_card_type: card["magic_card_type"]
    self.trap_card_type: card["trap_card_type"]
    self.card_text: card["card_text"]
    self.scale: card["scale"]
    self.pendulum: card["pendulum"]
    self.link_marker: card["link_marker"]
    self.rarity: card["rarity"]
    self.theme: card["theme"]
    self.limit_type: card["limit_type"]
    self.img: card["img"]


# ファイルパス
json_path = "output/cardinfo.json"
csv_path = "output/card_info.csv"
image_path = "output/image"

# 画像URL
url_domain = "https://appmedia.jp"

def download_file_to_dir(dst_dir, card):
    try:
      url = url_domain + card['img']
      jpg_url = url.replace(".webp", ".jpg")
      path = os.path.join(dst_dir, os.path.basename(jpg_url))
      download_file(jpg_url, path)
      print(card['id'] + " : ○")
      return path
    except urllib.error.HTTPError as e:
      print(card['id'] + " : ×")
      return ''

def download_file(url, dst_path):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    with urllib.request.urlopen(url) as web_file:
        with open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())

# json.load関数を使ったjsonファイルの読み込み
def open_json():
  with open(json_path) as f:
    data = json.load(f)
    return data

def write_card_info(card):
  with open(csv_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(card)

def main():
    # JSONファイル読み込み辞書形式に変換
    json_list = open_json()
    
    # カード情報を1件ずつ処理
    for card in json_list:
      # card = json.loads(json_data)
    
      # 画像ダウンロード
      # download_file_to_dir(image_path, card)
      
      # カード情報クラスを作成
      card_info = CardInfo(card)
      
      # CSV形式に変換
      card_info_csv = [val for val in card_info.__dict__.values()]
      
      # CSV出力
      write_card_info(card_info_csv)
  
# 実行
main()
