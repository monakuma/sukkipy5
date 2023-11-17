def is_leapyear(ad_num):
    if ad_num %400==0 or ad_num %4==0:
        print(f'西暦{ad_num}年はうるう年である')
    elif ad_num %100==0:
        print(f'西暦{ad_num}年はうるう年ではない')
    else:
        print(f'西暦{ad_num}年はうるう年ではない')    



ad_num=int(input('調べたい西暦を数字で入力してください＞＞'))
is_leapyear(ad_num)


