student_list=['浅木','松田']
for student in student_list:
    print(f'{student}さんの試験結果を入力してください')
    network=int(input('ネットワークの得点？＞＞'))
    database=int(input('データーベースの得点？＞＞'))
    security=int(input('セキュリティの得点？＞＞'))
    if student=='浅木':
        asagi_score=[network,database,security]
        asagi_avg=sum(asagi_score)/len(asagi_score)
    else:
        matsuda_score=[network,database,security]
        matuda_avg=sum(matsuda_score)/len(matsuda_score)
print(f'浅木さんの平均点は{asagi_avg}です')
print(f'松田さんの平均点は{matuda_avg}です')