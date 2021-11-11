n, i, m, g, gg = 0, 0, 0, 0, 0

n = int(input())

if n > 1983:
    while n > 1983:
        n -= 60
        m = n - 1923
else:
    while n < 1983:
        n += 60
        m = n - 1983

g = (m // 12) + 1
gg = m % 12

result = ''

if g == 1:
    result = 'зеленой'
elif g == 2:
    result = 'красной'
elif g == 3:
    result = 'желтой'
elif g == 4:
    result = 'белой'
elif g == 5:
    result = 'черной'
elif g == 6:
    result = 'черной'

if gg == 1:
    result += 'крысы'
elif gg == 2:
    result += 'коровы'
elif gg == 3:
    result += ' тигра'
elif gg == 4:
    result += ' зайца'
elif gg == 5:
    result += ' дракона'
elif gg == 6:
    result += ' змеи'
elif gg == 7:
    result += ' лошади'
elif gg == 8:
    result += ' овцы'
elif gg == 9:
    result += ' обезьяны'
elif gg == 10:
    result += ' курицы'
elif gg == 11:
    result += ' собаки'
elif gg == 0:
    result += ' свиньи'

print(result)