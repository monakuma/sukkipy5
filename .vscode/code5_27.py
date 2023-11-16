def eat(breakfast,lunch,dinner="カレー",*desserts):#ディホルト引数は後ろから、使う。前でつかえば後ろもせて
    print(f'朝は{breakfast}をたべました')
    print(f'昼は{lunch}をたべました')
    print(f'夕は{dinner}をたべました')
    for d in desserts:
        print(f'おやつに{d}をたべました')

eat('トースト','パスタ','カレー','アイス','チョコ','パフェ')