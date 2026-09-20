# 変数代入
height = 3
width = 10
print(height)
area = height * width
print(area)

# 関数 ・・・入力→処理→出力を意識する
def calculate_circle_area(radius):
  pi = 3.14
  area = radius ** 2 * pi
  return area

## 呼び出し
cal = calculate_circle_area(100)
print(cal)

# 引数が複数ある関数
def calc_rectangle_area(height, width):
  area = height * width
  return area

## 呼び出し
calc2 = calc_rectangle_area(5, 12)
print(calc2)

# 組み込み関数
print(pow(2,10))

# 文字列型
temp = 23
print("ただいまの気温:", temp)

## 文字列の足し算
era_name = "令和"
year_name = "8年"
wareki = era_name + year_name
print(wareki)

## 数値を文字列に変換する
era_name = "令和"
year = 7
wareki = era_name + str(year)
print(wareki) # 令和7

## f文字列
wareki = f"令和{year}年"
print(wareki)

## キーボードからの入力を変数に代入
year_str = input("西暦を入力してください:")
print (int(year_str))

# if文
year = 2018
wareki_year = year - 1988
if year > 2018:
  wareki_year = year - 2018
print(wareki_year)

## else
year = 1989
era_name = "昭和"
wareki_year = year - 1925

if 1989 <= year < 2019:
  era_name = "平成"
  wareki_year = year - 1988
elif 2019 <= year:
  era_name = "令和"
  wareki_year = year - 2018

wareki = era_name + f"{wareki_year}年"
print(wareki)