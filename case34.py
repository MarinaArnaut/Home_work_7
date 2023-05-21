def rhyme(str):
    str = str.split()
    My_list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        My_list.append(result)
    return len(My_list) == My_list.count(My_list[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhyme(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
