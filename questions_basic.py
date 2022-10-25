import pandas as pd

def basic_questions():
    dfq = pd.DataFrame(columns=["Question", "Hint", "Answer", "Code"])
    # Question 1
    q = """ 下の大文字と小文字が混じった文章を全部小文字にしてみよう。
tHiS iS lONg STRinG If I HaD THE enERgy tO tYPe More ANd moRE!!"""
    h = """.lower() を使おう"""
    a = ("this is long string if i had the energy to type more and more!!")
    c = """string='tHiS iS lONg STRinG If I HaD THE enERgy tO tYPe More ANd moRE!!'
print(string.lower())"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 2
    q = """ くじらが哺乳類かどうかIFをつかってチェックしてみよう。
哺乳類は次のカッコ内の動物です。
mammal=["うさぎ", "キリン", "オオカミ", "たぬき", "くじら"]"""
    h = """.isin() を使おう"""
    a = ("True")
    c = """ mammal=["うさぎ", "キリン", "オオカミ", "たぬき", "くじら"]
if 'くじら' in mammal:
    print('True')
else:
    print('False')"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 3
    q = """ カッコ内の数字の足し算をしてみよう。
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]"""
    h = """For loop を使おう"""
    a = ("48")
    c = """numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
total = 0
for num in numbers:
    total += num
print(total)"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 4
    q = """ 文字数をかぞえてみよう。
string = 'こんにちは。朝ですよ。'"""
    h = """len() を使おう"""
    a = ("11")
    c = """string = "こんにちは。朝ですよ。"
print(len(string))"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 5
    q = """ Dictionaryを使って電話帳をつくってみよう。
佐藤の電話番号は123987654
山田の電話番号は555044490
伊藤の電話番号は998877665"""
    h = """dictionary を使う方法は：
d = {
    "名前1": 電話番号1,
    "名前2": 電話番号2
}"""
    a = ("{'佐藤': 123987654, '山田': 555044490, '伊藤': 998877665}")
    c = """phonebook = {
    '佐藤' : 123987654,
    '山田' : 555044490,
    '伊藤' : 998877665
}
print(phonebook)"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 6
    q = """ 2つのLISTから共通している名前を探してみよう。
list1 = ['佐藤', '山田', '伊藤']
list2 = ['大谷', '伊藤', '井上']"""
    h = """a.intersection(b) を使おう"""
    a = ("{'伊藤'}")
    c = """a = set(['佐藤', '山田', '伊藤'])
b = set(['大谷', '伊藤', '井上'])
print(a.intersection(b))
"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 7
    q = """ LISTの中から空の要素を取り除きましょう。
list1 = ['佐藤', '', '山田', '', '', '伊藤']
"""
    h = """内包表記を使おう。
[l for l in list if l != '']"""
    a = ("['佐藤', '山田', '伊藤']")
    c = """list1 = ['佐藤', '', '山田', '', '', '伊藤']
print([l for l in list1 if l != ''])
"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 8
    q = """ 直角三角形の面積をもとめましょう。
底辺　= 5
高さ　= 4
面積 = （底辺　x 高さ）/ 2
"""
    h = """Pythonの掛け算は*を使います。
    面積 = （底辺　* 高さ）/2"""
    a = ("10.0")
    c = """area = (5 * 4) / 2
print(area)
"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 9
    q = """ 次の日付の年を求めましょう。
dates = '1993/09/25'
"""
    h = """split("/")を使いましょう。"""
    a = ("1993")
    c = """dates = '1993/09/25'
print(dates.split('/')[0])
"""
    dfq.loc[len(dfq)] = [q, h, a, c]
    # Question 10
    q = """ LISTの中から偶数の見つけて何個あるか数えてみよう。
list1 = [10, 21, 4, 45, 66, 93, 1]
"""
    h = """数字%2==0の場合偶数。
そうでないときは奇数です。"""
    a = ("3")
    c = """list1 = [10, 21, 4, 45, 66, 93, 1]
even_count = 0
for l in list1:
    if l % 2 == 0:
        even_count += 1
print(even_count)
"""
    dfq.loc[len(dfq)] = [q, h, a, c]

    # dfq = dfq.sample(n=10)

    return dfq
