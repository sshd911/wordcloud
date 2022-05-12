# キーの重複は出来ません。
prfm = {'a-chan': 'Perfume', 'KASHIYUKA': 'Perfume', 'NOCCHi': 'Perfume'}
print(prfm)
# 値にはキーでアクセスします。
print(prfm['a-chan'])
print(prfm['KASHIYUKA'])
print(prfm['NOCCHi'])
# 辞書への追加はメソッドupdate()を使用します。
team_prfm_dict = {'MIKIKO': 'Team Perfume'}
prfm.update(team_prfm_dict)
print(prfm)
# 値は任意のオブジェクトが扱えます。次の例はタプルを値としています。tapple -> () 
prfm_wt_dict = {
    2012: ('Perfume WORLD TOUR 1st', 'B00MXXEXUA'),
    2013: ('Perfume WORLD TOUR 2nd', 'B00MXXEXUU'),
    2014: ('Perfume WORLD TOUR 3rd', 'B00YRSC39W'),
    2019: ('Perfume WORLD TOUR 4th ｢FUTURE POP｣', 'B07TGCNDS3')}

# items() が返却するのは dict_items クラスのインスタンスです。dict_items クラスは、繰り返しを行うことが可能なイリタブル( iterable / 意味 反復可能) なクラスです。
# KeyとValueの参照の方法
for key, value in prfm_wt_dict.items():
    print(key, "->", value)

# 辞書をキーでソートしたい時、関数 sorted() を使います。sorted() はソートしたキーのリストを返します。
# キーがソートされてlistで返される
print(sorted(prfm_wt_dict))
published_years = sorted(prfm_wt_dict)
# 最後をアクセスするには、インデックスに-1を指定します。
print(published_years[-1])
print(prfm_wt_dict[published_years[-1]])

live_title, amazon_dp = prfm_wt_dict[published_years[-1]]
print(live_title)
print("https://amazon.co.jp/dp/"+amazon_dp)
