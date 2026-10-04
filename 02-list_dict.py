# リストの定義
# それぞれのデータがリストの要素であり、0から始まるインデックス番号がついている。
income_list = [522, 548, 576, 612, 728]

# リストのインデックス0番目の要素を取り出す
print(income_list[0])

# リストの要素同士の引き算
income_sa = income_list[4] - income_list[0]
print(income_sa)

# リストに要素を追加
# 厳密にはリスト同士の連結
new_income_list = income_list + [777]
print(new_income_list)

# 新しいリストを作成する（元のリストは変更しない）
# そのため変数に代入しないと、作成した新しいリストを保持できない
new_list = income_list + [777]

# append：元のリスト自体に要素を追加する
income_list.append(777)

# + → 新しく作る（非破壊的）
# .append() → 元を直接変える（破壊的）

# forを使ってリストをいろいろ
stock_price = [484, 478, 456, 462, 473, 473, 480, 499, 508, 511, 507, 503, 504, 507]
from matplotlib import pyplot as plt
plt.plot(stock_price)
# plt.show()
plt.savefig("stock_price.png")

total = 0
for price in stock_price:
  total += price
  # input("リターン押下")

print(total)

# Forの中にif
max_price = 0
for price in stock_price:
  if max_price < price:
    max_price = price
print(max_price)

# 辞書
# キー:値
tokyo = {
  "name": "東京",
  "latitude": 35.64,
  "longitude": 137.84
}

osaka = {
  "name": "大阪",
  "latitude": 34.68,
  "longitude": 135.52
}

# 要素の取り出し
print(tokyo["latitude"])

# 辞書の要素で計算
tokyo2 = tokyo["latitude"] - osaka["latitude"]
print(tokyo2)

# 辞書の要素を置き換える
tokyo["longitude"] = 139.84
print(tokyo)

# 新しい要素の追加
tokyo["aiueo"] = 23
print(tokyo)

cities = {
  "tokyo": tokyo,
  "osaka": osaka
  }

cities["nagoya"] = {
  "name": "名古屋",
  "latitude": 35.17,
  "longitude": 136.68
}

print(cities["nagoya"]["name"])
print(cities["tokyo"]["name"])

# 辞書ループ
# キーを使用したループとなる
for key in cities:
  print(key)

for key in cities:
  name = cities[key]["name"]
  latitude = cities[key]["latitude"]
  print(name + ":" + str(latitude))

# keyだけ必要 → for key in cities
# valueだけ必要 → for value in cities.values()
# 両方必要 → for key, value in cities.items()

# タプル　名前のないデータ構造
# リストと違い[]→()になった。
# 要素を取り出すにはインデックスを指定する。
tokyo = ("東京", 35.64, 139.84)
name = tokyo[0]
latitude = tokyo[1]
longitude = tokyo[2]

print(name, "の緯度、経度は", latitude, longitude, "です")

# タプルとリストの違い
# タプルはリストの入れ替えができない。
  # 一度作ったら中身を変更できない（immutable）
# リストは同じ種類のデータを並べる。タプルは異なった種類のデータを並べる。
# アンパック　→　要確認