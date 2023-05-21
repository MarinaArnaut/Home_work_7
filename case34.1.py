def rhyme(song):
    str = song.lower().split()
    def f(x): return sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(str[0])
    if all([f(i) == tmp for i in str]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(rhyme("Хорошо-живет-на-свете-Винни-Пух!\
 Оттого-поет-он-эти-Песни-вслух!"))

print(rhyme("И-не-важно,-чем-он-занят,\
 Если-он-худеть-не-станет,"))

print(rhyme("А-ведь-он-худеть-не-станет,\
 Если-конечно...-Вовремя-подкрепиться..."))
